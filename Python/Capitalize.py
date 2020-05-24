

# Complete the solve function below.
def solve(s):
    lst = s.split(' ')
    lst1 = []
    for i in range(len(lst)):
        lst1.append(lst[i].capitalize())
    s = " ".join(lst1)
    return s
# direct function hota hai capitalize()
