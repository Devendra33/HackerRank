#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    setlst = list(set(a))
    dis = []
    for  i  in setlst:
        if a.count(i) >= 2:
            s1 = a.index(i)  # 1st index value
            s2 = a.index(i,s1+1,len(a))   # 2nd index value
            dis.append(s2-s1)
    if len(dis) == 0:
        return -1
    else:
        return min(dis)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
