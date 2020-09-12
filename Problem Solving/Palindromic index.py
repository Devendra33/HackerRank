s = "baaa"
if s[::-1] == s:
    print(-1)
else:
    start = 0
    end = len(s) - 1
    while start <= len(s):
        if s[start] != s[end]:
            break
        start += 1
        end -= 1
    temp = s[:start] + s[start+1:]
    if temp == temp[::-1]:
        print(start)
    else:
        print(end)
