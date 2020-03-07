arr = [4,4,4,3,3]

#모든 case 통과했지만 효율성 0점
def solution(arr):
    x = 0
    while x < len(arr)-1: # 삭제가 이루어 질 때마다 len(arr)의 길이는 1 줄어들기 때문에, 최소한의 길이는 1이 되어야 하므로 x는 arr의 길이보다 1 작아야 함 
        if arr[x] == arr[x+1]:
            del arr[x+1]
            print(arr) #확인용
        else:
            x += 1
            print(arr) #확인용
    return arr


#케이스 17만 실패. 95.8 / 100.0
def solution(arr):
    result = []
    x = 0
    while x < len(arr)-1:
        if arr[x] != arr[x+1]:
            if arr[x] not in result:
                result.append(arr[x])
            result.append(arr[x+1])
            print(result)
            x += 1
        else:
            x += 1
    return result

#통과
def solution(arr):
    result = []
    result.append(arr[0])
    x = 0
    while x < len(arr)-1:
        if arr[x] != arr[x+1]:
            result.append(arr[x+1])
            x += 1
        else:
            x += 1
    return result

#for문을 이용한 풀이 - 런타임 에러
def solution(arr):
    result = []
    result.append(arr[0])
    for i in arr:
        if arr[i] != arr[i+1]:
            result.append(arr[i])
    return result

#가장 빠른 풀이
def solution(arr):
    result = []
    for i in arr:
        if result[-1:] == [i]: continue
        result.append(i)
    return result