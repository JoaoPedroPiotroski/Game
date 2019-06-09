import sys 
import os
import random 
import math
import cmd
import textwrap
import time

#Character Class#

class player:
    def __init__(self):
        self.name: ''
        self.job: ''
        self.hp=0
        self.mp=0
        self.status_effects = []
        self.location = 'b2'
        self.gameover = False
myPlayer = player()

#Title Screen#



def title_screen_selections():
    option=input("> ")
    if option.lower() == ('play'):
        setup_game()
    elif option.lower() == ('help'):
        help_menu()
    elif option.lower() == ('quit'):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please type a valid option:")
        option=input("> ")
        if option.lower() == ('play'):
            setup_game()
        elif option.lower() == ('help'):
            help_menu()
        elif option.lower() == ('quit'):
            sys.exit()   
def title_screen():
    os.system('cls')
    print("############################################")
    print("#      Welcome to the python text RPG      #")
    print("#                 Play                     #")
    print("#                 Load                     #")
    print("#                 Help                     #")
    print("#                 Exit                     #")
    print("############################################")
    title_screen_selections()
def help_menu():
    print("############################################")
    print("#      Welcome to the python text RPG      #")
    print("#    -Use up, down, left, right to move    #")
    print("#      -Type your commands to do them      #")
    print("#     -Use 'look' to inspect something     #")
    print("############################################")
    title_screen()

#MAP#
'''   #player starts at b2
-------------------------
| a1  | a2  | a3  | a4  |
-------------------------
| b1  | b2  | b3  | b4  |
-------------------------
| c1  | c2  | c3  | c4  |
-------------------------
| d1  | d2  | d3  | d4  |
-------------------------
'''

ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {
    'a1': False,
    'a2': False,
    'a3': False,
    'a4': False,
    'b1': False,
    'b2': False,
    'b3': False,
    'b4': False,
    'c1': False,
    'c2': False,
    'c3': False,
    'c4': False,
    'd1': False,
    'd2': False,
    'd3': False,
    'd4': False,
}

zonemap = {
    'a1': {
        ZONENAME: "Town Market",
        DESCRIPTION: 'The market where merchants come from far and wide to trade',
        EXAMINATION: 'there are many shops here where you can trade',
        SOLVED: False,
        UP: '',
        DOWN: 'b1',
        LEFT: '',
        RIGHT: 'a2',
    },
    'a2': {
        ZONENAME: "Town Entrance",
        DESCRIPTION: 'A big arch, leading to the city near your home',
        EXAMINATION: 'You mostly see lots of homes here',
        SOLVED: False,
        UP: '',
        DOWN: 'b2',
        LEFT: 'a1',
        RIGHT: 'a3',
    },
    'a3': {
        ZONENAME: "Town Hall",
        DESCRIPTION: 'The Town Hall, not much about it',
        EXAMINATION: "You can't find much to see besides the hall itself and some noble housing",
        SOLVED: False,
        UP: '',
        DOWN: 'b3',
        LEFT: 'a2',
        RIGHT: 'a4',
    },
    'a4': {
        ZONENAME: "Town Square",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up' 'north',
        DOWN: 'down' 'south',
        LEFT: 'left' 'west',
        RIGHT: 'right' 'east',
    },
    'b1': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up' 'north',
        DOWN: 'down' 'south',
        LEFT: 'left' 'west',
        RIGHT: 'right' 'east',
    },
    'b2': {
        ZONENAME: "Home",
        DESCRIPTION: 'This is your home',
        EXAMINATION: 'Your home looks the same - nothing has changed',
        SOLVED: False,
        UP: 'a2',
        DOWN: 'c2',
        LEFT: 'b1',
        RIGHT: 'b3',
    },
    'b3': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up' 'north',
        DOWN: 'down' 'south',
        LEFT: 'left' 'west',
        RIGHT: 'right' 'east',
    },
    'b4': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up' 'north',
        DOWN: 'down' 'south',
        LEFT: 'left' 'west',
        RIGHT: 'right' 'east',
    },
    'c1': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up' 'north',
        DOWN: 'down' 'south',
        LEFT: 'left' 'west',
        RIGHT: 'right' 'east',
    },
    'c2': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up' 'north',
        DOWN: 'down' 'south',
        LEFT: 'left' 'west',
        RIGHT: 'right' 'east',
    },
    'c3': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up' 'north',
        DOWN: 'down' 'south',
        LEFT: 'left' 'west',
        RIGHT: 'right' 'east',
    },
    'c4': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up' 'north',
        DOWN: 'down' 'south',
        LEFT: 'left' 'west',
        RIGHT: 'right' 'east',
    },
    'd1': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up' 'north',
        DOWN: 'down' 'south',
        LEFT: 'left' 'west',
        RIGHT: 'right' 'east',
    },
    'd2': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up' 'north',
        DOWN: 'down' 'south',
        LEFT: 'left' 'west',
        RIGHT: 'right' 'east',
    },
    'd3': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up' 'north',
        DOWN: 'down' 'south',
        LEFT: 'left' 'west',
        RIGHT: 'right' 'east',
    },
    'd4': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up' 'north',
        DOWN: 'down' 'south',
        LEFT: 'left' 'west',
        RIGHT: 'right' 'east',
    },
}

