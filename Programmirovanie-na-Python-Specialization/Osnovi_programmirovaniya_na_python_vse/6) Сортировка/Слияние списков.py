def merge(a, b):
    d = a + b
    c = []
    i = 0
    z = len(d)
    while i < z:
        y = min(d)
        d.remove(y)
        c.append(y)
        i += 1
    return c

#     c = a + b
#     d = 0
#     i = 0
#     while i < len(c):
#         d = 0
#         while d < (len(c) - 1):
#             if c[d] > c[d + 1]:
#                 c[d], c[d + 1] = c[d + 1], c[d]
#             d += 1
#         i += 1
#     return c


a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*merge(a, b))
