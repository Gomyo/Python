n = int(input())

data = [[' ']*n for i in range(n)]

i,j = 0,-1 # 행과 열의 시작
s = 1 # 행과 열의 증감을 다루기 위한 변수

# 첫번째 줄 완성
for p in range(n):
        j = j + s
        data[i][j] = '#'
n -= 1

# 증감을 바꾸어가면서 배열 완성
while True:
    if n <= 0:
        break

    for p in range(n):
        i = i + s
        data[i][j] = '#'

    s = s * -1

    for p in range(n):
        j += s
        data[i][j] = '#'
    n -= 2

for i in range(len(data)):
    for j in range(len(data[0])):
        print(data[i][j],end=' ')
    print()
