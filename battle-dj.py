from Contest import Creature
from Contest import Fighter
from Contest import Monster
from Contest import Cat
import random

# In Contest we make new Fighters or Monsters  name, strength, dexterity, constitution
# and we get hp, xp and "type"
# 4 8 15 16 23 42


class Kibble(Creature):
  print("This is a test")
  

def dice(n):
  return random.randint(1,n)

def lev(n): 
  a = dice(n)
  return Cat("Meowscles", a, 80-2*a, a)


def dom(n):
  a = dice(n)
  return Cat("Meowmeow",a,70-2*a,10+a)


def eli(n):
  return Kibble("Small",10000000,1000000,1000000)

  #return cat("Small",1000000,1000000,1000000)           


#small = eli(2)
#small.sheet()





meowscles = lev(10)
meowmeow = dom(10)

meowscles.battle(meowmeow)


meowscles.sheet()
meowmeow.sheet()

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
# nitro = Fighter("Nitro", 5, 5, 1)
#  Admiralspaceship = Fighter("Admiral spaceship", 5, 5, 1)
#  Shrek = Fighter("Shrek", 1, 1, 1)
# You aren't allowed "." in the names on the left side of the = - so it has to be "eat" not "e.a.t"
# eat = Fighter("Eat", 1, 5, 5)
# fatcatomega = Fighter("fat cat omega", 5, 5, 5)




  






#hurley = Fighter("Hurley", dice(5), dice(5), dice(5))
#locke = Fighter("Locke", dice(5), dice(5), dice(5))







