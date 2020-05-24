# Enter your code here. Read input from STDIN. Print output to STDOUT
m_no = int(input())
m = set(map(int, input().split()))
n_no = int(input()) 
n = set(map(int, input().split()))
# print(m,n)
lst1 = list(m.difference(n))
lst2 = list(n.difference(m))
lst1.extend(lst2)
lst1.sort()
for i in lst1:
    print(i)
