def solution(s):
    lens = len(s)
    pivot = lens//2
    if lens%2 == 0:
        answer = s[pivot-1]+s[pivot]
    else:
        answer = s[pivot]
    return answer