def workbook(n, k, arr):
    lst = []
    for i in range(n):
        ele = arr[i]
        div = ele // k
        mod = ele % k
        inr = 1
        for _ in range(div):
            test = []
            for _ in range(k):
                test.append(inr)
                inr += 1
            lst.append(test)
        if mod != 0:
            test = []
            for _ in range(mod):
                test.append(inr)
                inr += 1
            lst.append(test)
    spe = 0
    ind = 1
    for item in lst:
        if ind in item:
            spe += 1
        ind += 1
    return spe