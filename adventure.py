import time

# This is Oxford homeschool session #1. 
# We are commenting this code for just three kids. 


print("\n")
print("\n means NEW LINE - it's a little ugly, right?")
print("\n");

print(">>>Awesome Adventure<<<\n")
print("\n")
time.sleep(2)
print("\nA long time ago, a warrior strode forth from the frozen north.")
time.sleep(1)
print("Does this warrior have a name?")

name = input("> ")
print(name, "the barbarian, sword in hand and looking for adventure!")
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
  little gold in your purse but your sword is sharp,
  and you're ready for adventure.
  With you are three other customers.
  A ragged looking man, and a pair of dangerous
  looking guards.''')

def start():
  # This is how you add a new option
  print("----------")
        
  # What option are you presenting the player?
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
  print("Write your two options here...")
  print("1. <Write Option 1 here>")
  print("2. <Write Option 2 here>")

  cmdlist=["1", "2"]
 
  cmd = getcmd(cmdlist)
 
  if cmd == "1":
    LevOne()
  elif cmd == "2":
    LevTwo()


        
def guards():
  print("\n" * 2)
  print('''You walk up to the dangerous looking guards
  and greet them.  The guards look up from their drinks and
  snarl at you.  "What do you want, barbarian?" One guard reaches
  for the hilt of his sword...''')
 
  time.sleep(2)
  
  # What option are you presenting the player?
  print("Write your two options here...")
  print("1. <Write Option 1 here>")
  print("2. <Write Option 2 here>")

  #this code presents the options      
  cmdlist=["1", "2"] 
  cmd = getcmd(cmdlist)
 
  if cmd == "1":
    DavidOne()
  elif cmd == "2":
    DavidTwo()

def DavidOne():
  print("\n")
  print(''' Write what happens in Option 1 ''')
 
  time.sleep(2)
  
def DavidTwo():
  print("\n")
  print(''' Write What happens in Option 2 ''')
 
  time.sleep(2)
  
  
def LevOne():
  print("\n" * 2)
  print(''' Write what happens in Option 1 ''')
 
  time.sleep(2)
  
def LevTwo():
  print("\n" * 2)
  print(''' Write What happens in Option 2 ''')
 
  time.sleep(2)

def EliOne():
  print("\n" * 2)
  print(''' Write what happens in Option 1 ''')
 
  time.sleep(2)
  
def EliTwo():
  print("\n" * 2)
  print(''' Write What happens in Option 2 ''')
 
  time.sleep(2)
  
def DomOne():
  print("\n" * 2)
  print(''' Write what happens in Option 1 ''')
 
  time.sleep(2)
  
def DomTwo():
  print("\n" * 2)
  print(''' Write What happens in Option 2 ''')
 
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