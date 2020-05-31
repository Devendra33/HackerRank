import textwrap

def merge_the_tools(string, k):
    wrapper  = textwrap.TextWrapper(width = k)
    word_lst = wrapper.wrap(text = string)
    lst1 = []    

    for lst in word_lst:
        set_lst = [] ; j = 0

        for i in range(0,k):              
            if lst[i] not in set_lst:
                set_lst.append(lst[i])
                j += 1
        lst1.append(set_lst)     

    for j in lst1:
        print("".join(j))



