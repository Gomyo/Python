n = int(input())
a = 0

for x in range(n+1):
    if x%3 == 0 or x%5 == 0:
        a += x
print(a)
