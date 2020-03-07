s = '1234'

# 실패! 87.5 / 100.0
def solution(s):
    ls = len(s)
    if ls == 4 or 6:
        try:
            int(s)
            return True
        except ValueError:
            return False
    else:
        return False 

# 성공! 4 or 6으로 하면 안되는구나..왜일까?
def solution(s):
    ls = len(s)
    if ls == 4 or ls == 6:
        try:
            int(s)
            return True
        except ValueError:
            return False
    else:
        return False 

#다른 사람의 풀이

def solution(s):
    return s.isdigit() and len(s) in (4, 6)