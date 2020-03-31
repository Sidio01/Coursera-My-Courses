s = str(input())
if s.find('f', 0) == -1 and s.rfind('f', 0) == -1:
    print('')
elif s.find('f', 0) == s.rfind('f', 0):
    print(s.find('f', 0))
else:
    print(s.find('f', 0), s.rfind('f', 0))
