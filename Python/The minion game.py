def get_result(vc, strlen):
    cnt = 0
    for i in vc:
        cnt += strlen - i
    return cnt
    
def get_indexs(vc,string):

    vcl = []
    for i in vc:
        j = string.find(i,0)
        while j != -1:
            vcl.append(j)
            j = string.find(i,j+1)
    return vcl
    

def minion_game(string):
    str1 = 'AEIOU'
    vow = []
    con = []
    strlen = len(string)    # Len of the given strings
    # print(strlen)
    str2 = list(set(string))
    for i in str2:       
        if i in str1:
            vow.append(i)
        else:
            con.append(i)
    # print(vow)        # vow contains all vowels in the string.
    # print(con)        # con contains all consonents in the string.
    ind_vow = get_indexs(vow, string)
    # print(ind_vow)
    ind_con = get_indexs(con, string)
    # print(ind_con) 
    res_vow = get_result(ind_vow, strlen)
    res_con = get_result(ind_con, strlen)
    # print(f'vow: {res_vow}')
    # print(f'con: {res_con}')

    
    if  res_con > res_vow  :
        print(f'Stuart {res_con}')
    elif res_con < res_vow:
        print(f'Kevin {res_vow}')
    elif res_con ==  res_vow:
        print('Draw')  


