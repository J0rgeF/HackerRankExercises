if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    a = set(arr)
    a1 = sorted(a, reverse=True)
    print(a1[1])