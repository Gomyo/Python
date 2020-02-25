def solution(answers):
    answer = []
    
    # Let me use Index / Slice
    a = [1,2,3,4,5] * 2000
    b = [2,1,2,3,2,4,2,5] * 1250
    c = [3,3,1,1,2,2,4,4,5,5] * 1000
    
    # Create 3 of var
    ac, bc, cc = 0, 0, 0
    
    for i in range(len(answers)):
        if answers[i] == a[i]:
            ac += 1
        if answers[i] == b[i]:
            bc += 1
        if answers[i] == b[i]:
            cc += 1
            
    if ac >= bc and ac >= cc:
        answer.append(1)
    if bc >= ac and bc >= cc:
        answer.append(2)
    if cc >= ac and cc >= bc:
        answer.append(3)
        
    return answer
