#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    keyboards.sort()
    drives.sort()
    keyboards.reverse()
    drives.reverse()
    max_cnt = 0
    if len(keyboards) >= len(drives):
        for i in keyboards:
            for j  in drives:
                if (i+j) > max_cnt and (i+j) <= b:
                    max_cnt = i+j
    else:
        for i in drives:
            for j  in keyboards:
                if (i+j) > max_cnt and (i+j) <= b:
                    max_cnt = i+j
    if max_cnt == 0:
        return -1
    else:
        return (max_cnt)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
