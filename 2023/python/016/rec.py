
def move(position: tuple[int, int], direction: tuple[int, int]):
    x, y = position
    if x < 0 or x >= len(data) or y < 0 or y >= len(data[0]):
        return
    if (position, direction) in combo:
        print("hi")
        return
    points.add(position)
    combo.add((position, direction))
    try:
        char = data[x][y]
    except:
        print(position, direction)
        raise BrokenPipeError
    if char == '.':
        dx, dy = direction
        return move((x + dx, y + dy), direction)
    elif char == '/':
        dx, dy = tuple(-1 * n for n in direction[::-1])
        return move((x + dx, y + dy), (dx, dy))
    elif char == '\\':
        dx, dy = tuple(n for n in direction[::-1])
        return move((x + dx, y + dy), (dx, dy))
    elif char == '|':
        dx, dy = direction
        if dx == 0:
            return move((x + 1, y), (1, 0)), move((x - 1, y), (-1, 0))
        return move((x + dx, y + dy), direction)
    elif char == '-':
        dx, dy = direction
        if dy == 0:
            return move((x, y + 1), (0, 1)), move((x, y - 1), (0, -1))
        return move((x + dx, y + dy), direction)
    print("hi?")
    raise BrokenPipeError