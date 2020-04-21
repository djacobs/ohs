from Contest import Fighter
from Contest import Monster
from Contest import Creature
from random import randint
import time

# In Contest we make new Fighters or Monsters  name, strength, dexterity, constitution
# and we get hp, xp and "type"
# 4 8 15 16 23 42
#wassup
MAX_CAT_STATS = 150


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
            pOne.strength += 10  
            pOne.dexterity += 3
               
            
          
          
          
def dice(n):
  return random.randint(1,n)


def lev(n): 
  return Cat("Meowscles", 2, 78, 1)


def dom(n):
  return Cat("Meowmeow",2,78,1)


#def eli(n):
  # return Kibble_absorber("Small",10000000,1000000,1000000)           
  #return cat("Small",1000000,1000000,1000000)           







meowscles = lev(10)

meowmeow = dom(10)

#small = eli(2)
#small.sheet()

meowscles.battle(meowmeow)

# TODO - support AND syntax in battles! 


# TODO - IDEAS
# New Class: cat
# New Class: superhero
# New Class: Kibble Absorber
# - classes? (Knight, Demon, Archer, Wizard, Mechanic,fat cat) (a la Dom's exercise)


# TOURNAMENT! 
#  - one battle winner battles another battle-winner (and so on)
#  - the winner absorbs the losers stats
#  - We could also do 2 v 2 or 1 v 3

# Other ideas 
# - better stat sheets?
# - could characters have quirks?
# - different weapons?
# - potions?
# - monster fights (multiple fighters attack a monster?)
# - legendary monsters?
# - faster character creation?
# - level-ups?


#print(dice(6))
#small = Fighter("Small",dice(7), dice(7), dice(7))
#medium = Fighter("Medium", dice(8), dice(4), dice(3))

#super_small_kibble_absorbed = cat("super small kibble absorbed")



#hurley = Fighter("Hurley", 7, 7, 4)
#locke = Fighter("Locke", 4, 4, 4)
#jack = Fighter("Jack", 5, 3, 3)

#hurley.sheet()
#locke.sheet()

#smokey = Monster("Smokey",50,50,50)


  





def dice(n):
  return random.randint(1,n)

#hurley = Fighter("Hurley", dice(5), dice(5), dice(5))
#locke = Fighter("Locke", dice(5), dice(5), dice(5))







