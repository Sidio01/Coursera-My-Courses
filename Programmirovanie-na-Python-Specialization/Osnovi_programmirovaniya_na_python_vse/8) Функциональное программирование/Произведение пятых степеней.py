import functools

print(
    functools.reduce(
        lambda x, y: x * y**5,
        map(
            int,
            input().split()
        ),
        1)
)
