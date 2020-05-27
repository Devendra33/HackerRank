# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

n = int(input())
lst = list(map(int, input().split()))
cus = int(input())          
lst_cus = []
for i in range(cus):
    lst_cus.append(list(map(int,input().split())))

dic  = Counter(lst)    
cnt = 0

for  i in  range(cus):
    for j in range(1):

        if dic[lst_cus[i][j]] != 0:
            cnt += lst_cus[i][j+1]
            dic[lst_cus[i][j]] -= 1
print(cnt)
