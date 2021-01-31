fin = open('input.txt')
fin1 = fin.read().split()
word = dict()
for c in fin1:
    word[c] = word.get(c, 0) + 1
a = 0
for i in word:
    if int(word[i]) > a:
        a = int(word[i])
d = []
for i in word:
    if int(word[i]) == a:
        d.append(i)
d.sort()
print(d[0])
