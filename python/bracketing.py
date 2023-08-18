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


def test_inputs(func):
    indices = (1, 3, 5, 6, 7)
    name = func.__name__
    for arg1, arg2 in product(indices, indices):
        val = func(arg1, arg2)
        print(f"{func.__name__}({arg1}, {arg2}) = {val})")
    print("")


def test_many(*funcs):
    for func in funcs:
        name = func.__name__
        print(f"Testing function {name}:")
        print("----")
        print("")
        test_inputs(func)
        print("")


def main():
    test_many(knave_f, knave_g)


if __name__ == "__main__":
    main()
