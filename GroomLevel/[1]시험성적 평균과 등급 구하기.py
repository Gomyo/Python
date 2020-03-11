# 풀긴 풀었는데 왜 round로는 테스트 케이스 3을 통과하지 못했는지 이해가 가지 않음.
a, b, c = map(int, input().split())
avg = (a+b+c)/3

if avg >= 100:
    print(("%.2f" % avg), "A")
elif avg >= 90:
    print("%.2f" % avg, "A")
elif avg >= 80:
    print("%.2f" % avg, "B")
elif avg >= 70:
    print("%.2f" % avg, "C")
elif avg >= 60:
    print("%.2f" % avg, "D")
else:
    print("%.2f" % avg, "F")
