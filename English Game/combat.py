import os
import time
import keyboard
from random import seed
from random import randint
clear = lambda: os.system('cls')
clear()

options = [">", " ", " "]
weaponds = [">", " "]
items = [">", " "]
#             health stab gamage  slash damage  stab cahnce slash chance sml health lrg health option+selec weapon_selec item_selec  enemie_1 enemie_2  fight_type   menu_type
INT_VALUES = [90,     35,          25,            20,        15,           5,         5,          0,          0,               0,             100,        100,     0,           0]
STR_VALUES = ["0","0","0","0","0","0","0"]

flee_chance = randint(10, 20)

FIGHT_1V1 = "MACBETH  ENEMIE {}\n o           o   \n/|\|       |/|\  \n/ \         / \  \n                 \n".format(INT_VALUES[10])

FIGHT_1V2 = "         ENEMIE {}\n             o   \n           |/|\  \nMACBETH     / \  \n o               \n/|\|     ENEMIE {}\/ \          o   \n           |/|\  \n            / \  \n".format(INT_VALUES[10],INT_VALUES[11])

FIGHT_2V1 = "MACBETH          \n o               \n/|\|             \n/ \      ENEMIE {}\"BANQUO       o   \n o         |/|\  \n/|\|        / \  \n/ \              \n".format(INT_VALUES[10])

FIGHT_2V2 = "MACBETH  ENEMIE {}\n o           o   \n/|\|       |/|\  \n/ \         / \  \nBANQUO   ENEMIE {}\n o           o   \n/|\|       |/|\  \n/ \         / \  \n".format(INT_VALUES[10],INT_VALUES[11])

MENU = "=============================\n|            |              |\n|{}FIGHT      | HEALTH =  {} |\n|            |              |\n|{}ITEM       |              |\n|            |              |\n|{}FLEE       |              |\n|            |              |\n=============================\n".format(options[0],STR_VALUES[0],options[1],options[2])

FIGHT_MENU = "=============================\n|            |              |\n| FIGHT      |{}STAB         |\n|            | MISS CHANCE =|\n|            | {}           |\n|            | DAMAGE = {}  |\n|            |{}SLASH        |\n|            | MISS CHANCE =|\n|            | {}           |\n|            | DAMAGE = {}  |\n|            |              |\n=============================\n".format(weaponds[0],STR_VALUES[1],STR_VALUES[2],weaponds[1],STR_VALUES[3],STR_VALUES[4])

ITEM_MENU = "=============================\n|            |              |\n| ITEMS      |{}SMALL HEALTH |\n|            | = {}         |\n|            |{}LARGE HEALTH |\n|            | = {}         |\n|            |              |\n=============================\n".format(items[0],STR_VALUES[5],items[1],STR_VALUES[6])

FLEE_MENU = "=============================\n|            |              |\n|>FLEE       | FLEE CAHNCE =|\n|            |              |\n|            | {}           |\n|            |              |\n|            |              |\n=============================\n".format(flee_chance)





def drawFight(fight_type, menu_type):

	clear()
	print(INT_VALUES)
	if fight_type == 0:

		if menu_type == 0:

			print(FIGHT_1V1)
			print(MENU)

		elif menu_type == 1:

			print(FIGHT_1V1)
			print(FIGHT_MENU)

		elif menu_type == 2:

			print(FIGHT_1V1)
			print(ITEM_MENU)

		elif menu_type == 3:

			print(FIGHT_1V1)
			print(FLEE_MENU)

	elif fight_type == 1:

		if menu_type == 0:

			print(FIGHT_1V2)
			print(MENU)

		elif menu_type == 1:

			print(FIGHT_1V2)
			print(FIGHT_MENU)

		elif menu_type == 2:

			print(FIGHT_1V2)
			print(ITEM_MENU)

		elif menu_type == 3:

			print(FIGHT_1V2)
			print(FLEE_MENU)

	elif fight_type == 2:

		if menu_type == 0:

			print(FIGHT_2V1)
			print(MENU)

		elif menu_type == 1:

			print(FIGHT_2V1)
			print(FIGHT_MENU)

		elif menu_type == 2:

			print(FIGHT_2V1)
			print(ITEM_MENU)

		elif menu_type == 3:

			print(FIGHT_2V1)
			print(FLEE_MENU)

	elif fight_type == 3:

		if menu_type == 0:

			print(FIGHT_2V2)
			print(MENU)

		elif menu_type == 1:

			print(FIGHT_2V2)
			print(FIGHT_MENU)

		elif menu_type == 2:

			print(FIGHT_2V2)
			print(ITEM_MENU)

		elif menu_type == 3:

			print(FIGHT_2V2)
			print(FLEE_MENU)
	time.sleep(0.1)

def setPointer():
	global options, weaponds, items
	if INT_VALUES[7] == 0:
		options = [">", " ", " "]
	elif INT_VALUES[7] == 1:
		options = [" ", ">", " "]
	elif INT_VALUES[7] == 2:
		options = [" ", " ", ">"]

	if INT_VALUES[8] == 0:
		weaponds = [">", " "]
	elif INT_VALUES[8] == 1:
		weaponds = [" ", ">"]

	if INT_VALUES[9] == 0:
		items = [">", " "]
	elif INT_VALUES[9] == 1:
		items = [" ", ">"]
	drawFight(INT_VALUES[12], INT_VALUES[13])
