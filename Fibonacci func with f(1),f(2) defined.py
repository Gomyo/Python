def fibo(n):
    if n == 0:
        pass
    elif n == 1: #fibo(1)의 값 지정
        return 4
    elif n == 2: #fibo(2)의 값 지정
        return 7
    elif (n>2):
        return fibo(n-1) + fibo(n-2)

print(fibo(10))