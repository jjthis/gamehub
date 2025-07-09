import random, pygame,sys

pygame.init()
SIZE = 1000
screen = pygame.display.set_mode((SIZE, SIZE))
font = pygame.font.Font("font.ttf", 80)

direction = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
text = ['<', '>', 'ㅅ', 'v']

def makeRand(n):
    randDir = [random.randint(0,3) for _ in range(n)]
    return randDir


randDir = makeRand(10)

print(randDir)
correct = 0
score = 0

while True:
    
    if correct == len(randDir):
        randDir = makeRand(10)
        correct = 0
        score += 1

    screen.fill((255,255,255))

    ncorrectStr = ''
    correctStr = ''
    for i in range(correct, len(randDir)):
        ncorrectStr += text[randDir[i]]
    for i in range(correct):
        correctStr += text[randDir[i]]
    
    txt = font.render(correctStr, True, (0,255,0))
    txt2 = font.render(ncorrectStr, True, (0,0,0))
    txt3 = font.render(f"점수: {score}", True, (0,0,0))
    screen.blit(txt, (50, SIZE//2))
    screen.blit(txt2, (txt.get_width()+50, SIZE//2))
    screen.blit(txt3, (50, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_LEFT:
            #     print("LEFT")
            # if event.key == pygame.K_RIGHT:
            #     print("RIGHT")
            # if event.key == pygame.K_UP:
            #     print("UP")
            # if event.key == pygame.K_DOWN:
            #     print("DOWN")
            if event.key == direction[randDir[correct]]:
                correct += 1
                print("OK")
    pygame.display.flip()
