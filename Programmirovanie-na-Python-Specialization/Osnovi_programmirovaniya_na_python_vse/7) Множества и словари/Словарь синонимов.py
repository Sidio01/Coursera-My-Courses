n = int(input())
myDict = dict()
for i in range(n):
    n = list(input().split())
    myDict[n[1]] = n[0]
    myDict[n[0]] = n[1]
n = input()
print(myDict[n])
