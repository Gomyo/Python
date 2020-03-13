a,cal,b = map(str,input().split())

a = int(a)
b = int(b)

def calculator(a,cal,b):
    if cal == "+":
        return a+b
    elif cal == "-":
        return a-b
    elif cal == "*":
        return a*b
    elif cal == "/":
        return "%.2f" % (a/b)

print(calculator(a,cal,b))
