s = '1234'

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

print(solution(s))