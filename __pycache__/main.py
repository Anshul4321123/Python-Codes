import pygame
import time
import random
pygame.font.init()


WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

BG = pygame.transform.scale(pygame.image.load("image.png"), (WIDTH, HEIGHT))

PLAYER_VEL = 5
STAR_WIDTH = 10
STAR_HEIGHT = 10
STAR_VEL = 3


FONT = pygame.font.SysFont("comicsans", 30)

PLAYER_WIDTH = 20
PLAYER_HEIGHT = 30


def draw(player, elapsed_time, stars, score):
    WIN.blit(BG, (0, 0))

    time_text = FONT.render(f"Time: {int(elapsed_time)}", 1, "white")
    WIN.blit(time_text, (10, 10))

    score_text = FONT.render(f"Score: {int(score)}", 1, "white")
    WIN.blit(score_text, (10, 40))

    pygame.draw.rect(WIN, "red", player)

    for star in stars:
        pygame.draw.rect(WIN, "yellow", star)

    pygame.display.update()


def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0
    score = 0
    star_add_increment = 2000
    star_count = 0
    stars = []

    pygame.init()
    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if star_count >= star_add_increment:
            for _ in range(5):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, 0, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)
            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + PLAYER_WIDTH <= WIDTH:
            player.x += PLAYER_VEL

        hit = False
        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
                score += 0.2
            elif star.y >= player.y and star.colliderect(player):
                stars.remove(star)
                hit =True
                break

        if hit:
            lost_text = FONT.render("You lost!", 1, "red")
            WIN.blit(lost_text, (WIDTH // 2 - lost_text.get_width() // 2, HEIGHT // 2 - lost_text.get_height() // 2))
            pygame.display.update()
            pygame.time.delay(2000)
            break

        draw(player, elapsed_time, stars, score)

    pygame.quit()


if __name__ == "__main__":
    main()
