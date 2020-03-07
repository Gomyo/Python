array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

#에러로 통과 안된 코드
def solution(array, commands):
    result = []
    for x in range(3):
        a = sorted(array[commands[x][0]-1:commands[x][1]])[commands[x][2]-1]
        result.append(a)
    return result

#통과한 코드 (commands의 길이를 자유롭게 해둠)
def solution(array, commands):
    result = []
    for x in range(len(commands)):
        result.append(sorted(array[commands[x][0]-1:commands[x][1]])[commands[x][2]-1])
    return result