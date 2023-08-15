from itertools import product

words = tuple("W" + str(i) for i in (1,) + tuple(range(3, 8)))
strings = (f"        ({x}, {y}):" for x, y in product(words, words))

for x in strings:
    print(x)
