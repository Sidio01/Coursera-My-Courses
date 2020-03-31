print(
    any(
        map(
            lambda x: x == 0,
            map(
                lambda x: int(input()),
                range(
                    int(input())
                )
            )
        )
    )
)
