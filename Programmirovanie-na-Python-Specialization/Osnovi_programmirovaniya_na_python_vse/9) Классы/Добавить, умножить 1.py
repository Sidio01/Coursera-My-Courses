from sys import stdin
from copy import deepcopy


class MatrixError(BaseException):
    def __init__(self, Matrix, other):
        self.matrix1 = Matrix
        self.matrix2 = other


class Matrix():
    def __init__(self, matrix):
        self.matrix = deepcopy(matrix)

    def __str__(self):
        string = ''
        for i in self.matrix:
            for j in i:
                string += '%s\t' % j
            string = string[:-1]
            string += '\n'
        string = string[:-1]
        return string

    def size(self):
        rows = len(self.matrix)
        cols = 0
        for row in self.matrix:
            if len(row) > cols:
                cols = len(row)
        return (rows, cols)

    def __getitem__(self, idx):
        return self.matrix[idx]

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix):
            lenght = len(self.matrix[0])
            for row in self.matrix:
                if len(row) != lenght:
                    raise MatrixError(self, other)
            for row2 in other.matrix:
                if len(row2) != lenght:
                    raise MatrixError(self, other)
            result = []
            numbers = []
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    summa = other.matrix[i][j] + self.matrix[i][j]
                    numbers.append(summa)
                    if len(numbers) == len(self.matrix[0]):
                        result.append(numbers)
                        numbers = []
            return Matrix(result)
        else:
            raise MatrixError(self, other)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            result = [[other * j for j in i] for i in self.matrix]
            return Matrix(result)

    __rmul__ = __mul__

    def transpose(self):
        transMatrix = list(zip(*self.matrix))
        self.matrix = transMatrix
        return Matrix(transMatrix)

    def transposed(self):
        transMatrix = list(zip(*self.matrix))
        return Matrix(transMatrix)


exec(stdin.read())
