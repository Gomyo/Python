# 42m 3.56s
# lambda를 이용한 방식
def solution(strings, n):
    # n번째 index를 기준으로 정렬하되 해당 값이 동일하다면 전체를 비교해 정렬
    return sorted(strings, key=lambda x: (x[n],x)

# n번째 수를 글자에 앞에다 붙이고 정렬하는 방식(Wow)
def solution(strings, n):
    answer = []
    for i in range(len(strings)):
        # 특정 index의 문자를 앞에 붙이고 정렬한 뒤,
        strings[i] = strings[i][n]+strings[i] 
    strings.sort()

    for j in range(len(strings)):
        # index[1]부터 answer에 포함하기
        answer.append(strings[j][1:])
    return answer