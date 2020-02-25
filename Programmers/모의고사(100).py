def solution(answers):

    pickPatternArray = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    scoreArray = [0,0,0]

    result = []

    for idx, ans in enumerate(answers):
        for i in range(3):
            if ans == pickPatternArray[i][idx%len(pickPatternArray[i])]:
                scoreArray[i] += 1

    for idx, score in enumerate(scoreArray):
        if score == max(scoreArray):
            result.append(idx+1)

    return result
