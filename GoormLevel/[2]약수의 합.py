n = int(input())

def solution(n):
    result = []
    for x in range(1,n+1):
        if n%x == 0:
            result.append(x)
    return sum(result)

print(solution(n))