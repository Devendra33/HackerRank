if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())

    def runner(arr):
        arr.sort()
        arr.reverse()
        m = max(arr)
        for i in arr:
            if i < m:
                return(i)
            
    res = runner(arr)
    print(res)

     

    
