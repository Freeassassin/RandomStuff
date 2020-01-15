import os
import time
import keyboard
clear = lambda: os.system('cls')
clear()
TITLE = [[
"W     W EEEE  L     CCC  OOO  M   M EEEE ",
"W     W E     L    C    O   O MM MM E    ",
"W  W  W EEE   L    C    O   O M M M EEE  ",
" W W W  E     L    C    O   O M   M E    ",
"  W W   EEEE  LLLL  CCC  OOO  M   M EEEE "
],
[
"		TTTTTT  OOO  ",
"		  TT   O   O ",
"		  TT   O   O ",
"		  TT   O   O ",
"		  TT    OOO  "
],
[
"M   M  AA   CCC BBBB  EEEE TTTTTT H  H ",
"MM MM A  A C    B   B E      TT   H  H ",
"M M M AAAA C    BBBB  EEE    TT   HHHH ",
"M   M A  A C    B   B E      TT   H  H ",
"M   M A  A  CCC BBBB  EEEE   TT   H  H " ]
]

for i in TITLE:
	for j in i:
		print(j)
		time.sleep(0.125)

input("Press Enter To Continue>")


selection = 0
LEVELS = ["		ACT I, SCENE III\n","		ACT I, SCENE IV\n","		ACT II, SCENE I\n","		ACT II, SCENE II\n","		ACT III, SCENE II\n","		ACT III, SCENE IV\n","		ACT IV, SCENE I\n","		ACT V, SCENE I\n","		ACT V, SCENE V\n","		ACT V, SCENE VI\n","		ONLY IMPORTANT QUOTES\n"]
while True:
	clear()
	print("SELECT A LEVEL")
	for i in range(0,len(LEVELS)):
		if i == selection:
			print(">",LEVELS[i])
		else:
			print(LEVELS[i])		
	if keyboard.is_pressed("escape"):
		break
	elif keyboard.is_pressed("down"):
		selection += 1
	elif keyboard.is_pressed("up"):
		selection -= 1

	if selection ==12:
		selection = 0
	elif selection == -1:
		selection = 11 
	time.sleep(0.1)


"""
f=open("guru99.txt", "r")
#if f.mode == 'r': 
 #   contents =f.read()
  #  print( contents)
 #or, readlines reads the individual line into a list
fl =f.readlines()
print ()
"""