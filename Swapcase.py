def swap_case(s):
    str =""
    for c in s:
        if c.isupper():
            c = c.lower()
        else :
            c = c.upper()
        str += c        
    return str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
