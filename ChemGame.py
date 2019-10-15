import pygame
pygame.init()

class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the SCREEN
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            FONT = pygame.font.SysFont('cour.ttf', 40)
            text = FONT.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

BACK_B = button((225,0,0), 560, 310, 160, 80, "Back")
QUIT_B = button((225,0,0), 560, 310, 160, 80, "Quit Game")
START_B = button((0,225,0), 560, 90, 160, 80, "Start Game")
INFO_B = button((225,225,0), 560, 200, 160, 80, "How To Play")

GX = 1280
BG = pygame.transform.scale(pygame.image.load('BG.png'),(640,480))
FONT = pygame.font.Font("cour.ttf", 31)
WALK =[pygame.image.load("w1.png"),pygame.image.load("w1.png"),pygame.image.load("w2.png"),pygame.image.load("w2.png"),pygame.image.load("w3.png"),pygame.image.load("w3.png")]
HEART = pygame.image.load("heart.png")
CLOCK = pygame.time.Clock()
BG_LOC = [0,640,1280]
SCREEN = pygame.display.set_mode((1280, 480))
GOOMBA = pygame.transform.scale(pygame.image.load("g.png"), (80,80))
QUESTIONS = [("N2O","dinitrogen monoxide"),("S2F10","disulfur decafluoride"),("CF","carbon monofluoride"),("Si3N4","trisilicon tetranitride"),("SbCl5","antimony pentachloride"),("P2O3","diphosphorus trioxide"),("Br2","bromine gas"),("CO2","carbon dioxide"),("Cl2O8","dichlorine octoxide"),("Cl2","chlorine gas"),("CF4","carbon tetrafluoride"),("As4O6","tetrarsenic hexoxide"),("H2","hydrogen gas"),("CO","carbon monoxide"),("N2","nitrogen gas"),("PBr3","phosphorus tribromide"),("PCl3","phosphorus trichloride"),("Si2H3","disilicon trihydride"),("SO3","sulfur trioxide"),("PI5","phosphorus pentaiodide"),("NH3","ammonia gas"),("CO3","carbon trioxide"),("NF3","nitrogen trifluoride"),("SiCl4","silicon tetrachloride"),("O2","oxygen gas"),("O3","ozone gas"),("NO","nitrogen monoxide"),("PBr5","phosphorus pentabromide"),("PI3","phosphorus triiodide"),("Cl2O","dichlorine monoxide")]

y = 225
win = True
life = 3
text = ""
done = False
isjump= False
started = False    
quitted = False
walkcount = 0
jumpcount = 25

while not started:
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        FONT1 = pygame.font.Font("cour.ttf", 16)
        if event.type == pygame.QUIT:
            started = True
            quitted = True
        if event.type == pygame.MOUSEBUTTONDOWN and START_B.isOver(pos):
            started = True
        if event.type == pygame.MOUSEBUTTONDOWN and QUIT_B.isOver(pos):
            started = True
            quitted = True
        if event.type == pygame.MOUSEBUTTONDOWN and INFO_B.isOver(pos):
            info = True
            info_T = FONT1.render("Type the formula of the chemical on top of the goomba to avoid them", True, (0,225,0), (0,0,0))
            info_R = info_T.get_rect()
            info_R.center = (1280/2,480/2)
            while info:
                pos = pygame.mouse.get_pos()
                SCREEN.blit(BG, (BG_LOC[0],0))
                SCREEN.blit(BG, (BG_LOC[1],0))
                SCREEN.blit(BG, (BG_LOC[2],0))
                SCREEN.blit(info_T,info_R)
                BACK_B.draw(SCREEN)
                if BG_LOC[0] == -640:
                    BG_LOC[0] = 0
                if BG_LOC[1] == 0:
                    BG_LOC[1] = 640
                if BG_LOC[2] == 640:
                    BG_LOC[2] = 1280
                BG_LOC[0] -= 5
                BG_LOC[1] -= 5
                BG_LOC[2] -= 5
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        info = False
                        started = True
                        quitted = True
                    if event.type == pygame.MOUSEBUTTONDOWN and BACK_B.isOver(pos):
                        info = False
                CLOCK.tick(15)
            break            
    SCREEN.blit(BG, (BG_LOC[0],0))
    SCREEN.blit(BG, (BG_LOC[1],0))
    SCREEN.blit(BG, (BG_LOC[2],0))
    START_B.draw(SCREEN)
    INFO_B.draw(SCREEN)
    QUIT_B.draw(SCREEN)
    if BG_LOC[0] == -640:
        BG_LOC[0] = 0
    if BG_LOC[1] == 0:
        BG_LOC[1] = 640
    if BG_LOC[2] == 640:
        BG_LOC[2] = 1280
    BG_LOC[0] -= 5
    BG_LOC[1] -= 5
    BG_LOC[2] -= 5            
    pygame.display.flip()
    CLOCK.tick(15)

if not quitted:

    for question in QUESTIONS:
        chem = FONT.render(question[1], True, (0,0,0))
        done = False
        quitted = False
        walkcount = 0
        BG_LOC = [0,640,1280]
        GX = 1280
        while not done:
            pos = pygame.mouse.get_pos()
            answer = FONT.render(text, True, (0,0,0))
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    quitted = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        paused = True
                        while paused:
                            pos = pygame.mouse.get_pos()
                            START_B.draw(SCREEN)
                            QUIT_B.draw(SCREEN)
                            pygame.display.flip()
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN and START_B.isOver(pos):
                                    paused = False    
                                if event.type == pygame.MOUSEBUTTONDOWN and QUIT_B.isOver(pos):
                                    paused = False
                                    done = True
                                    quitted = True
                            CLOCK.tick(15)
                        break                        
                    if event.key == pygame.K_RETURN:
                        
                        if text == question[0]:
                            done = True
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
            answer = FONT.render(text, True, (0,0,0))
            
            
            if BG_LOC[0] == -640:
                BG_LOC[0] = 0
            if BG_LOC[1] == 0:
                BG_LOC[1] = 640
            if BG_LOC[2] == 640:
                BG_LOC[2] = 1280
            if GX == 0:
                GX = 1280
            walkcount +=1
            if walkcount == 6:
                walkcount = 0
            BG_LOC[0] -= 5
            BG_LOC[1] -= 5
            BG_LOC[2] -= 5
            GX -= 5

            if GX == 90:
                done = True
                life -= 1

            SCREEN.blit(BG, (BG_LOC[0],0))
            SCREEN.blit(BG, (BG_LOC[1],0))
            SCREEN.blit(BG, (BG_LOC[2],0))
            SCREEN.blit(WALK[walkcount], (0,y)) 
            SCREEN.blit(GOOMBA, (GX,315))
            SCREEN.blit(chem, (GX-20,300))
            SCREEN.blit(answer, (10,430))
            for i in range(0,life):
                SCREEN.blit(HEART, (1170-i*90,-20))
            pygame.display.flip()
            CLOCK.tick(15)
            
            if life == 0:
                done =True
                win = False

        if quitted:
            break
    
    if not quitted:
        FONT1 = pygame.font.Font("cour.ttf", 30)
        if win:
            info_T = FONT1.render("YOU WIN!!!", True, (0,225,0), (225,225,225))
        else:
            info_T = FONT1.render("YOU LOSE :'(", True, (0,225,0), (225,225,225))
        info_R = info_T.get_rect()
        info_R.center = (1280/2,480/2)
        for i in range(0,6):
            SCREEN.blit(info_T,info_R)
            CLOCK.tick(15)
            pygame.display.update()
pygame.quit()