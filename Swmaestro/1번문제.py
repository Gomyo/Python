n = int(input())

# 주어진 조건 내에서 가장 큰 수를 만족하기 위해 획수가 각각 2,3인 값 1,7의 경우만 고려
def solution(n):
    result = 0
    onelist = []
    while True:
        if n == 0:
            break
        elif n != 3:
            onelist.append('1')
            n -= 2
        elif n ==3:
            onelist.append('7')
            n -= 3
    for i in onelist:
        # 가장 큰 수를 나타내기 위해 reverse
        a = ''.join(reversed(onelist))
    result += int(a)
    print(type(result))
    return result


print(solution(n))
