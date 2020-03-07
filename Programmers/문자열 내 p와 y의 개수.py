

# 정규표현식... Thank you, Prof.Ma!
import re
def solution(s):
    ps = len(re.findall('[pP]',s))
    ys = len(re.findall('[yY]',s))
    if ps == ys:
        result = True
    else:
        result = False
    return result

# count를 활용한 아주 간단한 답
def numPY(s):
    return s.lower().count('p') == s.lower().count('y')

# Collections 모듈의 Counter를 사용한 코드
from collections import Counter
def numPY(s):
    # 함수를 완성하세요
    c = Counter(s.lower())
    return c['y'] == c['p']