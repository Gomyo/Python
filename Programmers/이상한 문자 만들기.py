# 문제를 풀면서 간과한 점 : 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야 한다는 것. 문제를 잘 읽자.
# 예시가 되더라도 채점이 안 될 경우, 테스트 케이스로 "sp ace" -> "Sp AcE"가 되는지 확인해 보자.
# 나의 풀이
def solution(s):
    sList = s.split(' ')
    a = []
    for i in sList:
        s = ''
        for j in range(len(i)):
            s += i[j].upper() if j % 2 == 0 else i[j].lower()
        a.append(s)
    return ' '.join(a)

# lambda를 이용한 풀이
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))
