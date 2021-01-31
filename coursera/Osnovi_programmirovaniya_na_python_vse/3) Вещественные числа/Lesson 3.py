s = 'abcdef'
print(s[0])
print(len(s))
print(s[0:2])
print(s[3:])
print(s[:3])
print(s[::2])
u = 'abcd abc abd'
print(u.find('abd'))
pos = 0
while u.find('abc', pos) != -1:
    print(u.find('abc', pos))
    pos = u.find('abc', pos) + 1
