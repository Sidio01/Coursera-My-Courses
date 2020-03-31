import sys
message = sys.stdin.readlines()
i = 0
sum = set()
while i < len(message):
    a = set(message[i].split())
    sum |= a
    i += 1
print(len(sum))
