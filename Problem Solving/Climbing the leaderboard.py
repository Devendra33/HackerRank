#!/bin/python3

import math
import os
import random
import re
import sys
from collections import OrderedDict 
# Complete the climbingLeaderboard function below.

def climbingLeaderboard(scores, alice):
    new_lst = list(reversed(sorted(set(scores))))
    print(new_lst)
    i = len(alice) - 1
    j =0
    lst = []
    while i >= 0:
        if j >= len(new_lst) or new_lst[j] <= alice[i]:
            lst.append(j+1)
            i-=1
        else:
            j += 1
    return reversed(lst)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
