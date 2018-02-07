'''-------------------------------------------------------------
PROBLEM 1: Say you have the three vectors, shown below.
Randomly choose three sequential elements from each vector.
This makes nine total items chosen.
What is the probability that among the nine there are three A's?
Solution by Adrian Ochoa 02/07/2018
--------------------------------------------------------------'''

# original vectors under consideration

vec1 = ['B', 'C', 'E', 'F', 'A', 'D', 'F', 'C', 'G', 'A', 'A', 'C', 'B', 'D', 'E', 'F']
vec2 = ['G', 'C', 'E', 'F', 'B', 'D', 'F', 'A', 'A', 'A', 'B', 'C', 'E', 'D', 'E', 'F']
vec3 = ['E', 'F', 'B', 'D', 'A', 'E', 'A', 'C', 'E', 'D', 'E', 'F', 'A', 'B', 'F', 'G']

# list of vector sequences from each of the original vectors

vec1seqs = [vec1[x:x + 3] for x in range(14)]
vec2seqs = [vec2[x:x + 3] for x in range(14)]
vec3seqs = [vec3[x:x + 3] for x in range(14)]

validSeqs = [1 for i in vec1seqs for j in vec2seqs for k in vec3seqs if (i + j + k).count('A') >= 3]

# can also solve problem for exactly three A's in selection
# validSeqs = [1 for i in vec1seqs for j in vec2seqs for k in vec3seqs if (i + j + k).count('A') == 3]

numSuccess = sum(validSeqs)

# there are 14^3 = 2744 possible selections of 9 items
print("The probability of finding three A's in the selection is {}/{} = {}".format(numSuccess, 2744, numSuccess/2744))