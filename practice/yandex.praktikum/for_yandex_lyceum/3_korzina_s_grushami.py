"""
Итак, у вас есть корзина с грушами и несколько детей. Нужно поделить груши 
так, чтобы никому из детей не было обидно, то есть поровну. (Теперь понятно, 
почему в задаче дети?)
Напишите класс PearsBasket, экземпляр которого при инициализации получает целое 
число – количество груш в корзине.
В классе должны быть методы:

pb // n – деление нацело, возвращает список объектов класса со значениями количества 
груш в каждой корзинке, если есть остаток – он должен находиться в дополнительной 
последней корзинке.
pb % n – получение остатка от деления, возвращает число: остаток от деления.
pb_1 + pb_2 – складываются две корзинки, получается новая корзина;
pb_1 - n – число вычитается из корзинки, если там есть такое количество груш; если 
нет – вычитается сколько есть, остается 0;
 __str__ – возвращает количество груш в корзине;
 __repr__ – возвращает строку в формате PearsBasket(<количество>).
"""


class PearsBasket:
    def __init__(self, amount):
        self.amount = amount

    def __floordiv__(self, other):
        x = self.amount // other
        y = self.amount % other
        z = []
        for i in range(x):
            z.append(PearsBasket(x))
        if y > 0:
            z.append(PearsBasket(y))
        return z

    def __mod__(self, other):
        self.amount = self.amount % other
        return self.amount

    def __add__(self, other):
        return self.amount + other.amount

    def __sub__(self, other):
        if other >= self.amount:
            self.amount = 0
            return self.amount
        else:
            self.amount -= other
            return self.amount

    def __str__(self):
        return self.amount

    def __repr__(self):
        return f'{self.__class__.__name__}({self.amount})'


pb = PearsBasket(17)
array = pb // 4
print(array)
pb_2 = PearsBasket(13)
pb_3 = pb + pb_2
print(pb_3)
print(pb_3 % 7)
pb - 2
print([pb])
