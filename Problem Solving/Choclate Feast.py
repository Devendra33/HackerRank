#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the chocolateFeast function below.
def chocolateFeast(cost, choc, wrap):
    c = cost//choc
    w = c
    tot_choc = c
    while w >= wrap:
        rwrap = w % wrap
        rchoc = w // wrap
        tot_choc += rchoc
        w = rwrap + rchoc
    return(tot_choc)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
