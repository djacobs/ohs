import random
#!/bin/python3

# Replace RPG starter project with this code when new instructions are live

# TODO
# X Change ['item'] calls to handle dictionaries instead of strings. 


# I did this by creating "label" and "description" for each item, after our class. 

# A Fat Cat Spy : Require some items to come into some rooms (i.e., you can't go into the secret bookshelf without a cat.)

# DOM: Add a random element to the game (a battle, or roulette?) (i.e., maybe opening the door to a new room triggers a random event - a monster? a cat?)

# A Fat Cat Spy 2: Add a new command ("go" and "get" are limited - battle? sleep? run? "drop" an item? )


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
    'west' : 'Hall'    
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

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '' or len(move)==1:  
    move = input('go <direction>, get <item>, open chest, or tell us your name? ')
    move = move.lower().split()
  
  # Right now this is go or get, and soon Lev will add a new option laser cat .
  command = move[0]
  direction = move[1]
  
  if command == 'name':
    playerName = direction
    print("Your name is now ", playerName)
    
  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if direction in rooms[currentRoom]:
      # i will write if to get into the bookshelf rituel of doom room
      if rooms[currentRoom][direction]=='Ritual of Doom Room':
        if 'mask' in inventory:
          print("Praise yee you are the great internet meme you are allowed to pass! \n")
          currentRoom = rooms[currentRoom][direction]
        else:
          print("you cant get in as you are not a viral internet meme\n ")
      else:
        currentRoom = rooms[currentRoom][direction]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']['label']:
      #add the item to their inventory
      inventory.append(direction)
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      # we can still only have one item per room
      del rooms[currentRoom]['item']
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
      inventory.append("sword of demons")
    else:
      print("no chest in inventory")
      
      # what else could they open?? Right now only the chest. 
    
  #if 'key' in inventory:
  # Dominic we'll come back to this! :)     


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
        for i in inventory:
          if inventory[i] == 'mask':
            del inventory[counter]
          counter += 1
        rooms['Kitchen']['item'] = { 'label' : 'mask', 'description' : 'Whoever is wearing the mask makes everyone sad with the word YEE' }
        print("The mask has been taken from you!")
      currentRoom == 'hall'
      print("You are now back in the hall.")
      
    
    # 
    #i choose diamond
    # who are you .
     #your worst nightmare
      #hello lev
      #no im your worst nightmare jimmy bob
      #oh the pain everything getting so cold
      #if they get it wrong delete mask from inventory