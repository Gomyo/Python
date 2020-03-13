
def solution(p,l):
    ans = 0
    m = max(p)
    while True:
        ptd = p.pop(0)
        if ptd == m:
            ans += 1
            if l == 0:
                break
            else:
                l -= 1
            m = max(p)
        else:
            p.append(ptd)
            if l == 0:
                l = len(p)-1
            else:
                l -= 1
    return ans