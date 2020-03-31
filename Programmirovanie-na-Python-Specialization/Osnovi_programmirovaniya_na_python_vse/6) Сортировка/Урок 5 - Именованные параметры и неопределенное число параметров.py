def printList(list, mySep=' '):
    for i in range(len(list) - 1):
        print(list[i], mySep, sep='', end='')
    print(list[-1], sep='')
printList([1, 2, 3], mySep='a')
printList([4, 5, 6])

def mySum(*args):
    nowSum = 0
    for now in args:
        nowSum += now
    return nowSum
print(mySum(1, 2, 3, 4, 5))
print(mySum(1))

def myMin(first, *others):
    nowMin = first
    for now in others:
        if now < nowMin:
            nowMin = now
    return nowMin
print(myMin(1, 2, 4, 5, -1))
