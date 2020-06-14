#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):
    alpha = []
    s = s.lower()
    for i in range(0,26):
        alpha.append(chr(97 + i))
    print(alpha)
    print(s)
    for i in s:
        if i in alpha:
            alpha.remove(i)
    if len(alpha) == 0:
        return 'pangram'
    else:
        return 'not pangram'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
