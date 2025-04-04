import numpy
a = input()
coeficents = []
i = 0
a = a.split(' ');
for b in a:
    coeficents.append(float(b))
x = float(input())
print(numpy.polyval(coeficents, x))
