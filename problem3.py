'''---------------------------------------------
PROBLEM 3: A person has two blank 6-sided dice.
They have 2 of every number (1 -- 6) available
to randomly distribute on the faces of the dice.
Considering all possible combinations,
what is the probability of rolling a seven?
----------------------------------------------'''

# There are 12! ways of arranging the 12 numbers on the
# two 6-sided dice.

import random
from itertools import permutations

dice = list(range(1,7)) + list(range(1,7))

#possible = permutations(dice)



#def makeDice():
#    dice = list(range(1,7)) + list(range(1,7))
#    random.shuffle(dice)
#    return dice
#
#def roll(die1, die2):
#    return random.choice(die1) + random.choice(die2)

#count = 0
#maxRolls = 10000
#
#for i in range(maxRolls):
#    dice = makeDice()
#    die1 = dice[:6]
#    die2 = dice[6:]
#    currentRoll = roll(die1, die2)
#    if currentRoll == 7:
#        count += 1
#
#print(count/maxRolls)