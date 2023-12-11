lijst = (
    (whil := [None] * 4),
    [
        float(i) if "." in i else int(i)
        for _ in whil
        if (
            b := (
                (i := input("geef inp: ")).isdigit()
                or (
                    len(i.split(".")) == 2
                    and all(n == "" or n.isdigit() for n in i.split("."))
                    and any(i.split("."))
                )
            ),
            whil.append(None) if not b else None,
        )[0]
    ],
)[1]

print(lijst)
