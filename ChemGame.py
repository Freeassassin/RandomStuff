import pygame

BG = pygame.transform.scale(pygame.image.load('BG.png'),(640,480))
BG1 = pygame.transform.scale(pygame.image.load('BG.png'),(640,480))
WALK =[pygame.image.load("w1.png"),pygame.image.load("w1.png"),pygame.image.load("w2.png"),pygame.image.load("w2.png"),pygame.image.load("w3.png"),pygame.image.load("w3.png")]
GOOMBA = pygame.transform.scale(pygame.image.load("g.png"), (80,80))
i = 0
BG_LOC = [0,640]
GX = 640


def main():
    global i
    global GX
    screen = pygame.display.set_mode((640, 480))
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.blit(BG, (BG_LOC[0],0))
        screen.blit(BG1, (BG_LOC[1],0))
        if BG_LOC[0] <= -640:
        	BG_LOC[0] = 0
        if BG_LOC[1] == 0:
        	BG_LOC[1] = 640
        if GX == 0:
        	GX = 640
        BG_LOC[0] -= 5
        BG_LOC[1] -= 5
        GX -= 5
        screen.blit(WALK[i], (0,225))
        screen.blit(GOOMBA, (GX,315))
        pygame.display.flip()
        clock.tick(24)
        i +=1
        if i == 6:
        	i = 0

if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()