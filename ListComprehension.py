import math

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    coordinates = [x, y ,z]
    cp = [[a, b, c] for a in range(x + 1) for b in range(y + 1) for c in range(z + 1)]
    
    cpn = [d for d in cp if sum(d) != n]
    print(cpn)
