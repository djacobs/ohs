import random
from Contest import Creature
from Contest import Fighter
from Contest import Monster
from Contest import Cat

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
  drop [item]
  name [name]
  open chest
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('Your name is ' + playerName)
  #print('You are in the ' + currentRoom)
  #print the current inventory
  #print('Inventory : ' + str(inventory))
  #print an item if there is one
  #if "item" in rooms[currentRoom]:
  #  print('You see a ' + rooms[currentRoom]['item']['label'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
rooms = {
  'Hall' : { 
    'south' : 'Kitchen',
    'west' : 'The Living Room',
    'item' : { 'label': 'key',
               'description' : 'A gnarled old key with a skull insignia' }
  },
  
  'Kitchen' : {
    'north' : 'Hall',
    'item' : { 'label' : 'mask', 
               'description' : 'Whoever is wearing the mask makes everyone sad with the word YEE' }
  },
  'The Living Room' : {
    'east' : 'Hall',
    'item' : { 'label' : 'chest',
               'description' : 'this chest was rumored to have a pirates greatest plunder.'}
  }
}

#start the player in the Hall
currentRoom = 'Hall'
playerName = 'Small'

showInstructions()

showStatus()

  
#loop forever
while True:

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':  
    move = input('Hello ' + playerName + ' go <direction>, get <item>, or status? ')
    move = move.lower().split()
  
  # "command" is command
  # "direction" is what comes after the command, if it exists
  
  command = move[0]
  if len(move) > 1:
    direction = move[1]
  else:
    direction = ""
  
  
  
  
  ## In here is all the stuff
  
  if command=="go":
    print("Command was go", direction)    
  elif command=="get":
    print("Command was get the", direction)
  elif command=="status":
    showStatus()
  else:
    print ("You want to ", command, " in the direction of ", direction, "but I don't know how")
