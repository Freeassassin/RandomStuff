import pygame
pygame.init()
BG = pygame.transform.scale(pygame.image.load('BG.png'),(640,480))
BG1 = pygame.transform.scale(pygame.image.load('BG.png'),(640,480))
WALK =[pygame.image.load("w1.png"),pygame.image.load("w1.png"),pygame.image.load("w2.png"),pygame.image.load("w2.png"),pygame.image.load("w3.png"),pygame.image.load("w3.png")]
GOOMBA = pygame.transform.scale(pygame.image.load("g.png"), (80,80))
i = 0
BG_LOC = [0,640]
GX = 640
screen = pygame.display.set_mode((640, 480))
font = pygame.font.Font("cour.ttf", 32)
input_box = pygame.Rect(100, 100, 140, 32)
clock = pygame.time.Clock()
text = ""
question = ""
done = False	
chem = font.render(question, True, (0,0,0))
questions = {"LiBr":"lithium bromide","KC2H3O2":"","CrCrO4":"","Hg2(HCO3)2":"",
			 "Pb(C2H3O2)2":"","Pb3P2":"","Li2SO4":"","Hg2SO3":"","MnPO4":"",
			 "Na2O":"","KClO4":"","Fe3(PO4)2":"","Sn(HCO3)4":"","HgCO3":"",
			 "Cr(ClO2)2":"","Mn2(Cr2O7)3":"","PbSO4":"","Fe2(C2O4)3":"",
			 "Cu(NO3)2":"","Hg2Cl2":"","CrSO3":"","Sn(NO2)4":"","KH2PO4":"",
			 "Mn3P2":"","Fe(NO3)2":"","CaCO3":"","Ag2SO4":"","Cr2(SO3)3":"",
			 "CaO":"","Mg(C2H3O2)2":"","CoCl3":""}
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
	answer = font.render(text, True, (0,0,0))
	
	if BG_LOC[0] <= -640:
		BG_LOC[0] = 0
	if BG_LOC[1] == 0:
		BG_LOC[1] = 640
	if GX == 0:
		GX = 640
	BG_LOC[0] -= 5
	BG_LOC[1] -= 5
	GX -= 5
	screen.blit(BG, (BG_LOC[0],0))
	screen.blit(BG1, (BG_LOC[1],0))
	screen.blit(WALK[i], (0,225)) 
	screen.blit(GOOMBA, (GX,315))
	screen.blit(chem, (GX-27,300))
	screen.blit(answer, (10,430))
	pygame.display.flip()
	clock.tick(15)
	
	i +=1
	if i == 6:
		i = 0
pygame.quit()