#입력받는 것을 딕셔너리로
keys = input().split()
values = map(int,input().split())

r = dict(zip(keys,values))
print(r)