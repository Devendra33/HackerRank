# Enter your code here. Read input from STDIN. Print output to STDOUT
a = input()
a_inp = set(input().split())
b = input()
b_inp = set(input().split())

res = a_inp.symmetric_difference(b_inp)
print(len(res))
