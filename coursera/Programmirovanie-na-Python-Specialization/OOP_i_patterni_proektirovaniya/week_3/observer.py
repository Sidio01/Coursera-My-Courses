from abc import ABC, abstractmethod


# class Engine:
#     pass


class ObservableEngine(Engine):
    def __init__(self):
        self.__subscribers = set()

    def subscribe(self, subscriber):
        self.__subscribers.add(subscriber)

    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)

    def notify(self, message):
        for subscriber in self.__subscribers:
            subscriber.update(message)


class AbstractObserver(ABC):
    @abstractmethod
    def update(self, achievement):
        pass


class ShortNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = set()

    def update(self, achievement):
        new_achievement = achievement['title']
        self.achievements.add(new_achievement)


class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = []

    def update(self, achievement):
        list_of_achievements = []
        if len(self.achievements) == 0:
            self.achievements.append(achievement)
        else:
            for _ in range(len(self.achievements)):
                list_of_achievements.append(self.achievements[_]['title'])
            if achievement['title'] not in list_of_achievements:
                self.achievements.append(achievement)


"""
В атрибуте achievements у ShortNotificationPrinter хранится множество названий полученных достижений,
у FullNotificationPrinter - список достижений в том порядке,в котором они генерируются Engine.
Обратите внимание, что каждое достижение должно быть уникальным (то есть учтено только один раз).
"""

# short_notifier = ShortNotificationPrinter()
# full_notifier = FullNotificationPrinter()
# engine = ObservableEngine()
# engine.subscribe(short_notifier)
# engine.subscribe(full_notifier)
# engine.notify({"title": "Покоритель", "text": "Дается при выполнении всех заданий в игре"})
# engine.notify({"title": "Покоритель", "text": "Дается при выполнении всех заданий в игре"})
# engine.notify({"title": "Покоритель", "text": "Дается при выполнении всех заданий в игре дважды"})
# engine.notify({"title": "Супер-Покоритель", "text": "Дается при выполнении всех заданий в игре трижды"})
# engine.notify({"title": "Покоритель", "text": "Дается при выполнении всех заданий в игре"})
# print('short notifier achievements -', short_notifier.achievements)
# print('full notifier achievements -', full_notifier.achievements)
