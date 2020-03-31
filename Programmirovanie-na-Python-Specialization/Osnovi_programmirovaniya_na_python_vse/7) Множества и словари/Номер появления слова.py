fin = open('input1.txt')
fin1 = fin.read().split()
word = dict()
for c in fin1:
    word[c] = word.get(c, 0) + 1
    print(word[c] - 1, end=' ')
