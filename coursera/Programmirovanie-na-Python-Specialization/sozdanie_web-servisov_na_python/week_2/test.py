import requests
from decimal import Decimal
# from currency import convert


# correct = Decimal('3754.8057')
# result = convert(Decimal("1000.1000"), 'RUR', 'JPY', "17/02/2005", requests)
# if result == correct:
#     print("Correct")
# else:
#     print("Incorrect: %s != %s" % (result, correct))


rur_val = 26.6352
rur_nom = 100
x = rur_nom / rur_val
print(x * 1000.1000)
