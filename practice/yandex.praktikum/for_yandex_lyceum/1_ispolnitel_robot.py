"""
Напишите класс Robot, который инициализируется с начальными координатами – положением Робота на 
плоскости, обе координаты заключены в пределах от 0 до 100.

Робот может передвигаться на одну клетку вверх (N), вниз (S), вправо (E), влево (W). Выйти за 
границы плоскости Робот не может.

Метод move() принимает строку – последовательность команд перемещения робота, каждая буква строки 
соответствует перемещению на единичный интервал в направлении, указанном буквой. Метод возвращает 
кортеж координат – конечное положение Робота после перемещения.

Метод path() вызывается без аргументов и возвращает список кортежей координат точек, по которым 
перемещался Робот при последнем вызове метода move. Если метод не вызывался, возвращает список с 
одним кортежем – начальным положением Робота.
"""


class Robot:
    def __init__(self, coordinate):
        self.coordinate = coordinate
        self._path = [(self.coordinate[0], self.coordinate[1])]
        self.x = self.coordinate[0]
        self.y = self.coordinate[1]

    def move(self, path):
        move_path = list(path)
        for i in move_path:
            if i in ('N', 'S'):
                if i == 'N':
                    if self.y < 100:
                        self.y += 1
                        self._path.append((self.x, self.y))
                    else:
                        self._path.append((self.x, self.y))
                else:
                    if self.y > 0:
                        self.y -= 1
                        self._path.append((self.x, self.y))
                    else:
                        self._path.append((self.x, self.y))

            if i in ('E', 'W'):
                if i == 'E':
                    if self.x < 100:
                        self.x += 1
                        self._path.append((self.x, self.y))
                    else:
                        self._path.append((self.x, self.y))
                else:
                    if self.x > 0:
                        self.x -= 1
                        self._path.append((self.x, self.y))
                    else:
                        self._path.append((self.x, self.y))
        return (self.x, self.y)

    def path(self):
        return self._path


r = Robot((0, 0))
print(r.move('N' * 200))
print(*r.path())
print(r.move('NNN'))
print(*r.path())