fleed = False
fighting = False
INT_VALUES[10] = 100
while True:
	if INT_VALUES[10] <= 0 or INT_VALUES[0] <= 0:
		break

	for i in range(0,len(INT_VALUES)-7):

		if INT_VALUES[i] >=100:

			STR_VALUES[i] = "\b100"
		elif 9 < INT_VALUES[i] < 100:

			STR_VALUES[i] = "{}".format(INT_VALUES[i])
		elif INT_VALUES[i] < 10:

			STR_VALUES[i] = " {}".format(INT_VALUES[i])


	setPointer()	

	FIGHT_1V1 = "MACBETH  ENEMIE {}\n o           o   \n/|\|       |/|\  \n/ \         / \  \n                 \n".format(INT_VALUES[10])

	MENU = "=============================\n|            |              |\n|{}FIGHT      | HEALTH =  {} |\n|            |              |\n|{}ITEM       |              |\n|            |              |\n|{}FLEE       |              |\n|            |              |\n=============================\n".format(options[0],STR_VALUES[0],options[1],options[2])

	FIGHT_MENU = "=============================\n|            |              |\n| FIGHT      |{}STAB         |\n|            | MISS CHANCE =|\n|            | {}           |\n|            | DAMAGE = {}  |\n|            |{}SLASH        |\n|            | MISS CHANCE =|\n|            | {}           |\n|            | DAMAGE = {}  |\n|            |              |\n=============================\n".format(weaponds[0],STR_VALUES[1],STR_VALUES[2],weaponds[1],STR_VALUES[3],STR_VALUES[4])

	ITEM_MENU = "=============================\n|            |              |\n| ITEMS      |{}SMALL HEALTH |\n|            | = {}         |\n|            |{}LARGE HEALTH |\n|            | = {}         |\n|            |              |\n=============================\n".format(items[0],STR_VALUES[5],items[1],STR_VALUES[6])


	if keyboard.is_pressed("down"):
		
		if INT_VALUES[13] == 0:

			INT_VALUES[7] += 1
			INT_VALUES[13] = 0
			if INT_VALUES[7] >= 3:
				INT_VALUES[7] = 0
				INT_VALUES[13] = 0

		elif INT_VALUES[13] == 1:

			INT_VALUES[8] += 1
			if INT_VALUES[8] >= 2:
				INT_VALUES[8] = 0

		elif INT_VALUES[13] == 2:

			INT_VALUES[9] += 1
			if INT_VALUES[9] >= 2:
				INT_VALUES[9] = 0
		
		setPointer()	
	elif keyboard.is_pressed("up"):
		
		if INT_VALUES[13] == 0:

			INT_VALUES[7] -= 1
			INT_VALUES[13] = 0
			if INT_VALUES[7] == -1:
				INT_VALUES[7] = 2
				INT_VALUES[13] = 0

		elif INT_VALUES[13] == 1:

			INT_VALUES[8] -= 1
			if INT_VALUES[8] == -1:
				INT_VALUES[8] = 1

		elif INT_VALUES[13] == 2:

			INT_VALUES[9] -= 1
			if INT_VALUES[9] == -1:
				INT_VALUES[9] = 1
		setPointer()
	elif keyboard.is_pressed("enter"):
		
		if INT_VALUES[13] == 0:
			if INT_VALUES[7] == 0:

				INT_VALUES[13] = 1
			elif INT_VALUES[7] == 1:

				INT_VALUES[13] = 2
			elif INT_VALUES[7] == 2:

				INT_VALUES[13] = 3
		elif INT_VALUES[13] == 1:
			if INT_VALUES[8] == 0:
				if randint(0,100) > 20:
					INT_VALUES[10] -= 35
					INT_VALUES[13] = 0
				else:
					INT_VALUES[0] -= 15
					INT_VALUES[13] = 0
			elif INT_VALUES[8] == 1:
				if randint(0,100) > 15:
					
					INT_VALUES[10] -= 25
					INT_VALUES[13] = 0
				else:
					INT_VALUES[0] -= 15
					INT_VALUES[13] = 0
		elif INT_VALUES[13] == 2:

			if INT_VALUES[9] == 0:
				if INT_VALUES[5] >0 and INT_VALUES[0] < 100:
					INT_VALUES[0] += 15
					INT_VALUES[5] -= 1
				elif INT_VALUES[6] >0 and INT_VALUES[0] < 100:
					INT_VALUES[0] += 25
					INT_VALUES[5] -= 1
		elif INT_VALUES[13] == 3:
			if not fleed:
				fleed = True
				if randint(0,100) <= 0:
					break
			else:
				print("You have already tried that")



		setPointer()
	elif keyboard.is_pressed("escape"):

		INT_VALUES[13] = 0
		drawFight(INT_VALUES[12],INT_VALUES[13])


		