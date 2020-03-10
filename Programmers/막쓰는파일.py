s = '-1234'

# 나의 풀이
def solution(s):
    if s[0] == '-':
        return -int(s[1:])
    elif s[0] == '+':
        return int(s[1:])
    else:
        return int(s)

# 다른 사람의 풀이
def strToInt(str):
    result = 0

    for idx, number in enumerate(str[::-1]):
        if number == '-':
            result *= -1
        else:
            result += int(number) * (10 ** idx)

    return result

