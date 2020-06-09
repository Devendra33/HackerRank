#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    cnt1 = 0
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                str1 = 'LP'
            else:
                str1 = 'NLP'
        else:
            str1 = 'LP'
    else:
        str1 = 'NLP'
    print(str1) # contains LP or NLP
    if year == 1918:
        cnt = 26
        return (f'{cnt}.09.{year}')
    elif year == 1800 or year == 1700 or year == 1900:
        cnt = 12
        return (f'{cnt}.09.{year}')

    elif str1 == 'NLP':
        cnt1 = 13
        return (f'{cnt1}.09.{year}')
    else:
        cnt1 = 12
        return (f'{cnt1}.09.{year}')



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
