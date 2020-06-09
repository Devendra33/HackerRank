#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):

    turn = 0
    # for starting logic!!
    lst  = [1]
    turn = 0
    for i in range(1,n):
        if len(lst) == 1 and p not in lst:
            lst.clear()
            lst.append(2)
            lst.append(3)
            turn += 1
        elif p not in lst :
            lst[0] = lst[1] + 1
            lst[1] = lst[1] + 2
            turn += 1
        else:
            break
# turn value from starting
# for reverse logic!

    lst.clear()
    lst = [n]
    turn1 = 0
    flag = 0
    for i in range(1,n):
        if n % 2 == 0:
            if len(lst) == 1 and p not in lst:
                lst.clear()
                lst.append(n-2)
                lst.append(n-1)
                turn1 += 1
            elif p not in lst:
                lst[0] = lst[0] - 2
                lst[1] = lst[1] - 2
                turn1 += 1
            else:
                break
        else:
            if flag == 0:

                lst.clear()
                lst.append(n-1)
                lst.append(n)
                flag = 1
                if p not in lst:
                    lst[0] = lst[0] - 2
                    lst[1] = lst[1] - 2
                    turn1 += 1

                else:
                    break

    if turn1 < turn:
        return (turn1)
    else:
        return (turn)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
