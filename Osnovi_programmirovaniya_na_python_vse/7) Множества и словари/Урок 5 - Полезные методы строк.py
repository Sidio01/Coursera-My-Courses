#gasCost = {}
#n = int(input())
#costs = list(map(int, input().split()))
#btypes = (92, 95, 98)
#for now in range(len(btypes)):
#    gasCost[btypes[now]] = costs[now]
#for i in range(n - 1):
#    costs = list(map(int, input().split()))
#    for now in range(len(btypes)):
#        gasCost[btypes[now]] = min(costs[now], gasCost[btypes[now]])
#print(gasCost[92], gasCost[95], gasCost[98])


#s = input()
#print(s.isalpha())

fin = open('input.txt')
myDict = {}
for line in fin:
    eng, latins = line.split('-')
    latinsList = latins.split(',')
    eng = eng.strip()
    newLatins = []
    for latin in latinsList:
        if latin not in myDict:
            myDict[latin.strip()] = []
        myDict[latin.strip()].append(eng)
        newLatins.append(latin.strip())
print(myDict)


# It's dangerous to go alone! Take this:
# isalpha - проверяет, что все символы строки являются буквами.
# isdigit - проверяет, что все символы строки являются цифрами.
# isalnum - проверяет, что все символы строки являются буквами или цифрами.
# islower - проверяет, что все символы строки являются маленькими (строчными) буквами.
# isupper - проверяет, что все символы строки являются большими (заглавными, прописными) буквами.
# lstrip - обрезает все пробельные символы в начале строки.
# rstrip - обрезает все пробельные символы в конце строки.
# strip - обрезает все пробельные символы в начале и конце строки.