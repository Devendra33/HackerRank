# Enter your code here. Read input from STDIN. Print output to STDOUT
m, base_set = input(), set(map(int, input().split()))
for i in range(0,int(input())):
    exec("base_set.{0}({1})".format(input().split()[0], set(map(int, input().split())) ))
print(sum(base_set))
