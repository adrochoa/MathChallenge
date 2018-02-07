'''----------------------------------------------
PROBLEM 3: A person has two blank 6-sided dice.
They have 2 of every number (1 -- 6) available
to randomly distribute on the faces of the dice.
Considering all possible combinations,
what is the probability of rolling a seven?
Solution by Adrian Ochoa 02/07/2018
----------------------------------------------'''

import random
from itertools import combinations
import matplotlib.pyplot as plt

# countSevens will count the number of ways
# a seven can be rolled given two dice
def countSevens(die1, die2):
    validRolls = [1 for i in die1 for j in die2 if i + j == 7]
    return sum(validRolls)

diceNums = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6] # numbers to write on dice

# there are 12 choose 6 = 924 possible 6 sided dice

dice1 = list(combinations(diceNums, 6))
dice2 = dice1[:] # copy die1
dice2.reverse() # reverse to match corresponding dice

# we now seek to find the number of ways 
# one can roll a seven in each case

#counts = []
#for d1, d2 in zip(dice1, dice2):
#    counts.append(countSevens(d1,d2))

counts = [countSevens(d1, d2) for d1, d2 in zip(dice1, dice2)]    

print("There are {} ways to roll a seven among all possible combinations of dice.".format(sum(counts)))


#----------------------------#
# Simulation of the scenario #
#----------------------------#

# The following simulation provides strong
# evidence that p = 2/11 = 0.1818...

# makeDice returns a random set of dice
# from the problem space
def makeDice():
    dice = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
    random.shuffle(dice)
    return dice

# rollDice returns the value
# of the roll from a set of dice
def rollDice(die1, die2):
    return random.choice(die1) + random.choice(die2)

flagSevens = 0 # initial counter
simRolls = 100000 # number of simulated rolls
accumulatedSevens = []

for i in range(simRolls):
    dice = makeDice()
    die1 = dice[:6]
    die2 = dice[6:]
    currentRoll = rollDice(die1, die2)
    if currentRoll == 7:
        flagSevens += 1
    accumulatedSevens.append(flagSevens / (i + 1))

print("The estimated probabillity of rolling a seven is {} with a sample size of {}".format(flagSevens/simRolls, simRolls))

#----------------------------------------#
# Plot simulation to observe convergence #
#----------------------------------------#

plt.plot(range(simRolls), accumulatedSevens)
plt.xlabel('simulation number (x)')
plt.ylabel('probability of rolling a seven (y)')
plt.title('running probability estimate')
plt.grid(True)
#plt.savefig("problem3convergence.png")
plt.show()