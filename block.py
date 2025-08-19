import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("벽돌깨기")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

PADDLE_WIDTH = 100
PADDLE_HEIGHT = 15

BallPos = random.randint(0 + PADDLE_WIDTH // 2,WIDTH - PADDLE_WIDTH // 2)

paddle = pygame.Rect(BallPos - PADDLE_WIDTH // 2, HEIGHT - 40, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_speed = 10

BALL_RADIUS = 10
ball = pygame.Rect(BallPos, HEIGHT - 80, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_dx = 5 * random.choice((1, -1))
ball_dy = -5

BRICK_ROWS = 6
BRICK_COLS = 10
BRICK_WIDTH = WIDTH // BRICK_COLS
BRICK_HEIGHT = 30
bricks = []
for row in range(BRICK_ROWS):
    for col in range(BRICK_COLS):
        brick = pygame.Rect(col * BRICK_WIDTH, row * BRICK_HEIGHT + 50, BRICK_WIDTH - 2, BRICK_HEIGHT - 2)
        bricks.append(brick)

score = 0
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()

running = True

start = False

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
            start = True


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.x += paddle_speed


    

    if start:
        ball.x += ball_dx
        ball.y += ball_dy

    if ball.left <= 0 or ball.right >= WIDTH:
        ball_dx *= -1
    if ball.top <= 0:
        ball_dy *= -1
    if ball.bottom >= HEIGHT:
        win_text = font.render("GameOver!", True, (0, 128, 0))
        screen.blit(win_text, (WIDTH // 2 - 60, HEIGHT // 2 - 20))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    if ball.colliderect(paddle):
        ball_dy *= -1
        ball.y = paddle.y - BALL_RADIUS * 2

    hit_index = ball.collidelist(bricks)
    if hit_index != -1:
        hit_brick = bricks.pop(hit_index)
        ball_dy *= -1
        score += 10

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, paddle)
    pygame.draw.ellipse(screen, RED, ball)
    for brick in bricks:
        pygame.draw.rect(screen, GREEN, brick)
    score_text = font.render(f"score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    if not bricks:
        win_text = font.render("clear!", True, (0, 128, 0))
        screen.blit(win_text, (WIDTH // 2 - 60, HEIGHT // 2 - 20))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    pygame.display.flip()

pygame.quit()
sys.exit()
