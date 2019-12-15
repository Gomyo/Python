import re


p = re.compile('[LVM]')

match_list, count_list, result = [],[],[]

count, L_count = 0, 0


with open("sample.txt") as f:#읽기 모드로 텍스트 파일 불러옴
    lines = f.readlines()
lines = [x.strip('\n') for x in lines]
f.close()

for i in lines:  #L,V,M이 포함되지 않은 경우 삭제
    if p.match(i) == None:
        lines.remove(i)



for i in lines: #5 종류의 문자로 이루어진 라인들로 리스트 형성
    for j in range(len(i)):
        if i[j] in count_list:
            pass
        else:
            count_list.append(i[j])
            count+=1
        
    if count == 5:
        match_list.append(i)
    count = 0
    count_list = []

for i in match_list:
    ct = re.findall('L',i)  #L이 2~5개인 경우를 반환
    if len(ct) >=2 and len(ct)<=5:
        result.append(i)


for i in result: #최종결과출력
    print(i)



for i in match_list:
    st = [m.start() for m in re.finditer('L',i)] #L이 몇번 위치에 있는지 반환하는 코드
    print(st)
    if len(ct) >=2 and len(ct)<=5:
        result.append(i)
        

    
