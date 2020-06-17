#!/bin/python3

from math import sqrt
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    last = int(sqrt(b))
    cnt = 0
    print(last)
    for i in range(1,last+1):
        s = i**2
        print("s:",s)
        if s >= a and s <= b:
            cnt += 1

    return cnt



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
