"""
В городе Тарантасске проходят гонки без ограничений. Это значит, что 
одновременно соревноваться могут гонщики на автомобилях, мотоциклах и 
даже гужевых повозках. Скорости автомобиля и мотоцикла зависят от того, 
каким бензином они заправлены - 98 позволяет ехать с полной скоростью, 
95 уменьшает скорость на 10% для машин и на 20% для мотоциклов, 92-й - 
на 20% и 40% соответственно. Гужевые повозки едут с постояной скоростью.

Длина кольцевой трассы равна M. Определить, какое транспортное средство 
будет ближе к финишу спустя время t после начала гонок (возможно, проходя 
при этом не первый круг). Если несколько средств будут одинаково близки, 
вывести нужно то, у которого меньше номер. Для описания транспортных средств 
используйте наследование классов.

Формат ввода
Программа получает на вход строку с натуральными числами N, M и t - количеством 
транспортных средств, длиной трассы и временем гонки соответственно.
Дальше следуют N строк. В каждой записано три натуральных числа - индивидуальный 
номер транспортного средства, тип средства (1 - автомобиль, 2 - мотоцикл, 
3 - гужевая повозка) и скорость данного средства. Если это автомобиль или мотоцикл, 
то в строке также есть четвёртое число - марка бензина, которым заправлено средство.

Формат вывода
Программа должна вывести одно число - номер транспортного средства, которое спустя 
время t окажется ближе всего к финишу.
"""


from icecream import ic
import re


class Vehicle:
    def __init__(self, number, speed):
        self.number = number
        self.speed = speed

    def get_distance(self, time, length):
        total_distance = time * self.speed
        total_laps = total_distance // length
        if total_laps == 0:
            estimated_distance = length - total_distance
        else:
            finish_distance = total_distance - total_laps * length
            estimated_distance = length - finish_distance
        return estimated_distance


class Car(Vehicle):
    def __init__(self, number, speed, petrol):
        super().__init__(number, speed)
        self.petrol = petrol
        if self.petrol == 95:
            self.speed *= 0.9
        elif self.petrol == 92:
            self.speed *= 0.8


class Motocycle(Vehicle):
    def __init__(self, number, speed, petrol):
        super().__init__(number, speed)
        self.petrol = petrol
        if self.petrol == 95:
            self.speed *= 0.8
        elif self.petrol == 92:
            self.speed *= 0.6


with open('input.txt', 'r') as input:
    total = []
    for i in input.readlines():
        x = re.split('[\s]+', i)
        if x[-1] == '':
            x.remove(x[-1])
        total.append(x)
    amount_of_racers = total[0][0]
    lap_length = total[0][1]
    race_time = total[0][2]
    racers = []
    for i in range(1, int(amount_of_racers) + 1):
        if int(total[i][1]) == 3:
            racers.append(Vehicle(int(total[i][0]), int(total[i][2])))
        if int(total[i][1]) == 2:
            racers.append(Motocycle(int(total[i][0]), int(
                total[i][2]), int(total[i][3])))
        if int(total[i][1]) == 1:
            racers.append(Car(int(total[i][0]), int(
                total[i][2]), int(total[i][3])))

    closest_to_finish = racers[0].get_distance(int(race_time), int(lap_length))
    number_of_winner = racers[0].number
    for racer in racers[1:]:
        x = racer.get_distance(int(race_time), int(lap_length))
        if x < closest_to_finish:
            closest_to_finish = x
            number_of_winner = racer.number
        elif x == closest_to_finish:
            if racer.number < number_of_winner:
                number_of_winner = racer.number
    with open('output.txt', 'w') as output:
        output.write(str(number_of_winner))
