#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar, ar_count):
    cnt = 0
    num = max(ar)
    for i in ar:
        if i == num:
            cnt += 1
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar,ar_count)

    fptr.write(str(result) + '\n')

    fptr.close()
