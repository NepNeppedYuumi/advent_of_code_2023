# part 1
print(sum(
    map(
        lambda x:
        int(x[0].split(' ')[-1]) if
            not any(
                (
                True for col in
                x[1].replace(';', ',').split(', ')
                if (12, 13, 14)[
                    ('red', 'green', 'blue').index(col.split(' ')[-1])
                   ] < int(col.split(' ')[0])
                )
            )
        else 0,
    map(
        lambda x: x.strip().split(': '), open('002.txt', 'r')
    ))))
# var = ["game 1", "12 rood, 5 blauw, 1 blauw, 4 rood"]
# game_id = var[0].split()
# col = "12 rood"
# col1 = "12"
# col2 = "rood"

print(sum(map(lambda x:int(x[0].split(' ')[-1]) if not any((True for col in x[1].replace(';', ',').split(', ') if (12, 13, 14)[('red', 'green', 'blue').index(col.split(' ')[-1])] < int(col.split(' ')[0])))else 0,map(lambda x: x.strip().split(': '), open('002.txt', 'r')))))


# pièrre's solution

print(sum(
    int(g.split(' ')[1])
    for g,r in
    (l.strip().split(': ')
     for l in open('input.txt'))
    if all({"red":13,"green":14,"blue":15}.get(
        c.split(' ')[1], 0) > int(c.split(' ')[0]
                               ) for s in r.split("; ")
           for c in s.split(", ")
           )
    )
)

# test for 1 line nested for loops

gen = (i for y in ((1, 2), (3, 4), (5, 6)) for i in y)

