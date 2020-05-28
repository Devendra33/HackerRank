# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import *
d = deque()
n = int(input())
# append, pop, popleft and appendleft
for i in range(n):
    v = ''
    str1 = input().rstrip().lstrip()
    if " " in str1:
        w,v = str1.split(" ")
    else:
        w = str1
    # print(w,v)
    if w == 'append':
        d.append(v)
    elif w == 'appendleft':
        d.appendleft(v) 
    elif w == 'pop':
        d.pop()
    elif w == 'popleft':
        d.popleft()
    else:
        pass
for j in d:
    print(j,end = " ")

