#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    min_cnt = 0
    max_cnt = 0
    min_val = scores[0]
    max_val = scores[0]

    for i in scores:
        if i > max_val:
            max_val = i
            max_cnt += 1
        elif i < min_val:
            min_val = i
            min_cnt += 1
    return (max_cnt, min_cnt)
    
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
