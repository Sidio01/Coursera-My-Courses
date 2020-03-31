def rec():
    n = int(input())
    if n == 0:
        return 0
    return rec() + n


print(rec())


# now = int(input())
# sumSeq = now
# while now != 0:
#     now = int(input())
#     sumSeq += now
# print(sumSeq)

# ДОДЕЛАТЬ !!!
