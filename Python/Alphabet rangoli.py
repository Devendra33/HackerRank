def print_rangoli(n):

    row_len = (n *4) - 3
    lst = []
    
    for i in range(n-1,-1,-1):
        lst.append(chr(97+i))
    # print(lst)   # gives output [e,d,b,c,a]
    
    lst1 = []
    lst1.append(lst[0])
    # print(lst1)  # gives output [e]
    
    for i in range(1,n):
        str1 = ''
        for j in range(0,i+1):
            str1 += lst[j]
        lst1.append(str1)
    
    # print(lst1)   #  gives output ['e', 'ed', 'edc', 'edcb', 'edcba']
    lst.clear()
    lst.append(lst1[0])
    str1 = ''
   
    for i in range(1,n):
        str1 += lst1[i]
        str1 += lst1[i][i - 1::-1]
        lst.append("-".join(str1))
        str1 = ''
    # print(lst)   # this contains all required alphabetical patterns!!

    for j in range(0,n):
        print(lst[j].center(row_len,'-'))
        if j == n-1:
            for k in range(n-2,-1,-1):
                print(lst[k].center(row_len,'-'))

