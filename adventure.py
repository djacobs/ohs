import time

# This is Oxford homeschool session #1. 
# We are commenting this code for just three kids. 


print("\n")
# \n means NEW LINE - it's a little ugly, right?")
#Laser cats
#laser dogs vs laser cats
print(">>>The reign of the fat cats<<<\n")
print("Laser cats rising")
print("\n")
time.sleep(2)
print("\nA long time ago, a warrior strode forth from the frozen north.")
time.sleep(1)
print("Does this warrior have a name?")

name = input("> ")
print(name, "the barbarian, laser cat in hand and looking for adventure!")
time.sleep(1)
print("However, evil is lurking nearby....")
time.sleep(1)
print("A pair of bulbous eyes regards the hero...")
time.sleep(1)
print("Will", name, "prevail, and win great fortune...")
time.sleep(1)
print("Or die by the hands of great evil...?")
time.sleep(1)
print("\n")
print("\n")
print("\n")
print("Only time will tell...")
time.sleep(1)
print('...')
time.sleep(1)
 
print("\n")
 
print(''' You find yourself at a small inn. There's
  little gold in your purse but your laser cat is well fed,
  and you're ready for adventure.
  With you are three other customers.
  A ragged looking man, and a pair of dangerous
  looking guards.''')

def start():
  # This is how you add a new option
  print("----------")
        
  # What option are you presenting the player
  print("Do you approach the...")
  print("1. Ragged looking man")
  print("2. Dangerous looking guards")

  cmdlist=["1", "2"]
 
  cmd = getcmd(cmdlist)
 
  if cmd == "1":
    ragged()
  elif cmd == "2":
    guards()

    
def ragged():
  print("\n")
  print('''You walk up to the ragged looking man and
  greet him.  He smiles a toothless grin and, with a strange
  accent, says. "Buy me a cup of wine, and I'll tell you of
  great treasure...''')
  time.sleep(2)
  
  # What option are you presenting the player?
  print("Do you buy the ragged man a cup of wine, or do you threaten him?")
  print("1. Buy the man a cup of wine")
  print("2. Rough him up a bit, but not too much")

  cmdlist=["1", "2"]
 
  cmd = getcmd(cmdlist)
 
  if cmd == "1":
    DavidOne()
  elif cmd == "2":
    DavidTwo()


        
def guards():
  print("\n" * 2)
  print('''You walk up to the dangerous looking guards
  and greet them.  The guards look up from their drinks and
  snarl at you.  "What do you want, barbarian?" One guard reaches
  for the hilt of his sword...''')
 
  time.sleep(2)
  
  # What option are you presenting the player?
  print("here are your action...")
  print("1. be nice and socialise ")
  print("2. beat them up with laser cats")

  #this code presents the options      
  cmdlist=["1", "2"] 
  cmd = getcmd(cmdlist)
 
  if cmd == "1":
    LevOne()
  elif cmd == "2":
    LevTwo()

def DavidOne():
  print("\n")
  print(''' Thank you so much. Go to the barkeep and tell him you want to know the location of the treasure. The secret password is flooby. ''')
  time.sleep(2)
  
def DavidTwo():
  print("\n")
  print(''' The ragged man pulls a knife out of his shorts and calls for help!
  The two guards approach - they are drunk enough to be angry but not drunk enough so you can easily beat them up''')
 
  # What option are you presenting the player
  print("do you ...")
  print("1. battle them with the conveniently placed laser cat")
  print("2. try to get them more drunk")

  cmdlist=["1", "2"]
 
  cmd = getcmd(cmdlist)
 
  if cmd == "1":
    DomOne()
  elif cmd == "2":
    DomTwo()

def LevOne():
  print("\n" * 2)
  print(''' they get drunk and give you a laser cat ''')
 
  time.sleep(2)
  
def LevTwo():
  print("\n" * 2)
  print(''' they try to shoot you with laser dogs ''')
 
  time.sleep(2)
  # What option are you presenting the player?
  print("here are your action...")
  print("1. Dodge and shoot them with your rapid fire sniper minigun laser cat ")
  print("2. Shoot them with a nuke laser cat and obliterate them only including the guards for some strange reason")

  #this code presents the options      
  cmdlist=["1", "2"] 
  cmd = getcmd(cmdlist)
 
  if cmd == "1":
    LevOne()
  elif cmd == "2":
    LevTwo()


def EliOne():
  print("\n" * 2)
  print('''  ''')
 
  time.sleep(2)
  
def EliTwo():
  print("\n" * 2)
  print(''' Write What happens in Option 2 ''')
 
  time.sleep(2)
  
def DomOne():
  print("\n" * 2)
  print(''' you grab the laser cat and go through their legs but are stopped by the ragged man stabbing you.GAME OVER. ''')
 
  time.sleep(2)
  
def DomTwo():
  print("\n" * 2)
  print(''' You get some more beers for the guards but before you can the bartender gives you a laser cat as well as the beers.''')
 
  time.sleep(2)
  
  
def getcmd(cmdlist):
  cmd = input(name+"> ")
  if cmd in cmdlist:
    return cmd
  elif cmd == "help":
    print("\nEnter your choices as detailed in the game.")
    print("or enter 'quit' to leave the game")
    return getcmd(cmdlist)
  elif cmd == "quit":
    print("\n-----------")
    time.sleep(1)
    print("Sadly you return to your homeland without fame or fortune...")
    time.sleep(5)
    exit()
  else:
    print(" Please enter a valid option")
    return getcmd(cmdlist)

if __name__ =="__main__":
  start()  