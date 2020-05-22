def average(array):

    lst  = list(set(array))
    set_len = len(lst)
    avg = sum(lst)/set_len
    return avg


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)