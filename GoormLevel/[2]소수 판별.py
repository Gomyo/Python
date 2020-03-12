n = int(input())
def solution(n):   
    if n<2:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    m = round(n ** 0.5) + 1
    for i in range(3,m,2):
        if n%i == 0:
            return False
    return True

print(solution(n))
