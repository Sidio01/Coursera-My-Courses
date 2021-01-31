def persistence(num):
    result = 0
    while num >= 9:
        a = []
        for i in str(num):
            a.append(int(i))
        length = len(a)
        x = 1
        for i in range(length):
            x *= a[i-1]
        num = x
        result += 1
    return result

persistence(39)
persistence(4)
persistence(25)
persistence(999)
