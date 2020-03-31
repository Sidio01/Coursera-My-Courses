fin = open('input.txt')
myDict = {}
for line in fin:
    eng, latins = line.split('-')
    latinsList = latins.split(',')
    eng = eng.strip()
    for latin in latinsList:
        if latin.strip() not in myDict:
            myDict[latin.strip()] = []
        myDict[latin.strip()].append(eng)
for latin in sorted(myDict):
    print(latin, '-', ', '.join(sorted(myDict[latin])))


tree = {'a': {
            'b':dict(),
            'c': {
                'd': dict(),
                'e': dict()
            }
        }
    }
