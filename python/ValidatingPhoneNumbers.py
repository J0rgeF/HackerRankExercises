import re

i = int(input())

for cnt in range(0,i):
    number = str(input())
    print('YES' if re.match('^[7-9][0-9]{9}$', number) else 'NO')