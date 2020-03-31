from sys import stdin
import copy


class Matrix:
    def __init__(self, m=[]):
        self.m = m
        self.matrix = copy.deepcopy(m)
        self.a = m[0]

    def __str__(self):
        string = ""
        for i in self.matrix:
            for j in i:
                string = string + '%s\t' % j
            string = string[:-1] + '\n'
        return string[:-1]

    def size(self):
        return len(self.matrix), len(self.a)

    def __add__(self, other):
        for i in range(len(self.matrix)):
            b = len(self.matrix) - 1
            for j in range(len(self.a)):
                x = self.matrix[i][j]
                y = other.matrix[i][j]
                result = x + y
                print(result, end='\t')
            if i < b:
                print()
        return ''

    def __mul__(self, other):
        for i in self.matrix:
            a = self.matrix.index(i)
            b = len(self.matrix) - 1
            for j in i:
                result = j * other
                print(result, end='\t')
            if a < b:
                print()
        return ''

    __rmul__ = __mul__

m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
print(m1 + m2)
print(m1 + m1)
print(m2 + m2)
print(m1 + m2)
print(m1.size())
print(m2.size())
a = 5
b = 2.5
print(m1 * a)
print(m2 * a)
print(m1 * b)
print(m2 * b)
print(m1 * a)
print(m2 * a)
print(m1 * b)
print(m2 * b)
#exec(stdin.read())
