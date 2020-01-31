n = int(input())
bin = []

def binary_scale(n):
    while n:     
        bin.append(str(n%2)) # Save as str in list bin(for .join)
        n = n//2 # //를 사용하는 이유는 /만 사용할 경우 실수형(float)으로 저장되기 때문
    bin.reverse()
    print(''.join(bin))
binary_scale(n)