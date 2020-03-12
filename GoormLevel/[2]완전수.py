# for문을 사용할 때에 depth를 잘 생각하자
# 왜인지 모르겠지만 제출했을 때 정답이었다가 오답이었다가 함. 실행 시간도 오래걸림!
a,b = map(int,input().split())
result = []

for i in range(a,b+1):
    yakList = []
    for j in range(1,i):
        if i%j == 0:
            yakList.append(j)
    if sum(yakList) == i:
        result.append(i)

for i in result:
    print(i, end=' ')
# 한줄풀이

a, b = map(int, input().split())
result = [x for x in range(a, b+1) if x == sum(y for y in range(1, x) if x % y == 0)]
for i in result:
    print(i, end=' ')

