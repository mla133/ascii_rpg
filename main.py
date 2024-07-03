import os

run = True
menu = True
play = False
rules = False
HP = 50
ATK = 3

def save():
    list = [ name, str(HP), str(ATK) ]

    f = open("load.txt", "w")

    for item in list:
        f.write(item + "\n")

    f.close()

def clear():
    os.system("clear")

while run:
    while menu:
        clear()
        print("1.  NEW GAME")
        print("2.  LOAD GAME")
        print("3.  RULES")
        print("4.  QUIT GAME")

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
            f = open("load.txt", "r")
            load_list = f.readlines()
            name = load_list[0][:-1]
            HP   = load_list[1][:-1]
            ATK  = load_list[2][:-1]
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

        dest = input("# ")

        if dest == "0":
            play = False
            menu = True
            save()
