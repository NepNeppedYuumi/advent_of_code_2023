from functools import cache


@cache
def func(thing):
    return thing[1]


func({1, 2, 3})