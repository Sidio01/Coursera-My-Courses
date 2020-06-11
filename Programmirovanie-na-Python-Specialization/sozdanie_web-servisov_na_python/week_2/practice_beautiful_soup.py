from bs4 import BeautifulSoup
import unittest
import lxml


def parse(path_to_file):
    html = open(path_to_file, 'r', encoding='utf-8')
    soup = BeautifulSoup(html, 'lxml')
    # Поместите ваш код здесь.
    # ВАЖНО!!!
    # При открытии файла, добавьте в функцию open необязательный параметр
    # encoding='utf-8', его отсутствие в коде будет вызвать падение вашего
    # решения на грейдере с ошибкой UnicodeDecodeError
    # return [imgs, headers, linkslen, lists]
    return soup


# class TestParse(unittest.TestCase):
#     def test_parse(self):
#         test_cases = (
#             ('wiki/Stone_Age', [13, 10, 12, 40]),
#             ('wiki/Brain', [19, 5, 25, 11]),
#             ('wiki/Artificial_intelligence', [8, 19, 13, 198]),
#             ('wiki/Python_(programming_language)', [2, 5, 17, 41]),
#             ('wiki/Spectrogram', [1, 2, 4, 7]),)
#
#         for path, expected in test_cases:
#             with self.subTest(path=path, expected=expected):
#                 self.assertEqual(parse(path), expected)
#
#
# if __name__ == '__main__':
#     unittest.main()

a = parse('/home/sidio01/PycharmProjects/Coursera-My-Courses/Programmirovanie-na-Python-Specialization/sozdanie_web'
          '-servisov_na_python/week_2/wiki/Stone_Age')
print(a)
b = parse('task.txt')
print(b)
