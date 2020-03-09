s = "AB"

a = ''
for i in s:
    a += chr(ord(i)+1)
print(a)