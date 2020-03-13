import math
n,k = map(int,input().split())
array = list(map(int, input().split()))


def solution(n,k):
    count = 1
    count += math.ceil(len(array[k:])/(k-1))
    return count

print(solution(n,k))
