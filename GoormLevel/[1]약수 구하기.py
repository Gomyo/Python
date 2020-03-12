# 정답!
n = int(input())
result = []

for x in range(1,n+1):
    if n%x == 0:
        result.append(x)
for i in result:
    print(i,end=' ')