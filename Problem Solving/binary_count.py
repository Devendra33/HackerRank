num = int(input("Enter a number:"))
print("Binary Representation: ", bin(num))
lst = []
for i in range(0, num+1):
    lst.append(list((bin(i)[2:])).count("1"))
print(lst)