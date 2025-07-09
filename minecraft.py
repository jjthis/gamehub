import pygame, sys
pygame.init()

# 화면 크기 및 그리드 설정
TILE = 40
COLS, ROWS = 20, 15
WIDTH, HEIGHT = TILE*COLS, TILE*ROWS
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# 바닥(블럭) 데이터
blocks = [[0 for _ in range(COLS)] for _ in range(ROWS)]

# 플레이어 위치 (행, 열)
player = [ROWS//2, COLS//2]

while True:
    screen.fill((135, 206, 235))  # 하늘색 배경
    # 바닥 그리기
    for r in range(ROWS):
        for c in range(COLS):
            if blocks[r][c]:
                pygame.draw.rect(screen, (139,69,19), (c*TILE, r*TILE, TILE, TILE))
            pygame.draw.rect(screen, (200,200,200), (c*TILE, r*TILE, TILE, TILE), 1)
    # 플레이어 그리기
    pr, pc = player
    pygame.draw.rect(screen, (0,0,255), (pc*TILE+5, pr*TILE+5, TILE-10, TILE-10))
    pygame.display.flip()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            mx, my = e.pos
            c, r = mx//TILE, my//TILE
            if 0<=r<ROWS and 0<=c<COLS:
                blocks[r][c] = 1
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_w and player[0]>0:
                player[0] -= 1
            if e.key == pygame.K_s and player[0]<ROWS-1:
                player[0] += 1
            if e.key == pygame.K_a and player[1]>0:
                player[1] -= 1
            if e.key == pygame.K_d and player[1]<COLS-1:
                player[1] += 1
    clock.tick(60)
