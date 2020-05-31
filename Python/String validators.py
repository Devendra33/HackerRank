if __name__ == '__main__':
    s = input()

def al_num(s):
    for i in s:
        if i.isalnum():
            return True
    else:
        return False
def alpha(s):
    for i in s:
        if i.isalpha():
            return True
    else:
        return False
def digit(s):
    for i in s:
        if i.isdigit():
            return True
    else:
        return False

def lower(s):
    for i in s:
        if i.islower():
            return True
    else:
        return False
def upper(s):
    for i in s:
        if i.isupper():
            return True
    else:
        return False


def validate(s):
    print(al_num(s))  #1.alphanumeric   
    print(alpha(s))  #2.alphabetical  
    print(digit(s))  #3.digits. 
    print(lower(s))  #4.lowercase characters.  
    print(upper(s))  #5.uppercase characters.

     

validate(s)
