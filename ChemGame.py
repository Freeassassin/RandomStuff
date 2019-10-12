import pygame 
bg = pygame.transform.scale(pygame.image.load('bg.png'),(640,480))
bg1 = pygame.transform.scale(pygame.image.load('bg.png'),(640,480))
WALK =[pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("w1.png"))),pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("w1.png"))),pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("w2.png"))),pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("w2.png"))),pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("w3.png"))),pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("w3.png"))),pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("w4.png"))),pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("w4.png")))]
i = 0
BG_LOC = [0,640]
def main():
    global i
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

        screen.blit(bg, (BG_LOC[0],0))
        screen.blit(bg1, (BG_LOC[1],0))
        if BG_LOC[0] <= -640:
        	BG_LOC[0] = 0
        if BG_LOC[1] == 0:
        	BG_LOC[1] = 640
        BG_LOC[0] -= 5
        BG_LOC[1] -= 5
        screen.blit(WALK[i], (100,300))
        pygame.display.flip()
        clock.tick(30)
        i +=1
        if i == 8:
        	i = 0

if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()