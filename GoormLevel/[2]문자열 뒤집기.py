# # for문을 사용한 것
n = str(input())

for x in range(-1,-(len(n)+1),-1):
    print(n[x],end='')

# join과 reversed를 사용한 것
n = str(input())

print(''.join(reversed(n)))
