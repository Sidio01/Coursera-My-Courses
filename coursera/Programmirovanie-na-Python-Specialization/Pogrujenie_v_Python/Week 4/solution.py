import os.path
import tempfile


class File:
    def __init__(self, file_path):  # Готово
        self.file_path = file_path
        try:
            with open(file=self.file_path, mode='r') as f:
                self.rl = f.read().splitlines()
                self.len_rl = len(self.rl)
                print(self.rl)
        except FileNotFoundError:
            f = open(file=self.file_path, mode='tw+', encoding='utf-8')
            self.rl = f.read().splitlines()
            self.len_rl = len(self.rl)
            f.close()

    def __str__(self):  # Готово
        return os.path.realpath(self.file_path)

    def __add__(self, other):
        f1 = open(file=self.file_path, mode='r')
        f1r = f1.read()
        f2 = open(file=other.file_path, mode='r')
        f2r = f2.read()
        new_file = File(os.path.join(tempfile.gettempdir(), '1.txt'))  # Проверить название файла
        new_file_writer = open(file=new_file.file_path, mode='tw+', encoding='utf-8')
        new_file_writer.write(f1r)
        # new_file_writer.write('\n')
        new_file_writer.write(f2r)
        f1.close()
        f2.close()
        new_file_writer.close()
        return new_file

    def __iter__(self):  # Готово
        return self

    def __next__(self):  # Готово
            if self.len_rl > 0:
                next_elem = self.rl[-self.len_rl]
                self.len_rl -= 1
                return next_elem
            else:
                raise StopIteration

    def read(self):  # Готово
        with open(file=self.file_path, mode='r') as f:
            return f.read()

    def write(self, new_str):  # Готово
        with open(file=self.file_path, mode='w') as f:
            return f.write(new_str)


# a = File('N:\P\PycharmProject\Week 4\h.txt')
# b = File('N:\P\PycharmProject\Week 4\w.txt')
# print(os.path.exists('N:\P\PycharmProject\Week 4\h.txt'))
# print(os.path.exists('N:\P\PycharmProject\Week 4\j.txt'))
# print(a, b, sep='\n')
# print()
# print(b.read())
# a.write('Hello!' '\n' '123' '\n' '456')
# print()
# c = a + b
# print(type(a))
# print(type(b))
# print(type(c))
# print(a.read())
# print(a + b)
# iter(a)
# next(a)
# next(a)
# next(a)
# for _ in a:
#     print(_)
