from Contest import Fighter
from Contest import Monster
import random

# In Contest we give name, strength, dexterity, constitution
# and we get hp, xp


hurley = Fighter("Hurley", 4, 4, 4)
locke = Fighter("Locke", 4, 4, 4)

hurley.sheet()
locke.sheet()

smokey = Monster("Smokey",50,50,50)


  


# Right now we can make Fighter and Monster
# We can sheet, attack, heal, 



# Functions help us be lazy programmers, and it also helps us string multiple different programs together. 

# note that we moved from lower case to upper case for "Contest" 
# show them what stats are in a fighter. 

# We can change them, but we can't make new ones. 

# talk through the battle I wrote, and then ...
# Ask the kids to build their own battle that returns the winner. 



#def dice(n):
#  return random.randint(1,n)

#hurley = Fighter("Hurley", dice(5), dice(5), dice(5))
#locke = Fighter("Locke", dice(5), dice(5), dice(5))




# Other ideas 
# - better stat sheets?
# - could characters have quirks?
# - different weapons?
# - potions?
# - monster fights (multiple fighters attack a monster?)
# - legendary monsters?
# - faster character creation?
# - level-ups?
# - classes? (a la Dom's exercise)


