from functools import singledispatch


def _string_backwards(input: str):
    print(input)
    for i in range(1, len(input)):
        print(input[:-i])


@singledispatch
def count_down(data_type):
    raise ValueError


@count_down.register(int)
@count_down.register(str)
@count_down.register(float)
def _(arg):
    _string_backwards(str(arg))


@count_down.register(list)
@count_down.register(tuple)
@count_down.register(set)
@count_down.register(range)
def _(arg):
    s = "".join(str(value) for value in arg)
    _string_backwards(s)


@count_down.register(dict)
def _(arg):
    s = "".join(str(value) for value in arg.keys())
    _string_backwards(s)
