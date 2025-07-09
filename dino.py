import pygame
import sys
import random

pygame.init()
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (255, 0, 0)


dino = pygame.Rect(50, HEIGHT - 100, 50, 100)  # x, y, width, height
dino_vel_y = 0
gravity = 1
jump_strength = 15
on_ground = True

obstacles = []
obstacle_speed = 10
spawn_timer = 0

score = 0
font = pygame.font.SysFont(None, 40)

def spawn_obstacle():
    height = 70
    width = 20
    x = WIDTH
    y = HEIGHT - height - 50  # 땅 위치 맞춤
    if random.random() < 0.3:
        y = HEIGHT - height - 200
    elif random.random() < 0.5:
        y = HEIGHT - height - 120

    return pygame.Rect(x, y, width, height)

isSmall = False
startSmall = 0



while True:
    screen.fill(WHITE)

    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))
    
    if pygame.time.get_ticks() - startSmall > 500:
        isSmall = False


    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            pygame.quit(); sys.exit()
        if e.type==pygame.KEYDOWN:
            if e.key==pygame.K_SPACE or e.key==pygame.K_UP:
                isSmall = False
                if on_ground:
                    dino_vel_y = -jump_strength
                    on_ground = False
            if e.key==pygame.K_DOWN and not isSmall and on_ground:
                isSmall = True
                startSmall = pygame.time.get_ticks()
                dino.y = HEIGHT - 50
    dino.height = 100 if not isSmall else 50

    # 중력 적용
    dino_vel_y += gravity
    dino.y += dino_vel_y

    # 바닥 충돌 처리
    if dino.bottom >= HEIGHT - 50:
        dino.bottom = HEIGHT - 50
        # dino_vel_y = 0
        on_ground = True


    # 공룡 그리기
    pygame.draw.rect(screen, GREEN, dino)

    # 장애물 생성
    spawn_timer += 1
    if spawn_timer > 60:
        obstacles.append(spawn_obstacle())
        spawn_timer = 0

    # 장애물 이동 및 그리기
    for obs in obstacles[:]:
        obs.x -= obstacle_speed
        pygame.draw.rect(screen, RED, obs)
        if obs.right < 0:
            obstacles.remove(obs)
            score += 1

        if dino.colliderect(obs):
            print("Game Over! 점수:", score)
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(60)
