fin = open('input.txt', encoding='utf8')
fin1 = fin.read().splitlines()
word = dict()
for c in fin1:
    word[c] = word.get(c, 0) + 1
max1 = 0
max2 = 0
for i in word:
    if int(word[i]) > max1:
        max1, max2 = int(word[i]), max1
    elif int(word[i]) > max2:
        max2 = int(word[i])
d = []
if max1 > sum(word.values()) / 2:
    for i in word:
        if int(word[i]) == max1:
            d.append((word[i], i))
else:
    for i in word:
        if int(word[i]) == max1 or int(word[i]) == max2:
            d.append((word[i], i))
d.sort(key=lambda d: (-d[0], d[1]))
s = set(d)
fin2 = open('output.txt', 'w', encoding='utf8')
if len(d) >= 2:
    for i in range(2):
        print(d[int(i)][1], file=fin2)
elif len(d) == 1:
    for i in range(1):
        print(d[int(i)][1], file=fin2)
