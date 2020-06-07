#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    cnt_alice = 0
    cnt_bob = 0
    lst = []
    for i in range(len(a)):
        if a[i] > b[i]:
            cnt_alice += 1
        elif a[i] < b[i]:
            cnt_bob += 1
        else:
            pass
    lst.append(cnt_alice)
    lst.append(cnt_bob)
    return lst


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
