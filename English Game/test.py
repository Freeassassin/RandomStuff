FIGHT_1V1 = [
"MACBETH          ",
" o           o   ",
"/|\|       |/|\  ",
"/ \         / \  ",
"                 "]
FIGHT_1V2 = [
"         ENEMIE 1",
"             o   ",
"           |/|\  ",
"MACBETH     / \  ",
" o               ",
"/|\|     ENEMIE 2",
"/ \          o   ",
"           |/|\  ",
"            / \  "]
FIGHT_2V1 = [
"MACBETH          ",
" o               ",
"/|\|             ",
"/ \      ENEMIE 1",
"BANQUO       o   ",
" o         |/|\  ",
"/|\|        / \  ",
"/ \              "]
FIGHT_2V2 = [
"MACBETH  ENEMIE 1",
" o           o   ",
"/|\|       |/|\  ",
"/ \         / \  ",
"BANQUO   ENEMIE 2",
" o           o   ",
"/|\|       |/|\  ",
"/ \         / \  "]

MENU = [
"=============================",
"|            |              |",
"| FIGHT      | HEALTH = %s |",
"|            |              |",
"| ITEM       |              |",
"|            |              |",
"| FLEE       |              |",
"|            |              |",
"============================="]
FIGHT_MENU = [
"=============================",
"|            |              |",
"| FIGHT      | STAB         |",
"|            | MISS CHANCE =|",
"|            | %s           |",
"|            | DAMAGE = %s  |",
"|            | SLASH        |",
"|            | MISS CHANCE =|",
"|            | %s  
          |",
"|            | DAMAGE = %s  |",
"|            |              |",
"============================="]
ITEM_MENU = [
"=============================",
"|            |              |",
"| ITEMS      | SMALL HEALTH |",
"|            | = %s          |",
"|            | LARGE HEALTH |",
"|            | = %s          |",
"|            |              |",
"============================="]
FLEE_MENU = [
"=============================",
"|            |              |",
"| FLEE       | FLEE CAHNCE =|",
"|            |              |",
"|            | %s%           |", 
"|            |              |",
"|            |              |",
"============================="]
name = 100
for i in FIGHT_MENU:
    if "%s" in i:
        print(i % name)
    else:
        print(i)