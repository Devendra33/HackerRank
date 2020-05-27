# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n = int(input())
dic = OrderedDict()
for i in range(n):
    lst = input().rpartition(" ")
    val = lst[2]
    str1 = lst[0]
    dic[str1] = dic.get(str1,0)+int(val)
for k in dic.keys():
    print(k,dic[k])
