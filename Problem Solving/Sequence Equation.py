#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    l = len(p)+1
    lst1 = []
    # print(p) # [2, 3, 1]
    for i in range(1,l):
        p_ind = p.index(i) + 1
        ind_of_ind = p.index(p_ind) + 1
        lst1.append(ind_of_ind)
    return (lst1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
