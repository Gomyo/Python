import re

p = re.compile('[LVM]')
q = re.compile('[L]{2,5}')
result = []
count, L_count = 0, 0

with open("sample.txt") as f:#읽기 모드로 텍스트 파일 불러옴
    lines = f.readlines()
lines = [x.strip('\n') for x in lines]
f.close()

for i in lines:  # L,V,M이 포함된 경우에만 통과
    if p.match(i) == None:
        lines.remove(i)

for i in lines: # L이 2~5개인 경우만 통과
    if q.match(i) == None:
        lines.remove(i)

for i in lines: #5 종류의 문자로 이루어진 라인들로 리스트 형성
    if len(set(i)) != 5:
        lines.remove(i)

for i in lines: #최종결과출력
    print(i)



for i in lines:
    st = [m.start() for m in re.finditer('L',i)] #L이 몇번 위치에 있는지 반환하는 코드
    print(st)