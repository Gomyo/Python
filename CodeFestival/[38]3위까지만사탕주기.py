l = list(map(int,input().split()))
count,third = 0,0
score = sorted(l,reverse=True)
for i in range(len(score)-1):
    if score[i] > score[i+1]:
        count += 1
        third += 1
    if third == 3:
        break
    elif score[i] == score[i+1]:
        count += 1
print(count)
