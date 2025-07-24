from fastapi import FastAPI, Request
from fastapi.responses import Response

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"Request to {request.url.path} received.")
    response: Response = await call_next(request)
    print(f"Response with status {response.status_code} sent.")
    return response

@app.get("/")
async def home():
    return "Hello, Middleware!"

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, debug=True)
