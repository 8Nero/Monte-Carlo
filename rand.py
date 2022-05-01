from itertools import permutations
from random import randrange

def perm():
    array2 = list(range(1,44))
    permutations(array2)

    return array2

def sample(n):
    array2 = []
    for i in range(n):
        array2.append(randrange(1, 44))
    return array2

val = input("Sampling - 1\ Permutations - 0\n")

if int(val):
    print(sample(5))
else:
    print(perm())

