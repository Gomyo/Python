def solution(answers):
    answer = []
    # Let me use Index / Slice
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    
    # Create 3 of var
    ac, bc, cc = 0, 0, 0
    
    for i in range(len(answers)):
        if answers[i] == a[i%5]:
            ac += 1
        if answers[i] == b[i%8]:
            bc += 1
        if answers[i] == b[i%10]:
            cc += 1
            
    if ac >= bc and ac >= cc:
        answer.append(1)
    if bc >= ac and bc >= cc:
        answer.append(2)
    if cc >= ac and cc >= bc:
        answer.append(3)
        
    return answer
