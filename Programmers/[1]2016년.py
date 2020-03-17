def solution(a, b):

    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    date = ['FRI','SAT','SUN','MON','TUE','WED','THU']

    result = b-1 

    for i in range(a-1):
        result += month[i]

    return date[result%7] #date 길이로 나눔
