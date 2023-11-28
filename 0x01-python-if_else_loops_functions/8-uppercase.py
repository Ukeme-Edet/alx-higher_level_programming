#!/usr/bin/python3
def uppercase(str):
    print(
        "".join(
            [chr(ord(s) - 32) for s in str if ord(s) > 96 and ord(s) < 123]
        ).format(
            ""
        )  # NOTE: had to use '.format("")', project requirements :)
    )
