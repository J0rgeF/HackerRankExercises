def swap_case(s): # could use str.swapcase()
    st = ""
    for c in s:
        if c.isalpha():
            if c.islower():
                st += chr(ord(c) - 32)
            else:
                st += chr(ord(c) + 32)
        else:
            st += c
    return st

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)