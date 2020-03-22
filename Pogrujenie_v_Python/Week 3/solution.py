class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        file_path = self.file_path
        try:
            with open(file=file_path, mode='r', encoding='utf-8') as f:
                print(f.read())
                return f.read()
        except FileNotFoundError:
            print('Файл не найден. Укажите корректный путь к файлу')


a = FileReader('Dir\D.txt')
a.read()
b = FileReader('F.txt')
b.read()
c = FileReader('2.txt')
c.read()