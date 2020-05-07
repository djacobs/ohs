#!/bin/python3

# Replace RPG starter project with this code when new instructions are live

# TODO
# X Change ['item'] calls to handle dictionaries instead of strings. 


# I did this by creating "label" and "description" for each item, after our class. 

# ELI the supreme : Require some items to come into some rooms (i.e., you can't go into the secret bookshelf without a cat.)

# DOM: Add a random element to the game (a battle, or roulette?) (i.e., maybe opening the door to a new room triggers a random event - a monster? a cat?)

# LEV: Add a new command ("go" and "get" are limited - battle? sleep? run? "drop" an item? )


# Refer to this for examples: https://www.w3schools.com/python/python_dictionaries.asp


def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item']['label'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
rooms = {
  'Hall' : { 
    'south' : 'Kitchen',
    'north' : 'Master Bedroom',
    'east'  : 'The Locked Room',
    'item' : { 'label': 'key',
               'description' : 'A gnarled old key with a skull insignia' }
  },
  'Kitchen' : {
    'north' : 'Hall'
  },
  'Master Bedroom' : {
    'south' : 'Hall',
    'east' : 'Secret Bookshelf Room',
    'item' : { 'label': 'knife', 
               'description' : 'a sharp knife' }
  },
  'Secret Bookshelf Room' : {
    'west' : 'Master Bedroom',
    'item' : { 'label' : 'cat',
               'description' : 'A diamond cat statuette holding a miniature meteor' } 
  },
  'The Locked Room' : {
    'west' : 'Hall',
    'item' : { 'label' : 'mask', 
               'description' : 'Whoever is wearing the mask makes everyone sad with the word YEE' }
  }
}

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '' or len(move)==1:  
    move = input('go or get? ')
    move = move.lower().split()
  

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']['label']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      # we can still only have one item per room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')

