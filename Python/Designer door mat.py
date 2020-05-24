# Enter your code here. Read input from STDIN. Print output to STDOUT


s = input()
lst = s.split();
n = int(lst[0])
m = int(lst[1])

s= ['.|.','WELCOME'] 
n1 = (n-1)//2

for i in range(1,2*n1, 2):
    print((s[0]*i).center(m, '-'))

print(s[1].center(m,'-'))

for i in range(((2*n1)-1), 0,-2):
    print((s[0]*i).center(m, '-'))

