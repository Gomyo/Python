vote = list(input().split())
count = 0
for i in range(len(vote)):
    if vote.count(vote[i-1]) < vote.count(vote[i]):
        count = i
print("{}이 총 {}표로 반장이 되었습니다.".format(vote[count],vote.count(vote[count])))