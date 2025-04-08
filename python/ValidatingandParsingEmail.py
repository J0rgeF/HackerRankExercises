import re
import email.utils 

i = int(input())

for cnt in range(0, i):
    s = email.utils.parseaddr(input())
    if re.match(r'^([A-Za-z]|\d]){1}([A-z]|\d|[-]|[.])+[@]([A-Za-z]+)[.]([A-Za-z]{1,3})$', s[1]):
        print(email.utils.formataddr(s))