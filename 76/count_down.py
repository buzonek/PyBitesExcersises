from functools import singledispatch


@singledispatch
def count_down(data_type):
    raise ValueError


@count_down.register(str)
@count_down.register(int)
@count_down.register(float)
def _(data):
    data = str(data)
    while data:
        print(data)
        data = data[:-1]


@count_down.register(set)
@count_down.register(list)
def _(data):
    while data:
        print(''.join(str(x) for x in data))
        data.pop()


@count_down.register(dict)
def _(data):
    keys = sorted(data.keys())
    count_down(keys)


@count_down.register(tuple)
def _(data):
    count_down(list(data))

