#print(
#    *filter(
#        lambda x: x > 0,
#        map(
#            int,
#            input().split()
#        )
#    )
#)

print(*enumerate('abcde'))
print(any((True, False, True)))
print(all((True, False, True)))

print(
    all(
        map(
            lambda x: x > 0,
            map(
                int,
                input().split()
            )
        )
    )
)