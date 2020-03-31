import itertools
print(*itertools.combinations([1, 2, 3], 2))
print(*itertools.permutations([1, 2, 3], 2))
import functools
prints = functools.partial(print, end=' ')
prints(1, 2, 3)
print(functools.reduce(lambda x, y: x + y, (1, 2, 3)))
print(*itertools.accumulate([1, 4, 3, 5], min))
