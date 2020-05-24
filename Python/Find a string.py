def count_substring(string, sub_string):
   # n and n+1 wali method se krna hai! (keshav method idea.)
    cnt = 0
    for i in range(0,len(string) - len(sub_string)+1):
        if string[i] == sub_string[0]:
            flag  = 1
            for j in range(0,len(sub_string)):
                if string[i+j] != sub_string[j]:
                    flag = 0
                    break
            if flag == 1:
                cnt = cnt +1

    return cnt


