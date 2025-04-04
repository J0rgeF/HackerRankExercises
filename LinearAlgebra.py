import numpy

n = int(input())
l = []

for i in range(0,n):
    d = []
    b = input()
    b = b.split(' ');
    for c in b:
        d.append(float(c))
    l.append(d)

print(round(numpy.linalg.det(l), 2))
