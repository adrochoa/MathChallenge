'''---------------------------------------------------------
PROBLEM 2: You have a bag containing
1 red ball, 1 blue ball, and 1 yellow ball.
You remove two balls.
The second ball you remove, color it the same as the first,
and put the two balls back in the bag.
What is the average number of times you do this
before all balls are the same color?
Solution by Adrian Ochoa 02/07/2018
---------------------------------------------------------'''

# This script provides strong evidence in favor of the answer
# arrived at in the included solutions document:
# We expect 4 replacements before reaching a single color state.

import random

# the changeState function receives the current
# state of the bag and outputs the next state
# by the described random replacement procedure
def changeState(origState):
    state = origState[:] # copy original state since it will be used for multiple trials
    choice1 = random.choice(state) # choose 1st ball
    state.remove(choice1) # remove 1st ball
    choice2 = random.choice(state) # choose 2nd ball
    state.remove(choice2) # remove 2nd ball
    choice2 = choice1 # explicit painting of 2nd ball
    state.append(choice1) # place balls back in the bag
    state.append(choice2)
    return state

# the numChanges function finds the number of
# replacements completed via the changeState
# function before the bag is in a state of
# having 3 balls of the same color
def numChanges(state):
    count = 0
    while len(set(state)) != 1: # set function removes repeated elements
        state = changeState(state)
        count += 1
    return count

# the avgTrials function does k experiments each yielding
# a bag in a single color state from some initial state.
# The output is the average number of replacements
# required over those k expeiments before reaching 
# a single color state.
def avgTrials(state, k):
    trials = [numChanges(state) for i in range(k)] # run k experimental trials
    return sum(trials)/k # average over the experimental trials

origState = [1, 2, 3] # the bag contains 3 different balls

k = 100000

avgNum = avgTrials(origState, k)

print("It took {} replacements on average for the bag to contain three balls of the same color.".format(avgNum))