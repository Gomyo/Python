import datetime

a,b = map(int, input().split())
day = ['MON','TUE','WED','THU','FRI','SAT','SUN']

def yoil(a,b):
    return day[datetime.date(2020,a,b).weekday()]

print(yoil(a,b))