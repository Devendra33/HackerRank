#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    odeve = 0
    for i in range(-1,-len(c)-1,-1):
        if c[i] == 1:
            break
        else:
            odeve += 1
    print(odeve)
    ind = 0
    jump = 0
    ind_range = len(c)-3
    print(c)
    for _ in range(len(c)-1):
        if ind <= ind_range:
            if c[ind+1] == 1:
                ind += 2
                jump += 1
            elif c[ind+1] == 0 and c[ind+2] == 0:
                ind += 2
                jump += 1
            elif c[ind+1] == 0 and c[ind+2] == 1:
                ind += 1
                jump += 1

        else:
            break
    if odeve % 2 == 0:
        return jump+1
    else:
        return jump

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
