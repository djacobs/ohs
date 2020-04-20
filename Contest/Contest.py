#!/usr/bin/python3

# Importing functions we need
import time
from random import seed
from random import randint

# these are CONSTANTS - we expect them to not change
# Some rules are written in stats!
MAX_LEVEL = 1
MAX_STRENGTH = 5
MAX_DEXTERITY = 5
MAX_CONSTITUTION = 5
MAX_STATS = 12
MAX_MONSTER_STATS = 13
MONSTER_RAGE_FACTOR = 2


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

  def attacks(pOne, pTwo):
    if (pOne.dexterity + randint(1, 6)) > (pTwo.dexterity + randint(1, 6)):
      print("It's a hit...", end=" ")
      time.sleep(1)
      pTwo.hp = pTwo.hp - randint(1, pOne.strength + 2)
      print(pTwo.name + " now has only " + str(pTwo.hp) + " hit points remaining.")
      time.sleep(1)
    else:
      print("It's a miss!")
      time.sleep(1)
    if pTwo.hp <= 0:
      print(pTwo.name, "is out of health.")
      pOne.xp += 50

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

    if (self.strength + self.dexterity + self.constitution > MAX_STATS):
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
    print("The monster", self.name, "is hatched.")


if __name__ == "__main__":
  lev = Fighter("Lev", 3, 4, 4)
  eli = Fighter("Eli", 5, 3, 4)
  dom = Fighter("Dom", 5, 2, 4)
  nitro = Fighter("Nitro", 5, 5, 1)
  Admiralspaceship = Fighter("Admiral spaceship", 5, 5, 1)

  # You aren't allowed "." in the names on the left side of the = - so it has to be "eat" not "e.a.t"

  eat = Fighter("E.A.T.", 1, 5, 5)
  fatcatomega = Fighter("fat cat omega", 5, 5, 5)

  # Hi! The syntax error was because Shrek was missing a trailing quote.
  # Originall it was:
  # Shrek = Fighter("Shrek,1,1,1)
  # Shrek's name needs to be in quotes Like this: "Shrek"

  Shrek = Fighter("Shrek", 1, 1, 1)

  #

  drScientist = Monster("DR science", 8, 5, 8)
  Getoutman = Monster("Get out man", 50, 50, 50)

  nitro.battle(lev)

  nitro.sheet()
  lev.sheet()

# Other ideas
# - better stat sheets?
# - could fighters have quirks?
# - different weapons?
# - potions?
# - monster fights?
# - faster character creation?
# - I think dexterity is too important right now ... we need to figure out how to make it less powerful! - DJ
