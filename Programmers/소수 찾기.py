# 소수 찾는 함수 구현 
# 모든 수로 나누어 보기 때문에 한 개의 소수만 판별할 때는 괜찮지만 범위의 소수를 구할 때는 비효율적이라 시간 초과가 된다.
def is_Prime(num):
    if num != 1:
        for f in range(2,num):
            if num % f == 0:
                return False
    else:
        return False
    return True

def solution(n):
    result = 0
    for x in range(1,n+1):
        if is_Prime(x) == True:
            result += 1
    return result     

# 에라토스테네스의 체를 이용해 간략화
def solution(n):
    # 에라토스테네스의 체 초기화: n개를 True로 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i = sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2,m+1):
        if sieve[i] == True: # i가 소수인 경우
            for j in range(i*2,n,i): # i의 배수는 모두 False
                sieve[j] = False
    return len([i for i in range(2,n) if sieve[i] == True])
    

# 다른 사람의 풀이. 실행은 통과하지만 제출하면 0점
def solution(n):
    # 연산을 위해 list를 set 형으로 변환
    a = set([i for i in range(3,n+1,2)])
    for i in range(3,n+1,2):
        if i in a:
            a -= set([i for i in range(i*2,n+1,i)])
        # result에 2를 추가
        return len(a)+1

# 다른 사람의 코드 (차집합을 사용)
def solution(n):
    num = set(range(2,n+1))
    
    for i in range(2,n+1):
        if i in num:
            num -= set(range(i*2,n+1,i))
    return len(num)