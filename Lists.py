if __name__ == '__main__':
    commands = []
    arr = []
    N = int(input())
    for i in range(0, N):
        commands.append(input())
    
    for c in commands:
        if c.split()[0] == "insert":
            arr.insert(int(c.split()[1]), int(c.split()[2]))
        elif c.split()[0] == "print":
            print(arr)
        elif c.split()[0] == "remove":
            arr.remove(int(c.split()[1]))
        elif c.split()[0] == "append":
            arr.append(int(c.split()[1]))
        elif c.split()[0] == "sort":
            arr = sorted(arr)
        elif c.split()[0] == "pop":
            arr.pop()
        elif c.split()[0] == "reverse":
            arr.reverse()