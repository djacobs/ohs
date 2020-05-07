from Contest import Fighter
from Contest import Monster
#from Contest import Cat
import random

# In Contest we make new Fighters or Monsters  name, strength, dexterity, constitution
# and we get hp, xp and "type"
# 4 8 15 16 23 42

def dice(n):
  return random.randint(1,n)


meowscles = Fighter("Meowscles", 4, 5, 3)
meowmeow = Fighter("Meowmeow",5,3,4)
tokoyami = Fighter("Tokoyami", 5, 5, 2)
muscular = Fighter("Muscular", 6, 2, 4)
def One_For_All(pOne): 
  pOne.strength += 5
  pOne.dexterity += 5
  pOne.constitution += 3
  print(pOne.name,"gets ready to detriot smash")




One_For_All(meowscles)

def Engine(pTwo):
  pTwo.dexterity += 6
  pTwo.strength += 4
  print(pTwo.name,"gets his engines ready")
   


def Dark_Shadow(pThree):
  pThree.dexterity += 5
  pThree.strength += 5
  print(pThree.name,"In the midst of night the Dark Shadow rises and brings down in mountain in its rage.")
  
  
Dark_Shadow(tokoyami)

  

def Muscle_Augmentation(pFour):
  pFour.strength += 7
  pFour.constitution += 5
  pFour.dexterity += 4
  print(pFour.name,"feels as the strength rise inside and the power explodes out.")
#def eli(n):
  # return Kibble_absorber("Small",10000000,1000000,1000000)           
 #return cat("Small",1000000,1000000,1000000)











#small = eli(2)
#small.sheet()

tokoyami.battle(meowscles)

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







