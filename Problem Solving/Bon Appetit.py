#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    # k that index that anna doesn't like
    # bill is the array of amount!
    # b = amount paid by anna 
    cnt = 0
    for i in range(len(bill)):
        if i == k:
            pass
        else:
            cnt += bill[i]
    b_actual = cnt//2
    over = b - b_actual
    if over == 0:
        print('Bon Appetit')
    else:
        print(over)

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
