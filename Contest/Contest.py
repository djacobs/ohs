#!/usr/bin/python3

# Importing functions we need
import time
from random import seed
from random import randint

# these are CONSTANTS - we expect them to not change
# Some rules are written in stats!

# We are using these two to keep characters from being OP
MAX_STATS = 12
MAX_MONSTER_STATS = 13
MAX_CAT_STATS = 150
MAX_KIBBLE_STATS = 5000

# We are not yet using these
MAX_LEVEL = 1

MAX_STRENGTH = 5
MAX_DEXTERITY = 5
MAX_CONSTITUTION = 5

MONSTER_RAGE_FACTOR = 2

MAX_SUPERHERO_STATS = 30



#4 8 15 16 23 42
# Defines character attributes - this is an "object."


class Creature:
  def __init__(self):
    print("A creature appears")

  def sheet(fighter):
    print(fighter.name + "! (" + str(fighter.strength) + ", " + str(fighter.dexterity) + ", " + str(
      fighter.constitution) + ").");
    print("I have " + str(fighter.xp) + " experience points.")
    fighter.healthStatus()
    print("\n");

  def healthStatus(fighter):
    print(fighter.name + " has " + str(fighter.hp) + " hit points remaining.")

  def attacks(attacker, defender):
    if (attacker.dexterity + randint(1, 4)) > (defender.dexterity + randint(1, 6)):
      print("It's a hit...", end=" ")
      time.sleep(1)
      defender.hp = defender.hp - randint(1, attacker.strength + 2)
      print(defender.name + " now has only " + str(defender.hp) + " hit points remaining.")
      time.sleep(1)
    else:
      print("It's a miss!")
      time.sleep(1)
    if defender.hp <= 0:
      print(defender.name, "is out of health.")
      attacker.xp += 50

  # This is the monster battle code, which we will change later to be different than the fighter battle code
  def battle(pOne, pTwo):
    print("This is a battle between... ")
    # First we print the character sheets
    pOne.sheet()
    pTwo.sheet()
    # Sleep for two seconds for dramatic effect
    time.sleep(2)

    # While both players have positive hit points
    while (pOne.hp > 0) and (pTwo.hp > 0):
      if randint(0, pOne.dexterity + pTwo.dexterity) < pOne.dexterity:
        print(pOne.name + " goes first...", end=" ")
        pOne.attacks(pTwo)
        if (pTwo.hp > 0):
          print(pTwo.name + " responds...", end=" ")
          pTwo.attacks(pOne)
      else:
        print(pTwo.name + " goes first...", end=" ")
        pTwo.attacks(pOne)
        if (pOne.hp > 0):
          print(pOne.name + " responds...", end=" ")
          pOne.attacks(pTwo)

  def heal(pOne):
    self.hp = self.constitution * 2


class Fighter(Creature):
  def __init__(self, name, strength, dexterity, constitution):
    self.name = name
    self.strength = strength
    self.dexterity = dexterity
    self.constitution = constitution

    # new users have zero experience
    self.xp = 0
    self.type = "fighter"

    # Define rules
    # we want to make sure we can return an error if the stats are too high.

    while (self.strength + self.dexterity + self.constitution > MAX_STATS):
      self.strength = 3;
      self.dexterity = 3;
      self.constitution = 3;
      print("Looks like", self.name, "was a little OP... We've fixed that!")

    # we define hit points after the rules check to make sure we have a valid number
    self.hp = self.constitution * 2
    print("The fighter", self.name, "is born.")


class Monster(Creature):
  def __init__(self, name, strength, dexterity, constitution):
    self.name = name
    self.strength = strength
    self.dexterity = dexterity
    self.constitution = constitution

    # new users have zero experience
    self.xp = 0
    self.type = "monster"
    # Define rules
    # we want to make sure we can return an error if the stats are too high.

    if (self.strength + self.dexterity + self.constitution > MAX_MONSTER_STATS):
      self.strength = 3;
      self.dexterity = 3;
      self.constitution = 3;
      print("Looks like", self.name, "was a little OP... We've fixed that!")

    # we define hit points after the rules check to make sure we have a valid number
    self.hp = self.constitution * 2
    print("The monster", self.name, "emerges from the depths.")

