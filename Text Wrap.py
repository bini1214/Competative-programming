import textwrap

def wrap(string, max_width):
    str = ""
    for i in range (0,len(string),max_width) :
        str += string[i:i+int(max_width)]+'\n'
    return str

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