#Game Interactivity#
def print_location():
    print_location_name = zonemap[myPlayer.location][ZONENAME].upper()
    print('\n' '\n')
    print(print_location_name)
    print('# ' + zonemap[myPlayer.location][DESCRIPTION] + ' #')
    print('\n' '\n')

def prompt():
    print("\n" + "=====================================")
    print("What would you like to do?")
    action = input("> ")
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look']
    while action.lower() not in acceptable_actions:
        print("Unknown action, try again.\n")
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
        player_examine(action.lower())

def player_move(myAction):
    ask = "Where would you like to move to?\n"
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = zonemap[myPlayer.location][UP]
        movement_handler(destination)
    elif dest in ['left', 'west']:
        destination = zonemap[myPlayer.location][LEFT]
        movement_handler(destination)
    elif dest in ['east', 'right']:
        destination = zonemap[myPlayer.location][RIGHT]
        movement_handler(destination)
    elif dest in ['south', 'down']:
        destination = zonemap[myPlayer.location][DOWN]
        movement_handler(destination)

def movement_handler(destination):
    myPlayer.location = destination
    print("\n" + "You have moved to the " + zonemap[myPlayer.location][ZONENAME] + ".")
    print_location()

def player_examine(action):
    print(zonemap[myPlayer.location][EXAMINATION])

#Game Functionality#
#Game Functionality#

def main_game_loop():
    while myPlayer.gameover is False:
        prompt()

def setup_game():
    os.system('cls')

    #Name Registration#

    question1 = "Hello, what's your name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    myPlayer.name = player_name

    #Class Selection#

    question2 = "Hello, what role do you want to play?\n"
    question2added = "(You can play as a warrior, priest, or mage)\n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in question2added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_job = input("> ")
    valid_jobs = ['warrior', 'mage', 'priest']
    if player_job.lower() in valid_jobs:
        myPlayer.job = player_job
        print("You are now a " + player_job + "!\n")
    while player_job.lower() not in valid_jobs:
        player_job = input ("> ")
        if player_job.lower() in valid_jobs:
            myPlayer.job = player_job
        print("You are now a " + player_job + "!\n")
    myPlayer.job = player_job
    
    #Class stats#

    if myPlayer.job is 'warrior':
        self.hp = 120
        self.mp = 20
    elif myPlayer.job is 'mage':
        self.hp = 40
        self.mp = 120
    elif myPlayer.job is 'priest':
        self.hp = 60
        self.mp = 60
    #Introduction#

    question3 = 'Welcome, ' + myPlayer.name + ' the ' + myPlayer.job + '.\n'
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    
    speech1 = "Welcome to this fantasy world!\n"
    speech2 = "I hope it greets you well\n"
    speech3 = "Just make sure you don't get too lost...\n"
    speech4 = "Hehehe....\n"
    for character in speech1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.03)
    for character in speech2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.03)
    for character in speech3:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.01)
    for character in speech4:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.2)
    os.system('cls')
    print("#####################")
    print("  Let's start now!   ")
    print("#####################")
    main_game_loop()
    

title_screen()















    

























































