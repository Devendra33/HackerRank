# Enter your code here. Read input from STDIN. Print output to STDOUT
lst = list(map(int,input().split()))   # contains lst[0]: contains no. of elements in                                              orginal lst/
                                        # lst[1]:(m) num of elements in sets A & B. 
# print(lst)
org_lst = list(map(int,input().split()))
# print(org_lst)
A = set(map(int,input().split()))
B = set(map(int, input().split()))
# print(A,B)
cnt = 0
for i in org_lst:
    
    if i in A and i in B:
        pass
    elif i in A:
        cnt += 1
    elif i in B:
        cnt -= 1
print(cnt)
     
