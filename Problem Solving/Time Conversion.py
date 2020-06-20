#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    # print(s)
    str1 = ''
    lst = s.split(':')      # contains list of time separated by ':'
    
    lst1 = list(lst[2])
    str1 = lst1.pop(-2) + lst1.pop(-1)
    lst[2] = ''.join(lst1)

    if str1 == 'AM':
        if int(lst[0]) == 12:
            lst[0] = '00'
        else:
            pass

        return (':'.join(lst))

    else:
        if int(lst[0]) != 12:
            lst[0] = str((int(lst[0]) + 12))
        return (':'.join(lst))


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
