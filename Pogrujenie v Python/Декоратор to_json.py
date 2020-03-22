import json
import functools


def to_json(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # print('Code before')
        return json.dumps(func(*args, **kwargs))
        # ОБЯЗАТЕЛЬНО НЕОБХОДИМО ВОЗВРАЩАТЬ ЗНАЧЕНИЕ
        # print(type(json.dumps(func())))
        # print('Code after')
    return wrapper


# @to_json
# def get_data():
#     return 4
#
# get_data()
# assert isinstance(get_data(), str)
# print(get_data.__name__)
# вернёт '{"data": 42}'
# print(json.dumps({'data': 42}))
