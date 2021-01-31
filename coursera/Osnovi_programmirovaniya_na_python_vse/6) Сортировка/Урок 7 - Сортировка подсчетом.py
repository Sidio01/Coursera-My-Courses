myList = list(map(int, input().split()))
newList = []
for i in range(len(myList)):
    newList.append((myList[i], i))
newList.sort()
for now in newList:
    print(now[1])
print(newList)

myList1 = list(map(int, input().split()))
grades = [0] * 11
for now in myList1:
    grades[now] += 1
for grade in range(len(grades)):
    for i in range(grades[grade]):
        print(grade, end=' ')

