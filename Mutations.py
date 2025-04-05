def mutate_string(string, position, character):
    m = list(string)
    m[position] = character
    return ''.join(m)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)