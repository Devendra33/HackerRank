from itertools import *

lst =  input().split(' ')
r = int(lst[1])
lst1 = []
for i in list(permutations(lst[0],r)):
    lst1.append(i)
lst1.sort()
for i in lst1:
    print("".join(i))


