# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
n_inp = set(input().split())
b = input()
b_inp = set(input().split())

res = n_inp.union(b_inp)
print(len(res))