from collections import namedtuple
from functools import reduce
from itertools import product
from pprint import pprint

def word(*indices:int):
    '''Return the word corresponding to any number of indices.'''
    # define lookup table
    string = {1: '10',
              2: '11',
              3: '1110',
              4: '11110',
              5: '111110',
              6: '111000',
              7: '1111000',}
    # concatenate results
    return reduce(lambda acc, index: acc + string[index],
                  indices, "")


def entrywise(x:tuple, y:tuple):
    '''Return entrywise sum of two tuples.'''
    return tuple(sum(pair) for pair in zip(x, y))


Stats = namedtuple('stats', ['zeros', 'ones', 'length'], defaults=(0, 0, 0))

def stats(*indices:int):
    '''Return the stats tuple corresponding to any number of indices.'''
    # define lookup table
    tuple = {1: (1, 1, 2),
             2: (2, 0, 2),
             3: (1, 3, 4),
             4: (1, 4, 5),
             5: (1, 5, 6),
             6: (3, 3, 6),
             7: (3, 4, 7),}
    # sum results
    seq = reduce(lambda acc, index: entrywise(acc, tuple[index]),
                 indices, Stats())
    return Stats(*seq)


def expand(*seq:int):
    return word(*seq), stats(*seq)


def knave_f(m, n):
    '''Return the index-sequence corresponding to f(w_m, w_n).'''
    # select lookup table
    match m:
        case 1 | 3 | 4:
            seq = {1: (3,),
                   3: (4,),
                   4: (6,),
                   5: (3, 1),
                   6: (4,),
                   7: (6,),}
        case 5:
            seq = {1: (1, 3),
                   3: (1, 4),
                   4: (1, 6),
                   5: (1, 3, 1),
                   6: (1, 4),
                   7: (1, 6),}
        case 6 | 7:
            seq = {1: (4,),
                   3: (5,),
                   4: (7,),
                   5: (4, 1),
                   6: (5,),
                   7: (7,),}
    return seq[n]


def knave_g(m, n):
    '''Return the index-sequence corresponding to g(w_m, w_n).'''
    match m:
        case 1 | 3 | 4 | 5:
            seq = {1: (3,),
                   3: (4,),
                   4: (6,),
                   5: (3,),
                   6: (4,),
                   7: (6,),}
        case 6 | 7:
            seq = {1: (4,),
                   3: (5,),
                   4: (7,),
                   5: (4,),
                   6: (5,),
                   7: (7,),}
    return seq[n]


def test_single(func, seqs=None):
    '''Print results of func applied to a sequence of index-sequences'''
    # define default value of seqs
    if seqs is None:
        indices = (1, 3, 5, 6, 7)
        seqs = product(indices, indices)
    name = func.__name__
    for arg1, arg2 in seqs:
        val = func(arg1, arg2)
        print(f'{func.__name__}({arg1}, {arg2}) = {val}')


def test_mult(*funcs):
    '''Print results of test_single applied to a sequence of functions.'''
    for func in funcs:
        name = func.__name__
        print(f'Testing function {name}:')
        print('----------------')
        print('')
        test_single(func)
        print('')


def main():
    test_mult(expand, knave_f, knave_g)


if __name__ == '__main__':
    main()
