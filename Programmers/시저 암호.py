# 나의 풀이 38.5
def solution(s,n):
    a = ''
    for i in s:
        # 공백 처리
        if i == ' ':
            a += i
        elif ord(i) < ord('a') and (ord(i)+n) > ord('Z'):
            a += chr((ord(i)+n)-26)
        elif ord(i) >= ord('a') and (ord(i)+1) > ord('z'):
            a += chr((ord(i)+n)-26)
        else:
            a += chr(ord(i)+n)
    return a

# Ascii를 이용한 풀이 (통과)
from string import ascii_lowercase
from string import ascii_uppercase

lowerList = list(ascii_lowercase)
upperList = list(ascii_uppercase)

def solution(s,n):
    a = ''
    for i in s:
        if i == ' ':
            a += i
        elif i in lowerList and (lowerList.index(i)+n) > 25:
                a += lowerList[(lowerList.index(i)+n)-26]
        elif i in upperList and (upperList.index(i)+n) > 25:
                a += upperList[(upperList.index(i)+n)-26]
        else:
            a += chr(ord(i)+n)
    return a

# 다른 사람의 풀이

def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)