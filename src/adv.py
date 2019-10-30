from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east."),

    'overlook': Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. \n Ahead to the north, a light flickers in the distance,\n but there is no way across the chasm."),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
#Creating new player
new_player = Player("BryBryTheFryGuy","foyer")
#messing with our data 

def get_rooms():
    for item in room.keys():
        print(item)
    choose_path_input()




"""
Setting up my Room Structure
function that when you reach a room it describes it.
input handler

"""
#setting up input and rules
def choose_path_input():
    global direction
    print(f"To Move Around Use The N,S,E,W Keys. \n To See all the Rooms press R \n And to quit the game please enter q\n")
    direction=input().lower()
    game_handler()
#setting up direction handler
def game_handler():
    if direction == 'r':
        get_rooms()
    if direction == 'q':
        print(f"You have Quit the Game Successfully")





choose_path_input()