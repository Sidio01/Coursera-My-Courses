def myRange(n):
    i = 0
    while i < n:
        yield i**2
        i += 1


for i in myRange(10):
    print(i)
