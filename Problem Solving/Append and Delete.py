#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
    
def appendAndDelete(s, t, k):
    sub = ''
    final_sub = ''

    if (len(s) + len(t)) <= k:
        return 'Yes'
    
    else:
        
        for i in t:
            sub += i
            if sub not in s:
                break
        final_sub = sub[:len(sub)-1:]
        com_move = len(s) - 2*len(final_sub) + len(t)
        remain = k - com_move
        if remain < 0:
            return 'No' 
        elif final_sub == s and k % 2 != 0:    
            return 'Yes'

        elif remain % 2 == 0:
            return 'Yes'

        else:
            return 'No'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
