maxP = int(input())
P = int(input())
count = 0

for x in range(P):
    a = int(input())

for x in range(P):
    a += a
    count += 1
    if a >= maxP:
        print(count)
        break


    