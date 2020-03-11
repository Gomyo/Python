# 너무 간단한 문제 ㅎㅎ
def solution(n):
    answer = []
    for i in range(n):
        answer.append('수') if i%2 == 0 else answer.append('박')
    return ''.join(answer)

# 하지만 python의 한계는 없다.
def water_melon(n):
    s = "수박" * n
    return s[:n]