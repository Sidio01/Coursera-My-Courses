from abc import ABC, abstractmethod
from inspect import isabstract

"""
Объявляем класс Hero
"""


# class Hero:
#     def __init__(self):
#         self.positive_effects = []
#         self.negative_effects = []
#         self.stats = {
#             "HP": 128,  # health points
#             "MP": 42,  # magic points,
#             "SP": 100,  # skill points
#             "Strength": 15,  # сила
#             "Perception": 4,  # восприятие
#             "Endurance": 8,  # выносливость
#             "Charisma": 2,  # харизма
#             "Intelligence": 3,  # интеллект
#             "Agility": 8,  # ловкость
#             "Luck": 1  # удача
#         }
#
#     def get_positive_effects(self):
#         return self.positive_effects.copy()
#
#     def get_negative_effects(self):
#         return self.negative_effects.copy()
#
#     def get_stats(self):
#         return self.stats.copy()


class AbstractEffect(Hero, ABC):
    def __init__(self, base):
        self.base = base

    @abstractmethod
    def get_positive_effects(self):
        return self.positive_effects.copy()

    @abstractmethod
    def get_negative_effects(self):
        return self.negative_effects.copy()

    @abstractmethod
    def get_stats(self):
        pass


class AbstractPositive(AbstractEffect):
    def get_positive_effects(self):
        self.positive_effects = self.base.get_positive_effects()
        effect_name = self.__class__.__name__
        self.positive_effects.append(effect_name)
        return self.positive_effects

    def get_negative_effects(self):
        self.negative_effects = self.base.get_negative_effects()
        return self.negative_effects.copy()

    @abstractmethod
    def get_stats(self):
        pass


class AbstractNegative(AbstractEffect):
    def get_negative_effects(self):
        self.negative_effects = self.base.get_negative_effects()
        effect_name = self.__class__.__name__
        self.negative_effects.append(effect_name)
        return self.negative_effects

    def get_positive_effects(self):
        self.positive_effects = self.base.get_positive_effects()
        return self.base.positive_effects.copy()

    @abstractmethod
    def get_stats(self):
        pass


"""
Положительные эффекты
"""


class Berserk(AbstractPositive):
    def get_stats(self):
        self.stats = self.base.get_stats()
        self.stats['HP'] = self.stats['HP'] + 50
        self.stats['Strength'] = self.stats['Strength'] + 7
        self.stats['Endurance'] = self.stats['Endurance'] + 7
        self.stats['Agility'] = self.stats['Agility'] + 7
        self.stats['Luck'] = self.stats['Luck'] + 7
        self.stats['Perception'] = self.stats['Perception'] - 3
        self.stats['Charisma'] = self.stats['Charisma'] - 3
        self.stats['Intelligence'] = self.stats['Intelligence'] - 3
        return self.stats.copy()


class Blessing(AbstractPositive):
    def get_stats(self):
        self.stats = self.base.get_stats()
        self.stats['Strength'] = self.stats['Strength'] + 2
        self.stats['Endurance'] = self.stats['Endurance'] + 2
        self.stats['Agility'] = self.stats['Agility'] + 2
        self.stats['Luck'] = self.stats['Luck'] + 2
        self.stats['Perception'] = self.stats['Perception'] + 2
        self.stats['Charisma'] = self.stats['Charisma'] + 2
        self.stats['Intelligence'] = self.stats['Intelligence'] + 2
        return self.stats.copy()


"""
Отрицательные эффекты
"""


class Weakness(AbstractNegative):
    def get_stats(self):
        self.stats = self.base.get_stats()
        self.stats['Strength'] = self.stats['Strength'] - 4
        self.stats['Endurance'] = self.stats['Endurance'] - 4
        self.stats['Agility'] = self.stats['Agility'] - 4
        return self.stats.copy()


class Curse(AbstractNegative):
    def get_stats(self):
        self.stats = self.base.get_stats()
        self.stats['Strength'] = self.stats['Strength'] - 2
        self.stats['Endurance'] = self.stats['Endurance'] - 2
        self.stats['Agility'] = self.stats['Agility'] - 2
        self.stats['Luck'] = self.stats['Luck'] - 2
        self.stats['Perception'] = self.stats['Perception'] - 2
        self.stats['Charisma'] = self.stats['Charisma'] - 2
        self.stats['Intelligence'] = self.stats['Intelligence'] - 2
        return self.stats.copy()


class EvilEye(AbstractNegative):
    def get_stats(self):
        self.stats = self.base.get_stats()
        self.stats['Luck'] = self.stats['Luck'] - 10
        return self.stats.copy()


# hero = Hero()
# print('Hero:', hero.get_stats())
# print('Positive effects:', hero.get_positive_effects())
# print('Negative effects:', hero.get_negative_effects())
# print()
# berserk = Berserk(hero)
# print('Berserk:', berserk.get_stats())
# print('Positive effects:', berserk.get_positive_effects())
# print('Negative effects:', berserk.get_negative_effects())
# print()
# berserk2 = Berserk(berserk)
# print('Berserk2:', berserk2.get_stats())
# print('Positive effects:', berserk2.get_positive_effects())
# print('Negative effects:', berserk2.get_negative_effects())
# print()
# curse = Curse(berserk2)
# print('Curse:', curse.get_stats())
# print('Positive effects:', curse.get_positive_effects())
# print('Negative effects:', curse.get_negative_effects())
# print()
# print(curse.base)
# curse.base = berserk
# print(curse)
# print()
# print('Curse:', curse.get_stats(), 'После снятия эффекта Берсерк')
# print('Positive effects:', curse.get_positive_effects())
# print('Negative effects:', curse.get_negative_effects())
# print()
# print('Hero:', hero.get_stats())
# print(isabstract(Berserk.__base__))
# print(isabstract(AbstractNegative))
# print(AbstractNegative.__base__)
