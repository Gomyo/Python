# 정규표현식을 사용한 풀이
import re

n = int(input())
input_list = []
result = []
for x in range(n):
    x = input()
    input_list.append(x)

for i in input_list:
    m = re.findall('[aeiouAEIOU]',i)
    result.append("".join(m))

for i in result:
    print("???") if len(i) == 0 else print(i)
    
