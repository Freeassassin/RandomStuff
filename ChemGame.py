import pygame
pygame.init()
BG = pygame.transform.scale(pygame.image.load('BG.png'),(640,480))
WALK =[pygame.image.load("w1.png"),pygame.image.load("w1.png"),pygame.image.load("w2.png"),pygame.image.load("w2.png"),pygame.image.load("w3.png"),pygame.image.load("w3.png")]
GOOMBA = pygame.transform.scale(pygame.image.load("g.png"), (80,80))
walkcount = 0
BG_LOC = [0,640,1280]
GX = 1280
screen = pygame.display.set_mode((1280, 480))
screen1 = pygame.display.set_mode((1280, 480))
font = pygame.font.Font("cour.ttf", 32)
input_box = pygame.Rect(100, 100, 140, 32)
clock = pygame.time.Clock()
text = ""
question = "lithium bromide"
done = False
started = False	
chem = font.render(question, True, (0,0,0))
y = 225
jumpcount = 25
isjump= False
questions = [
("N2O","dinitrogen monoxide"),("S2F10","disulfur decafluoride"),
("CF","carbon monofluoride"),("Si3N4","trisilicon tetranitride"),
("SbCl5","antimony pentachloride"),("P2O3","diphosphorus trioxide"),
("Br2","bromine gas"),("CO2","carbon dioxide"),("Cl2O8","dichlorine octoxide"),
("Cl2","chlorine gas"),("CF4","carbon tetrafluoride"),("As4O6","tetrarsenic hexoxide"),
("H2","hydrogen gas"),("CO","carbon monoxide"),("N2","nitrogen gas"),
("PBr3","phosphorus tribromide"),("PCl3","phosphorus trichloride"),
("Si2H3","disilicon trihydride"),("SO3","sulfur trioxide"),
("PI5","phosphorus pentaiodide"),("NH3","ammonia gas"),
("CO3","carbon trioxide"),("NF3","nitrogen trifluoride"),
("SiCl4","silicon tetrachloride"),("O2","oxygen gas"),
("O3","ozone gas"),("NO","nitrogen monoxide"),
("PBr5","phosphorus pentabromide"),("PI3","phosphorus triiodide"),
("Cl2O","dichlorine monoxide")]

class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('cour.ttf', 40)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

start_button = button((225,225,0), 1280/2, 90, 160, 80, "Start Game")
info_button = button((0,225,0), 1280/2, 90, 160, 80, "How To Play")

while not started:
	pos = pygame.mouse.get_pos()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			started = True
		if event.type == pygame.MOUSEBUTTONDOWN and start_button.isOver(pos):
			started = True

	screen.blit(BG, (BG_LOC[0],0))
	screen.blit(BG, (BG_LOC[1],0))
	screen.blit(BG, (BG_LOC[2],0))
	start_button.draw(screen)
	screen.blit
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
	clock.tick(15)
 
for i in questions:
	chem = font.render(i[1], True, (0,0,0))
	done = False
	while not done:
		answer = font.render(text, True, (0,0,0))
		

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					paused = True
					while paused:
						pass
				if event.key == pygame.K_RETURN:
					
					if text == i[0]:
						isjump = True
						done = True
					text = ''
				elif event.key == pygame.K_BACKSPACE:
					text = text[:-1]
				else:
					text += event.unicode
		answer = font.render(text, True, (0,0,0))
		
		
		if BG_LOC[0] == -640:
			BG_LOC[0] = 0
		if BG_LOC[1] == 0:
			BG_LOC[1] = 640
		if BG_LOC[2] == 640:
			BG_LOC[2] = 1280
		if GX == 0:
			GX = 1280
		BG_LOC[0] -= 5
		BG_LOC[1] -= 5
		BG_LOC[2] -= 5
		GX -= 5
		screen.blit(BG, (BG_LOC[0],0))
		screen.blit(BG, (BG_LOC[1],0))
		screen.blit(BG, (BG_LOC[2],0))
		if isjump:
			if jumpcount >= -25:

				y -= (jumpcount * abs(jumpcount)) * 0.05
				jumpcount -= 1
			else:
				jumpcount = 25
				isjump = False

		screen.blit(WALK[walkcount], (0,y)) 
		screen.blit(GOOMBA, (GX,315))
		screen.blit(chem, (GX-20,300))
		screen.blit(answer, (10,430))
		pygame.display.flip()
		clock.tick(15)
		
		walkcount +=1
		if walkcount == 6:
			walkcount = 0
pygame.quit()
