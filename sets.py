import random
from itertools import combinations

A1 = {1,5,7,9,10}
A2 = {1,2,3,8,9}
A3 = {2,4,6,8,9}
A4 = {2, 4, 8}
A5 = {3, 6, 7}
A6 = {3, 8, 10}
A7 = {4, 5, 7, 9}
A8 = {4, 5, 10}
A9 = {4, 6, 8}
A10 = {5, 6, 10}
A11 = {5, 8, 9}
A12 = {6, 7, 10}
A13 = {6, 8, 9}

ls = [A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13]

def largest_sets(possible_sets):
    max_ = 0
    largest_sets = []
    for I in possible_sets:
        current = 0
        for j in I:
            current += len(j)
        if current > max_:
            max_ = current
            largest_sets.append(I)
    return largest_sets

def check_intersection(set_, n):
    """
    Assumes lset to be a set of integers, e.g: {1, 2, 5}
    """
    combs = combinations(range(n), 2)

    #combs e.g: [(0,1), (0,2) ... ]
    for i in list(combs):
        first, second = i[0], i[1]
        inters = set_[first] & set_[second]
        if len(inters) != 0:
            return False
    return True

def main(ls, n):
    possible_sets = []
    all_sets = list(combinations(ls, n))
    for set_ in all_sets:
        if check_intersection(set_, n):
            possible_sets.append(set_)
    return possible_sets

for i in range(1,6):
    sets = main(ls, i)
    print(largest_sets(sets))



