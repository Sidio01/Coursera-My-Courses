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


exec(stdin.read())
