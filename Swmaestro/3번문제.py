# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n,k = map(int,input().split())
arr = list(map(int,input().split()))

def solution(n,k,arr):
    # 가장 큰 수부터 횟수가 허락하는 한, 제거
	# 그러나 이렇게 풀면 4,4,4,40,41에 K=2와 같은 경우는 통과하지 못함. 그럼 어떻게 해야 할까?
    result = 0
    while k > 1:
        for x in range(n):
            if max(arr[:x])-min(arr[:x]) <= max(arr[x:]) - min(arr[:x]):
                continue
            elif max(arr[:x])-min(arr[:x]) > max(arr[x:]) - min(arr[:x]):
                result += max(arr[x:]) - min(arr[:x])
            if k == 1:
                result += max(arr[:x])-min(arr[:x])
        k -= 1
    return result

print(solution(n,k,arr))