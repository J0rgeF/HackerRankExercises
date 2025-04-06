import textwrap

def wrap(string, max_width):
    # Without using textwrap library:
    #strn = [None]*int(len(string)+(len(string) / max_width))
    #i = 0
    #cnt = 0
    #while i != len(strn):
        #if (i + 1) % (max_width + 1) == 0:
            #strn[i] = '\n'
        #else:
            #strn[i] = string[cnt]
            #cnt +=1
        #i+=1
    #return ''.join(strn)
    # Using textwrap library:
    return textwrap.fill(string, max_width)
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)