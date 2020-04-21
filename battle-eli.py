from Contest import Fighter
from Contest import Monster
from Contest import Creature
from random import randint
#from Constest import kibble absorber
import time

# In Contest we make new Fighters or Monsters  name, strength, dexterity, constitution
# and we get hp, xp and "type"
# 4 8 15 16 23 42





  

def dice(n):
  return random.randint(1,n)


  #Cat("Meowscles", 1, 148, 1)



  # return Kibble_absorber("Small",10000000,1000000,1000000)           
  #return cat("Small",1000000,1000000,1000000)           




meowmeow = Kibble("Meowmeow",1,77,2)

super_Small_kibble_absorber = Kibble("super Small kibble absorber",99,78,99)

super_Small_kibble_absorber.sheet()

super_Small_kibble_absorber.battle(meowmeow)

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

#super_small_kibble_absorbed = kibble("super small kibble absorbed")



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







