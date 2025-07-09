import pygame, sys, random
pygame.init()
wsize = 1200
hsize = 400

screen = pygame.display.set_mode((wsize, hsize))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)

ROWS, COLS = 5, 15  # n*m 격자
APPLE_RADIUS = 25
MARGIN = 40

apples = []
cell_w = (wsize - 2*MARGIN) // (COLS-1) if COLS>1 else 0
cell_h = (hsize - 2*MARGIN) // (ROWS-1) if ROWS>1 else 0
for row in range(ROWS):
    for col in range(COLS):
        x = MARGIN + col*cell_w
        y = MARGIN + row*cell_h
        n = random.randint(1, 9)
        apples.append([x, y, n])

dragging = False
start_pos = None
end_pos = None

while True:
    screen.fill((255,255,255))
    # 사과 그리기
    for x, y, n in apples:
        pygame.draw.circle(screen, (255,0,0), (x, y), APPLE_RADIUS)
        pygame.draw.rect(screen, (0,150,0), (x-5, y-APPLE_RADIUS-15, 10, 20))
        txt = font.render(str(n), True, (255,255,255))
        rect = txt.get_rect(center=(x, y))
        screen.blit(txt, rect)
    # 드래그 사각형 그리기
    if dragging and start_pos and end_pos:
        x1, y1 = start_pos
        x2, y2 = end_pos
        rect = pygame.Rect(min(x1,x2), min(y1,y2), abs(x2-x1), abs(y2-y1))
        pygame.draw.rect(screen, (0,0,255), rect, 3)
    pygame.display.flip()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            dragging = True
            start_pos = e.pos
            end_pos = e.pos
        if e.type == pygame.MOUSEMOTION and dragging:
            end_pos = e.pos
        if e.type == pygame.MOUSEBUTTONUP and dragging:
            dragging = False
            x1, y1 = start_pos
            x2, y2 = end_pos
            rect = pygame.Rect(min(x1,x2), min(y1,y2), abs(x2-x1), abs(y2-y1))
            selected = [i for i, (x, y, n) in enumerate(apples) if rect.collidepoint(x, y)]
            total = sum(apples[i][2] for i in selected)
            if total == 10:
                for i in sorted(selected, reverse=True):
                    apples.pop(i)
            start_pos = None
            end_pos = None
    clock.tick(60)
