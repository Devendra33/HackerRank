# Enter your code here. Read input from STDIN. Print output to STDOUT
def div(a,b):
    if b == 0:
        raise ZeroDivisionError ('Error Code: integer division or modulo by zero')
    else:
        print(a//b) 

n = int(input())


for _ in range(n):
    try:
        a,b = [int(x) for x in input().split()]
    except ValueError as v:
        print(f"Error Code: {v}")
        continue
    try:
        div(a,b)
    except ZeroDivisionError as e:
        print(e)
