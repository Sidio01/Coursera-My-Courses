class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""


class EventGet:
    def __init__(self, kind):
        self.kind = kind


class EventSet:
    def __init__(self, value):
        self.value = value


class NullHandler:
    def __init__(self, successor=None):
        self.__successor = successor

    def handle(self, field, event):
        if self.__successor is not None:
            return self.__successor.handle(field, event)


class IntHandler(NullHandler):
    def handle(self, field, event):
        if 'kind' in event.__dir__():
            if event.kind.__name__ == 'int':
                return field.integer_field
            else:
                return super().handle(field, event)
        elif 'value' in event.__dir__():
            if isinstance(event.value, int):
                field.integer_field = event.value
            else:
                return super().handle(field, event)


class FloatHandler(NullHandler):
    def handle(self, field, event):
        if 'kind' in event.__dir__():
            if event.kind.__name__ == 'float':
                return field.float_field
            else:
                return super().handle(field, event)
        elif 'value' in event.__dir__():
            if isinstance(event.value, float):
                field.float_field = event.value
            else:
                return super().handle(field, event)


class StrHandler(NullHandler):
    def handle(self, field, event):
        if 'kind' in event.__dir__():
            if event.kind.__name__ == 'str':
                return field.string_field
            else:
                return super().handle(field, event)
        elif 'value' in event.__dir__():
            if isinstance(event.value, str):
                field.string_field = event.value
            else:
                return super().handle(field, event)


"""
Debug
"""
# obj = SomeObject()
# obj.integer_field = 42
# obj.float_field = 3.14
# obj.string_field = "some text"
# chain = FloatHandler(IntHandler(StrHandler(NullHandler)))
# print('old values')
# print(chain.handle(obj, EventGet(int)))
# print(chain.handle(obj, EventGet(float)))
# print(chain.handle(obj, EventGet(str)))
# print()
# print('new values')
# chain.handle(obj, EventSet(100))
# print(chain.handle(obj, EventGet(int)))
# chain.handle(obj, EventSet(0.5))
# print(chain.handle(obj, EventGet(float)))
# chain.handle(obj, EventSet('new text'))
# print(chain.handle(obj, EventGet(str)))
