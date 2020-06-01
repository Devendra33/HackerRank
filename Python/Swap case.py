def swap_case(s):
    # yaha coding krni hai
    s1 =""
    for i in range(len(s)):
        if s[i] == s[i].upper():
            s1 += s[i].lower()
        else:
            s1 += s[i].upper()
    return s1

