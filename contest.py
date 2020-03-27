#!/usr/bin/python3

import time
from random import seed
from random import randint

# Some rules are written in stats!
MAX_LEVEL = 1
MAX_STRENGTH = 5
MAX_DEXTERITY = 5
MAX_CONSTITUTION = 5
MAX_STATS = 11

# Defines character attributes - this is an "object." 
class Fighter:
  def __init__(self, name, strength, dexterity, constitution):
    self.name = name
    self.strength = strength
    self.dexterity = dexterity
    self.constitution = constitution
    
    # new users have zero experience
    self.xp = 0
    
    # Define rules
    # we want to make sure we can return an error if the stats are too high. 

    if (self.strength + self.dexterity + self.constitution > MAX_STATS):
      self.strength = 3;
      self.dexterity = 3;
      self.constitution = 3;

    # we define hit points after the rules check to make sure we have a valid number
    self.hp = self.constitution * 2

  def sheet(fighter):
    print(fighter.name + "! (" + str(fighter.strength) + ", " + str(fighter.dexterity) + ", " + str(fighter.constitution) + ").");
    print("I have " + str(fighter.xp) + " experience points.")
    fighter.healthStatus()
    print("\n");
    
  def healthStatus(fighter):
    print(fighter.name + " has " + str(fighter.hp) + " hit points remaining.")

  def attacks(pOne, pTwo):
    if ((pOne.dexterity + randint(1 , 6)) > (pTwo.dexterity + randint(1 , 6))):
      print("It's a hit...", end=" ")
      time.sleep(1)
      pTwo.hp = pTwo.hp - randint(1, pOne.strength*2)
      print(pTwo.name + " now has only " + str(pTwo.hp) + " hit points remaining.")
      time.sleep(1)
    else:
      print("It's a miss!")
      time.sleep(1)


  def battle(pOne, pTwo):
    print ("This is a battle between... ")
    pOne.sheet()
    pTwo.sheet()
    time.sleep(2)
    while ((pOne.hp > 0) and (pTwo.hp > 0)):
      if (randint(0, pOne.dexterity + pTwo.dexterity) < pOne.dexterity):
        print(pOne.name + " goes first...", end=" ")
        pOne.attacks(pTwo)
        if (pTwo.hp > 0):
          print(pTwo.name + " responds...", end=" ")
          pTwo.attacks(pOne)
        else:
          pOne.xp=pOne.xp+50
          print(pTwo.name + " is out of health!")
      else:
        print(pTwo.name + " goes first..." , end=" ")
        pTwo.attacks(pOne)
        if (pOne.hp > 0):
          print(pOne.name + " responds...", end=" ")
          pOne.attacks(pTwo)
        else:
          print(pOne.name + " is out of health!")
          pTwo.xp=pTwo.xp+50

lev = Fighter("Lev", 3, 4, 4)
eli = Fighter("Eli", 4, 3, 4)
dom = Fighter("Dom", 5, 2, 4)

lev.battle(dom)

lev.sheet()
dom.sheet()




# Other ideas 
# - better stat sheets?
# - different weapons?
# - potions?
# - monster fights?
# - faster character creation?