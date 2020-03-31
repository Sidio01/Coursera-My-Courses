def CountSort(a):
    x = [0] * 101
    for j in a:
        x[j] += 1
    for y in range(len(x)):
        for i in range(x[y]):
            print(y, end=' ')
    return ''


n = list(map(int, input().split()))
print(CountSort(n))
