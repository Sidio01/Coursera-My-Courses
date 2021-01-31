"""
Чип и Дейл устали от публичности. Чтобы как-то обезопасить
свои персональные данные, они решили шифровать
sms - сообщения. Числа они решили разворачивать. Помогите
им написать программу для кодирования чисел.

Формат ввода
На вход подается целое число n, по модулю не
превосходящее 10000.

Формат вывода
На выходе должно быть число, развернутое в обратном порядке.
"""


with open('input.txt', 'r') as input:
    num = input.read()
    total = list(num)
    if int(num) > 0:
        result = []
        for _ in total[::-1]:
            if _ == '\n':
                pass
            elif _ == '0' and result == []:
                pass
            else:
                result.append(_)
    elif int(num) < 0:
        result = ['-']
        for _ in total[::-1]:
            if _ == '-' or _ == '\n':
                pass
            elif _ == '0' and result[-1:] == ['-']:
                pass
            else:
                result.append(_)
    else:
        result = ['0']
    result = ''.join(result)
    with open('output.txt', 'w') as output:
        output.write(result)
