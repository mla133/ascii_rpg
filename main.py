import os

run = True
menu = True
play = False
rules = False
key = False

HP = 50
HPMAX = HP
ATK = 3
pot = 1
elix = 0
gold = 0
x = 0
y = 0

        # x=0       x=1         x=2         x=3         x=4         x=5         x=6
map = [ ["plains",	"plains",	"plains",	"plains",	"forest",	"mountain",	 "cave"],	    #y=0
        ["forest",	"forest",	"forest",	"forest",	"forest",	"hills",	"mountain"],    #y=1
        ["forest",	"fields",	"bridge",	"plains",	"hills",	"forest",	"hills"],	    #y=2
        ["plains",	"shop",	    "town",	    "major",	"plains",	"hills",	"mountain"],	#y=3
        ["plains",	"fields",	"fields",	"plains",	"hills",	"mountain",	"mountain"]]    #y=4

y_len = len(map)-1
x_len = len(map[0])-1
current_tile = map[y][x]

biom = {
        "plains": {
            "t": "PLAINS",
            "e": True},
         "woods": {
            "t": "WOODS",
            "e": True},
        "fields": {
            "t": "FIELDS",
            "e": False},
        "bridge": {
            "t": "BRIDGE",
            "e": True},
        "town": {
            "t": "TOWN",
            "e": False},
        "shop": {
            "t": "SHOP",
             "e": False},
        "major": {
            "t": "MAJOR",
            "e": False},
        "cave": {
            "t": "CAVE",
            "e": False},
        "mountain": {
            "t": "MOUNTAIN",
            "e": True},
        "hills":    {
            "t": "HILLS",
            "e": True},
        "forest":   {
            "t": "FOREST",
            "e": True}
        }
        


def save():
    list = [ name, str(HP), str(ATK), str(pot), str(elix), str(gold), str(x), str(y), str(key) ]

    f = open("load.txt", "w")

    for item in list:
        f.write(item + "\n")

    f.close()

def load():
    try:
        f = open("load.txt", "r")
        load_list = f.readlines()
        if len(load_list) == 9:
            name = load_list[0][:-1]
            HP   = int(load_list[1][:-1])
            ATK  = int(load_list[2][:-1])
            pot  = int(load_list[3][:-1])
            elix = int(load_list[4][:-1])
            gold = int(load_list[5][:-1])
            x    = int(load_list[6][:-1])
            y    = int(load_list[7][:-1])
            key  = bool(load_list[8][:-1])
        else:
            print("Corrupt save file!")
            input("> ")
    except OSError:
        print("No loadable save files!")
        input("> ")

    f.close()


def clear():
    os.system("clear")

def draw():
    print("Xx---------------------------xX")

while run:
    while menu:
        clear()
        draw()
        print("1.  NEW GAME")
        print("2.  LOAD GAME")
        print("3.  RULES")
        print("4.  QUIT GAME")
        draw()

        if rules:
            print("I'm the creator of this game and these are the rules.")
            rules = False
            choice = ""
            input("> ")
        else:
            choice = input("# ")
        
        if choice == "1":
            clear()
            name = input("What is your name, hero? ")
            menu = False
            play = True
        elif choice == "2":
            load()
            clear()
            print("Welcome back, " + name + "!")
            input("# ")
            play = True
        if choice == "3":
            rules = True
        if choice == "4":
            quit() 
    
    while play:
        save()  #autosave
        clear()
        draw()
        print("LOCATION: " + biom[map[y][x]]["t"])
        draw()
        print("NAME: " + name)
        print("HP: " + str(HP) + "/" + str(HPMAX))
        print("ATK: " + str(ATK))
        print("POTIONS: " + str(pot))
        print("ELIXIRS: " + str(elix))
        print("GOLD: " + str(gold))
        print("COORDS: ", x, y)
        draw()
        print("0 - SAVE AND QUIT")
        if y > 0:
            print("1 - NORTH")
        if x < x_len:
            print("2 - EAST")
        if y < y_len:
            print("3 - SOUTH")
        if x > 0:
            print("4 - WEST")
        draw()

        dest = input("# ")

        if dest == "0":
            play = False
            menu = True
            save()
        elif dest == "1":
            if y > 0:
                y -= 1
        elif dest == "2":
            if x < x_len:
                x += 1
        elif dest == "3":
            if y < y_len:
                y += 1
        elif dest == "4":
            if x > 0:
                x -= 1
