from fastapi import FastAPI, HTTPException
from Pydantic import BaseModel
from typing import Optional, List, Dict
from uuid import uuid4

app = FastAPI()

games: Dict[str, dict] = {}


class CreateGameRequest(BaseModel):
    player: str


class JoinGameRequest(BaseModel):
    player: str


class MoveRequest(BaseModel):
    player: str
    row: int
    col: int

# Helper functions


def check_winner(board, player):
    # Rows, columns, diagonals
    return any(
        all(cell == player for cell in line)
        for line in (
            board,                              # rows
            zip(*board),                        # columns
            [[board[i][i] for i in range(3)]],  # main diag
            [[board[i][2-i] for i in range(3)]]  # anti diag
        )
    )


def is_draw(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)


@app.post("/create_game")
def create_game(request: CreateGameRequest):
    game_id = str(uuid4())
    board = [[" "]*3 for _ in range(3)]
    games[game_id] = {
        "board": board,
        "players": {request.player: True},
        "turn": "X",
        "winner": None
    }
    return {"game_id": game_id}


@app.post("/join_game/{game_id}")
def join_game(game_id: str, request: JoinGameRequest):
    game = games.get(game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")

    if request.player in game["players"]:
        return {"message": "Already joined."}

    if len(game["players"]) >= 2:
        raise HTTPException(status_code=400, detail="Game full")

    game["players"][request.player] = True
    return {"message": f"Player {request.player} joined"}


@app.post("/move/{game_id}")
def make_move(game_id: str, request: MoveRequest):
    game = games.get(game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")

    board = game["board"]
    if request.player != game["turn"]:
        raise HTTPException(status_code=400, detail="Not your turn")

    if board[request.row][request.col] != " ":
        raise HTTPException(status_code=400, detail="Cell already taken")

    board[request.row][request.col] = request.player

    if check_winner(board, request.player):
        game["winner"] = request.player
        return {"message": f"Player {request.player} wins!"}

    if is_draw(board):
        game["winner"] = "Draw"
        return {"message": "Game is a draw."}

    game["turn"] = "O" if request.player == "X" else "X"
    return {"message": "Move accepted", "next_turn": game["turn"]}


@app.get("/state/{game_id}")
def get_state(game_id: str):
    game = games.get(game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")

    return {
        "board": game["board"],
        "turn": game["turn"],
        "winner": game["winner"]
    }