class Cat(Creature):
  def __init__(self, name, strength, dexterity, constitution):
    self.name = name
    self.strength = strength
    self.dexterity = dexterity
    self.constitution = constitution

    # new users have zero experience
    self.xp = 0
    self.type = "cat"
    # Define rules
    # we want to make sure we can return an error if the stats are too high.

    if (self.strength + self.dexterity + self.constitution > MAX_CAT_STATS):
      self.strength = randint(3, 34);
      self.dexterity = randint(3, 34);
      self.constitution = randint(3,34);
      print("Looks like", self.name, "was a little OP... We've fixed that!")

    # Cats have nine lives!  
    self.constitution = constitution * 9

    # we define hit points after the rules check to make sure we have a valid number
    self.hp = self.constitution * 2
    print("The cat", self.name, "rolls throughs the cat flap.")

  # This is cat attacks code
  def attacks(attacker, defender):
    if (attacker.dexterity * randint(1, 10)) > (defender.dexterity * randint(1, 12)):
      print("It's a hit." +attacker.name+ " is about to use the scratch of the 9 lives...", end=" ")
      time.sleep(1)
      defender.hp = defender.hp - randint(1, attacker.strength  + attacker.constitution - 3)
      print(defender.name + " now has only " + str(defender.hp) + " hit points remaining.")
      time.sleep(1)
    else:
      print("It's a miss. " + attacker.name + "'s owner is not proud !")
      time.sleep(1)
    if defender.hp <= 0:
      print(defender.name, "is now bored.")
      attacker.xp += 100000

  # This is the cat battle code, which we will change later to be different than the fighter battle code
  def battle(pOne, pTwo):
    print("This is a battle between... ")
    # First we print the character sheets
    pOne.sheet()
    pTwo.sheet()
    # Sleep for two seconds for dramatic effect
    time.sleep(2)

    # While both players have positive hit points
    while (pOne.hp > 0) and (pTwo.hp > 0):
      if randint(0, pOne.dexterity + pTwo.dexterity) < pOne.dexterity:
        print(pOne.name + " goes first...", end=" ")
        pOne.attacks(pTwo)
        if (pTwo.hp > 0):
          print(pTwo.name + " responds...", end=" ")
          pTwo.attacks(pOne)
      else:
        print(pTwo.name + " goes first...", end=" ")
        pTwo.attacks(pOne)
        if (pOne.hp > 0):
          print(pOne.name + " responds...", end=" ")
          pOne.attacks(pTwo)
          
          #while there at low health they it is harder to hit but does more damage.(having revenge)
          if pOne.hp <4:
            print(pOne.name+ " is feeling a rage inside")
            pOne.strength += 20  
            pOne.dexterity += 10
               
            
class Kibble(Creature):
  def __init__(self, name, strength, dexterity, constitution):
    self.name = name
    self.strength = strength
    self.dexterity = dexterity
    self.constitution = constitution

    # new users have zero experience
    self.xp = 0
    self.type = "kibble"
    # Define rules
    # we want to make sure we can return an error if the stats are too high.

    if (self.strength + self.dexterity + self.constitution > MAX_KIBBLE_STATS):
      self.strength = 100;
      self.dexterity = 100;
      self.constitution = 100;
      print("Looks like", self.name, "was a little OP... We've fixed that!")

    # we define hit points after the rules check to make sure we have a valid number
    self.hp = self.constitution * 2
    print("The cat", self.name, "rolls throughs the cat flap.")

  # This is cat attacks code
  def attacks(attacker, defender):
    if (attacker.dexterity + randint(1, 4)) > (defender.dexterity + randint(1, 6)):
      print("It's a hit...", end=" ")
      time.sleep(1)
      defender.hp = defender.hp - randint(1, attacker.strength + 2)
      print(defender.name + " now has only " + str(defender.hp) + " hit points remaining.")
      time.sleep(1)
    else:
      print("It's a miss!")
      time.sleep(1)
    if defender.hp <= 0:
      print(defender.name, "is turned into kibble and absorbed.")
      # This is were the other person gets turned into kibble ant absorbed
      attacker.strength += defender.strength
      attacker.dexterity += defender.dexterity
      attacker.constitution += defender.constitution
      

  # This is the cat battle code, which we will change later to be different than the fighter battle code
  def battle(pOne, pTwo):
    print("This is a battle between... ")
    # First we print the character sheets
    pOne.sheet()
    pTwo.sheet()
    # Sleep for two seconds for dramatic effect
    time.sleep(2)

    # While both players have positive hit points
    while (pOne.hp > 0) and (pTwo.hp > 0):
      if randint(0, pOne.dexterity + pTwo.dexterity) < pOne.dexterity:
        print(pOne.name + " goes first...", end=" ")
        pOne.attacks(pTwo)
        if (pTwo.hp > 0):
          print(pTwo.name + " responds...", end=" ")
          pTwo.attacks(pOne)
      else:
        print(pTwo.name + " goes first...", end=" ")
        pTwo.attacks(pOne)
        if (pOne.hp > 0):
          print(pOne.name + " responds...", end=" ")
          pOne.attacks(pTwo)  
  print("This is a test")
  

   
          
          
if __name__ == "__main__":
  
  # These things only run if we call "Contest" from the command line. 
  
  
  lev = Fighter("Lev", 3, 4, 4)
  eli = Fighter("Eli", 5, 3, 4)
  dom = Fighter("Dom", 5, 2, 4)
 
  drScientist = Monster("DR science", 8, 5, 8)
  Getoutman = Monster("Get out man", 50, 50, 50)

  nitro.battle(lev)

  nitro.sheet()
  lev.sheet()

