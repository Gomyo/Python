# 나의 풀이
def solution(n):
    a = 0
    for x in range(1,n+1):
        if n%x == 0:
            a += x
    return a

# 다른 사람의 풀이 
def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상잼
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])

# Using lambda
def sumDivisor(num):
    return sum(filter(lambda x: num % x == 0, range(1, num + 1)))