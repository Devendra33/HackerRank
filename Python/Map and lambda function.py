cube = lambda x: x**3

# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    lst = [0,1]
    f1 = 0
    f2 = 1
    if n == 0:
        return []
    elif n == 1:
        return [0]
    else:
        for _ in range(n - 2):
            f = f1+f2
            lst.append(f)
            f1 = f2
            f2 = f

        return lst

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))