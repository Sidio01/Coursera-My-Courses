n = int(input())
s = list(map(int, input().split()))
b = s[0:n + 1]
b.sort()
print(*b)
