#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#

def diagonalDifference(arr):
    sum_d1 = 0
    sum_d2 = 0
    n1 = n - 1
    for i in range(n):
        sum_d1 += arr[i][i]

    for i in range(n): 
        sum_d2 += arr[n1-i][i]
    return abs(sum_d1-sum_d2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
