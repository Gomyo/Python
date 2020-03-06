def solution(s):
    return ''.join(sorted(list(s),reverse=True))
#내 실수 : sorted는 애초에 리스트로 값을 반환하는
#함수이기에 list로 변환해줄 필요가 없다.
