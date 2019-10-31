from room import Room
from player import Player


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

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
#Creating player
Bryce = Player("Bryce",room["outside"])
#defining location so that we can use it within our loop

current_location = None
print('Choose a direction (n,s,e, or w) or quit the game by pressing q!\n')
#A while loop is set up. Code runs until playing = false 
playing = True
while playing:
  for key, value in room.items():
      #loops through items from the room dictionary and if the value === my current location it prints the value
    # print(value.name,"value.name")
    # print(Bryce.location.name,"Printing Bryce.location.name")
    if value.name==Bryce.location.name:
       print(value)
       current_location = value
       #Given certain moves it sees if its a valid move and if it is it moves
  move=input(f"\nWhich direction should we head, {Bryce.name}?\n")
  if move == "n":
      #if input doesn't exist it doesn't move forward.
      if Bryce.location.n_to == None:
        print("\nWe can't go there!")
      else:
          #sets Location Class value to the input value 
        Bryce.location = Bryce.location.n_to
  if move == "s":
      if Bryce.location.s_to == None:
        print("\nWe can't go there!")
      else:
        Bryce.location = Bryce.location.s_to
        print
  if move == "e":
      if Bryce.location.e_to == None:
        print("\nWe can't go there!")
      else:
        Bryce.location = Bryce.location.e_to
  if move == "w":
      if Bryce.location.w_to == None:
        print("\nWe can't go there!")
      else:
        Bryce.location = Bryce.location.w_to
  if move == "q":
      print(f"You found some treasure. It is the knowledge you gained from stuggling on this stupid project")
      playing=False

#messing with our data 
# def game_start():
#     print(f'Thank you for choosing my adventure game! I have put a whole afternoon into it.')
#     print(f"-------------------------------------------------------------------------------")
#     print("Please Select a room")
#     print("To Select a room please type in a room name")
#     print("To Inquire about the different rooms you can travel to please type R")


# def get_rooms():
#     for item in room.keys():
#         print(item)
#     choose_path_input()


# def pick_direction():
#     global explore
#     print("classic impass. Looks like we gotta make a decison here")
#     explore = input().lower()

    


# If the user enters "q", quit the game.
# def choose_path_input():
#     global direction
#     print(f"To Move Around Use The N,S,E,W Keys. \n To See all the Rooms press R \n And to quit the game please enter q\n")
#     print(f"To begin please type in start")
#     direction=input().lower()
#     game_handler()


# #setting up direction handler
# def game_handler():
#     #setting up state
#     global state
#     #state checkers
#     def if_outside():
#         global state
#         state = 'choose_location'
#         if state == 'outside':
#             print("it seems you chose to outside. What a unique developer")
#             pick_direction()
#             if explore == 'n':
#                 state = 'foyer'
#                 print("time to move on to the foyer. (yeet...)")
#             elif explore == 'w':
#                 print("Bro thats a cliff i know CS is hard but we gotta make it through this")
#             elif explore == 's':
#                 print("Lets not go this way we need to go north")
#             elif explore == 'e':
#                 print("Have you tried north yet?")

#     def set_state():
#         print(f"Please Type in a location")
#         state = input().lower()

#     if direction == 'r':
#         get_rooms()
#     if direction == 'q':
#         print(f"You have Quit the Game Successfully")
#     if direction == 'start':

#         game_start()
#         set_state()
#         if_outside()

        # if state = 'foyer':
        #     print(f"hey guys im not sure what a foyer is so i don't know what to put here")
        #     pick_direction()
        








# choose_path_input()
# new_player = Player(room["outside"],"Bryce")

# direction = ''

# print("test")
     

# def get_location():
#     global direction
#     print("Please Choose a direction n,s,w,e or press q to quit my amazing game")
#     direction = input().lower()
#     newGame(direction)

# def describe_room():
#     for key, value in room.items():
#         print(new_player.current_room.name)


#         # print(new_player.current_room.name)
#     #   for key, value in room.items():
#     #     print(value.name)
#     #     if value.name==new_player.current_room.name:
#     #         print(value)
#             # print(f"Current Area...  \n      {key} \n{value}")
#     # for key, value in room.items():
#     #     if .current_room == key:
#     #         print(f"Current Area...  \n      {key} \n{value}")

            
    

# def newGame(direction):
#     if direction == 'q': 
#         print("You successfully exited the game")
#         return
#     if new_player.current_room == "outside":
#         if direction == 'n':
#            new_player.current_room = "foyer"
#            describe_room()
#            get_location()


#         else:
#             print ("test")
#             get_location()

#     elif new_player.current_room == "foyer":

#         if direction == 's':
#            new_player.current_room = "outside"
#         #    print("you approach the Outside... \n look around do you spot anything?")
#            describe_room()
#            get_location()

#         elif direction == 'n':
#            new_player.current_room = "overlook"
#            print("You see a cliff... Watch your step bruh")
#            describe_room()
#            get_location()

#         elif direction == 'e':
#            new_player.current_room = "narrow"
#            print("Whats this? gold fills your senses")
#            describe_room()
#            get_location()
       
#         else:
#             print ("test")
#             get_location()

#     elif new_player.current_room == "overlook":
#         print("you have arrived at the overlook, think carefully about which direction you will decide to go")
#         if direction == 's':
#            new_player.current_room = "foyer"
#            describe_room()



#         else:
#             print ("test")
#             get_location()

#     elif new_player.current_room == "narrow":
#         print("You are walking through a narrow passage. there are multiple routes to take choose wisely")
#         if direction == 'w':
#            new_player.current_room = "foyer"
#            describe_room()
#            get_location()
        
#         elif direction == 'n':
#            new_player.current_room = "treasure"
#            describe_room()
#            get_location()

#         else:
#             print ("test")
#             get_location()

#     elif new_player.current_room == "treasure":
#         if direction == 's':
#            new_player.current_room = "narrow"
#            describe_room()
#            get_location()

#         else:
#             print ("test")
#             get_location()

# # describe_room()
# # get_location()
    
# get_location()