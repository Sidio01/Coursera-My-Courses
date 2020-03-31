n = int(input())
if n % 10 == 1 and n != 11:
    print(n, 'korova')
elif n % 10 == 2 and n != 12:
    print(n, 'korovy')
elif n % 10 == 3 and n != 13:
    print(n, 'korovy')
elif n % 10 == 4 and n != 14:
    print(n, 'korovy')
else:
    print(n, 'korov')
