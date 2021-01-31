fin = open('input3.txt')
fin1 = fin.read().split()
word = dict()
for c in fin1:
    word[c] = word.get(c, 0) + 1
a = []
for i in word:
    a.append((word[i], i))
a.sort(key=lambda a: (-a[0], a[1]))
for i in range(len(a)):
    print(a[i][1])
