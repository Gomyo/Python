def solution(n):
    base = ['A']*len(n)
    ans = 0
    n = list(n)
    idx = 0
    while True:
        rightidx = 1
        leftidx = 1
        if n[idx] != 'A':
            if ord(n[idx])-ord('A') >= 14:
                ans += 26 - (ord(n[idx])-ord('A'))
            else:
                ans += ord(n[idx])-ord('A')
            n[idx] = "A"
        if n == base:
            break
        else:
            for i in range(1,len(n)):
                if n[idx+i] == 'A':
                    rightidx+=1
                else:
                    break
                if n[idx-i] == 'A':
                    leftidx+=1
                else:
                    break
            if rightidx > leftidx:
                ans += leftidx
                idx -= leftidx
            else:
                ans += rightidx
                idx += rightidx
    return ans
