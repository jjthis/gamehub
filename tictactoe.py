import pygame, sys
pygame.init()
pygame.font.init()
size = 300
screen = pygame.display.set_mode((size, size))
board = [[0]*3 for _ in range(3)]
turn = 1
game_over = False
font = pygame.font.SysFont(None, 80)

while True:
    screen.fill((255,255,255))
    pygame.draw.line(screen, (0,0,0), (0, size//3), (size, size//3), 2)
    pygame.draw.line(screen, (0,0,0), (0, 2*size//3), (size, 2*size//3), 2)
    pygame.draw.line(screen, (0,0,0), (size//3, 0), (size//3, size), 2)
    pygame.draw.line(screen, (0,0,0), (2*size//3, 0), (2*size//3, size), 2)
    # 말
    for y in range(3):
        for x in range(3):
            if board[y][x]:
                txt = font.render('X' if board[y][x]==1 else 'O', True, (0,0,0))
                screen.blit(txt, (x*size//3+30, y*size//3+30))
    # 승리 체크
    win = 0
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2]!=0: win=board[i][0]
        if board[0][i]==board[1][i]==board[2][i]!=0: win=board[0][i]
    if board[0][0]==board[1][1]==board[2][2]!=0: win=board[0][0]
    if board[0][2]==board[1][1]==board[2][0]!=0: win=board[0][2]
    if win or all(board[y][x] for y in range(3) for x in range(3)):
        game_over = True
        msg = 'draw' if not win else ('X win' if win==1 else 'O win')
        txt = font.render(msg, True, (200,0,0))
        screen.blit(txt, (30, size//2-40))
    pygame.display.flip()
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            pygame.quit(); sys.exit()
        if e.type==pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = e.pos[0]//(size//3), e.pos[1]//(size//3)
            if board[y][x]==0:
                board[y][x]=turn
                turn=3-turn
        if e.type==pygame.KEYDOWN and e.key==pygame.K_r:
            board=[[0]*3 for _ in range(3)]
            turn=1
            game_over=False
