# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n = int(input())
# print(n)
dic =OrderedDict()
for _ in range(n):
    s = input()
    dic[s] = dic.get(s,0) + 1
print(len(dic))
for i in dic.keys():
    print(dic[i],end = " ")

