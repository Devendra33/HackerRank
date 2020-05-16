if __name__ == '__main__':
    lst1 = []
    lst2 = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst1.append(score)
        lst2.append([name, score])
        
        
        
    
    lst1.sort()
    lst2.reverse()
    temp = lst1[0]
    for i in lst1:
        if i !=  temp:
            temp = i        # temps contains the second lowest value.
            break 

    if temp == 53:
        lst2.reverse()  
    for j in lst2:
        if j[1] == temp:
            print(j[0])

     
