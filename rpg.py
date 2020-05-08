import random
from Contest import Creature
from Contest import Fighter
from Contest import Monster
from Contest import Cat

#!/bin/python3

# TODO

# LEV: Add a battle (Goblins) or a battle with Yee, zombies in the master bedroom?

# DOM: Make the locked room next to the kitchen, and require a key to enter the locked room

# ELI: "drop" an item so that it stays in the room you are in, helping with the battle 
# in the future: multiplayer support 

# TODO: 
# _ offer what directions are available when someone enters a room
# _ force the user to choose a name 


# Refer to this link for examples when you are stuck : https://www.w3schools.com/python/python_dictionaries.asp


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
    'east': 'The Locked Room',
    'west': 'The Living Room',
    'item' : { 'label': 'key',
               'description' : 'A gnarled old key with a skull insignia' }
  },
  
  'Kitchen' : {
    'north' : 'Hall',
    'south' : 'The Locked Room',
    'item' : { 'label' : 'mask', 
               'description' : 'Whoever is wearing the mask makes everyone sad with the word YEE' }
  },
  'Master Bedroom' : {
    'south' : 'Hall',
    'east' : 'Ritual of Doom Room',
    'item' : { 'label': 'knife', 
              'description' : 'a sharp knife' }
  },
  
  'Ritual of Doom Room' : {
     'west' : 'Master Bedroom',
     'item' : { 'label' : 'cat',
               'description' : 'A tubby diamond cat statuette holding a miniature meteor like a ball of yarn' } 
  },
  
  'The Locked Room' : {
    'north' : 'Kitchen'    
  },
  
  'The Living Room' : {
    'east' : 'Hall',
    'item' : { 'label' : 'chest',
               'description' : 'this chest was rumored to have a pirates greatest plunder.'}
  }
}

#start the player in the Hall
currentRoom = 'Hall'
playerName = ''

showInstructions()

fighter = Fighter(playerName, 4,4,4)

goblin = Monster("goblin", 2,4,2)
yee = Monster("YEE", 2,5,5 )
yee_empowered = Monster("YEE Empowered", 1,7,4)
zombie = Monster("Zombie", 5,2,1)
ghost = Monster("ghost", 1,4,4)
      
      
#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '' or len(move)==1:  
    if playerName == "":
      move = input('Hello, go <direction>, get <item>, open chest, drop <item>, or tell us your name? ')
    else: 
      move = input('Hello,', playerName, 'go <direction>, get <item>, open chest, drop <item> ')
    move = move.lower().split()
  
  # Right now this is go or get, and soon Lev will add a new option laser cat .
  command = move[0]
  direction = move[1]
  
  if command == 'name':
    playerName = direction
    print("Your name is now ", playerName)
    
  #if they type 'go' first
  if command == 'go':
    #check that they are allowed wherever they want to go
    if direction in rooms[currentRoom]:
      # i will write if to get into the bookshelf rituel of doom room
      if rooms[currentRoom][direction]=='Ritual of Doom Room':
        if 'mask' in inventory:
          print("Praise yee you are the great internet meme you are allowed to pass! \n")
          currentRoom = rooms[currentRoom][direction]
        else:
          print("you cant get in as you are not a viral internet meme\n ")
      elif rooms[currentRoom][direction]=='The Locked Room':          
        # If you have the key... 
        if 'key' in inventory:
          print("welcome to the locked room! \n")
          currentRoom = rooms[currentRoom][direction]
        else:
          print("no key no YEE")
      else:
        currentRoom = rooms[currentRoom][direction]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')
    # When a user goes to a new room, see if there is a monster waiting to battle
    dice = random.randint(1,6)
    #user_guess = int(input("Put in a number from one to six: "))
    if not(dice == 6):
      print("no monsters appeared!")
    else:
      fighter.battle(ghost)
      

    
    # ask the user to guess a random number
    #goblin = ("goblin" = 2,4,2)
    # if the user guess right, a Goblin appears
    # Yee is always in the locked room
    
        
        
        
  #if they type 'get' first
  if command == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']['label']:
      #add the item to their inventory
      inventory.append(direction)
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      # we can still only have one item per room
      del rooms[currentRoom]['item']
      # if the item is a weapon 
      # then we need to add strength, dexterity and/or consitution to our hero, the fighter
      
      if direction=="knife":
        fighter.strength += 3 
        fighter.dexterity += 5 
      
      if direction=="sword_of_demons":
        fighter.strength += 5 
        fighter.dexterity += 3
        fighter.constitution += 3 
        
      
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')

      #choose == ""

  if command == 'open':
    # Check to see if the user has the chest in their inventory 
    # And if they do - what rewards to they get? 
    if "chest" in inventory:
      print("you get 20000 gold and the sword that labled he who finds becomes king of the demons but beware with great power comes great bloodlust")
      inventory.append("gold")
      inventory.append("sword_of_demons")
    else:
      print("no chest in inventory")
      
      # what else could they open?? Right now only the chest. 
  
  if command == 'drop':
    print("you are going to drop an item") 
    # check to see if <direction> is in inventory
      # if it is, remove the item
      # and make sure you add it to the inventory of the room where you are standing (currentRoom)
      # if it is not, say "You actually don't have one"
  
  
  

  #cheebee
  # Dominic we'll come back to this! :)     

#you need the key to get into the locked room
  
  # chance to see your fate
  if currentRoom == 'The Locked Room':
    print("this is the locked room. now you are in the presence of the YEE you must take your chances.")
    # the true answer is random
    answer = random.randint(1, 5)  
    print("five crystals appear 1.silver 2.gold 3.bronze 4.copper 5.diamond")
    choose = int(input("choose a crystal. Choose it by it's number."))
    if choose == answer:
      inventory.append("crystal")
      print("congrats you win now you may keep the mask.")
      currentRoom == 'hall'
      print("Welcome back to the hall")
    else:
      print("that is wrong it was crystal " + str(answer))
      print("YEE is not impressed.")
      if 'mask' in inventory:
        counter=0
        while counter < len(inventory):
          if inventory[counter] == 'mask':
            del inventory[counter]
          counter += 1
        rooms['Kitchen']['item'] = { 'label' : 'mask', 'description' : 'Whoever is wearing the mask makes everyone sad with the word YEE' }
        print("The mask has been taken from you!")
      currentRoom == 'hall'
      print("You are now back in the hall.")
      
    

   
     
      #if they get it wrong delete mask from inventory