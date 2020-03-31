capitals = {'Russia': ['Moscow'], 'France': 'Paris'}
capitals['USA'] = 'Washington'
print(capitals['USA'])
print(*capitals)
del capitals['France']
print(capitals)
if 'Russia' in capitals:
    capitals['Russia'].append('Peterburg')
    print(capitals['Russia'])
    print(capitals)
print('Russia' in capitals)
myDict = dict({('x', 5), ('y', 3)})
print(myDict)
for i in myDict:
    print(i, myDict[i])
