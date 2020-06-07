#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    cnt  = 0
    v  = 0
    for i in s:
        if i == 'U':
            if cnt == -1:
                v += 1
            cnt += 1
        elif i == 'D':
            cnt -= 1
    return(v) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
