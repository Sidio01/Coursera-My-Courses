from contracts import contract


@contract(x='int', y='float', returns='float')
def mul(x, y):
    return x * y


print(mul(3, 2.5))
