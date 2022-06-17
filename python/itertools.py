import itertools

names = ["Ben", "Daisy", "John", "Lauren"]

repeated = itertools.cycle(names)

def cycle(iterable):
    saved = []
    for item in iterable:
        yield item
        saved.append(item)
    else:
        yield "iterable exhausted"

cycled = cycle(names)

print(next(cycled))
print(next(cycled))
print(next(cycled))
print(next(cycled))
