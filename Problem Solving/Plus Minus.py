#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    l = len(arr)

    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        elif i == 0:
            zero += 1
    pos = pos/l
    neg = neg/l
    zero = zero/l

    print(f'{pos:.6}\n{neg:.6}\n{zero:.6}')

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
