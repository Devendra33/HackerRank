n = int(input("Enter number: "))
if n <= 10:
    print("Not a valid number, number should be greater than 10")
else:
    cnt = 0
    for num in range(10, n+1):
        lst = []
        temp = list(str(num))
        if len(temp) != len(set(temp)):
            cnt += 1
    print(cnt)
