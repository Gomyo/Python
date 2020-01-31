def one(n):
    def two(value):
        sq = value ** n
        return sq
    return two
    
a = one(2)
print(a(20))