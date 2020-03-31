s = str(input())
a = s.find('h', 0)
b = s.rfind('h', 0) + 1
print(s[:a], s[b:], sep='')
