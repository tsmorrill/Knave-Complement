from itertools import product

def knave_f(m, n):
    """Calculate indices corresponding to f(w_m, w_n)."""
    match m:
        case 1 | 3 | 4:
            lookup = {1: (3,),
                      3: (4,),
                      4: (6,),
                      5: (3, 1),
                      6: (4,),
                      7: (6,),}
        case 5:
            lookup = {1: (1, 3),
                      3: (1, 4),
                      4: (1, 6),
                      5: (1, 3, 1),
                      6: (1, 4),
                      7: (1, 6),}
        case 6 | 7:
            lookup = {1: (4,),
                      3: (5,),
                      4: (7,),
                      5: (4, 1),
                      6: (5,),
                      7: (7,),}
        case None:
            pass
    return lookup[n]

def knave_g(m, n):
    """Calculate indices corresponding to f(w_m, w_n)."""
    match m:
        case 1 | 3 | 4 | 5:
            lookup = {1: (3,),
                      3: (4,),
                      4: (6,),
                      5: (3,),
                      6: (4,),
                      7: (6,),}
        case 6 | 7:
            lookup = {1: (4,),
                      3: (5,),
                      4: (7,),
                      5: (4,),
                      6: (5,),
                      7: (7,),}
        case None:
            pass
    return lookup[n]


def test(func, arg1, arg2):
    name = func.__name__
    val = func(arg1, arg2)
    print(f"{name}({arg1}, {arg2}) = {val}")


def test_many(func):
    indices = (1, 3, 5, 6, 7)
    name = func.__name__
    print(f"Testing function {name}:")
    print("")
    for arg1, arg2 in product(indices, indices):
        test(func, arg1, arg2)
    print("")

test_many(knave_f)
print("----")
print("")
test_many(knave_g)
