from collections import namedtuple
from functools import reduce
from itertools import pairwise, product
from pprint import pprint

AUTHOR = 'Tamsyn Morrill'
TITLE = 'knave_star.py'
DESCRIPTION = "Let's have some knavery!"
VERSION = '0.1'

def compose(*funcs):
    if funcs == ():
        chain = lambda x: x
    else:
        head, *tail = funcs
        chain_t = compose(*tail)
        chain = lambda x: head(chain_t(x))
    return lambda x: chain(x)


bond = {'|': '',
        'a': '',
        'e': '',
        'i': '',
        'b': 'e',
        'c': 'a',
        'd': 'i',
        'f': 'e',
        'g': 'a',
        'h': 'i',
        'j': 'e',
        'k': 'a',
        'l': 'i',
        'm': 'e',
        'n': 'a',
        'p': 'i'}

desc_0 = {'|': '|',
          'a': 'b',
          'e': 'c',
          'i': 'f',
          'b': 'b',
          'c': 'bb',
          'd': 'b',
          'f': 'c',
          'g': 'cb',
          'h': 'c',
          'j': 'f',
          'k': 'fb',
          'l': 'f',
          'm': 'd',
          'n': 'db',
          'p': 'd'}

desc_a = {'|': 'a|',
          'a': 'c',
          'e': 'f',
          'i': 'd',
          'b': 'c',
          'c': 'cb',
          'd': 'c',
          'f': 'f',
          'g': 'fb',
          'h': 'f',
          'j': 'd',
          'k': 'db',
          'l': 'd',
          'm': 'bb',
          'n': 'bbb',
          'p': 'bb'}

desc_e = {'|': 'e|',
          'a': 'f',
          'e': 'd',
          'i': 'bb',
          'b': 'f',
          'c': 'fb',
          'd': 'f',
          'f': 'd',
          'g': 'db',
          'h': 'd',
          'j': 'bb',
          'k': 'bbb',
          'l': 'bb',
          'm': 'g',
          'n': 'gb',
          'p': 'g'}

desc_i = {'|': 'i|',
          'a': 'd',
          'e': 'bb',
          'i': 'g',
          'b': 'd',
          'c': 'db',
          'd': 'd',
          'f': 'bb',
          'g': 'bbb',
          'h': 'bb',
          'j': 'g',
          'k': 'gb',
          'l': 'g',
          'm': 'j',
          'n': 'jb',
          'p': 'j'}

lookup = {'': desc_0,
          'a': desc_a,
          'e': desc_e,
          'i': desc_i}


def knave_star(word: str):
    acc = '|'
    for pair in pairwise(word):
        val = bond[pair[0]]
        desc = lookup[val]
        acc += desc[pair[1]]
    return acc


def welcome():
    print(f'{AUTHOR} welcomes you to {TITLE}, v{VERSION}.')
    print('')
    print(DESCRIPTION)
    print('')


def oops():
    print('Come again?')


def pick(msg:str, options:tuple):
    if msg != '':
        print(msg)
    verbose = (f'    {i}: {opt}' for i, opt in enumerate(options))
    for line in verbose:
        print(line)
    selection = None
    while selection is None:
        try:
            i = int(input())
            selection = options[i]
        except:
            oops()
    print('')
    return selection


MODES = ('Knave*', 'Translation dicitionary')


def set_mode():
    return pick('Select mode:', MODES)


def single():
    print('Input a word using the letters a-m, p.')
    word = input('Vowels may only occur at the end of the word.\n')
    print()
    word = '|' + word + '|'
    desc = knave_star(word)
    print(f'The star-eyed knave describes {word} as {desc}.')


bits = {'|': '',
        'a': '1',
        'e': '11',
        'i': '111',
        'b': '10',
        'c': '100',
        'd': '1000',
        'f': '110',
        'g': '1100',
        'h': '11000',
        'j': '1110',
        'k': '11100',
        'l': '111000',
        'm': '11110',
        'n': '111100',
        'p': '1111000'
}


def print_dict():
    pprint(bits)
    print()


action = {'Knave*': single,
          'Translation dicitionary': print_dict}


def again():
    val = pick('Choose another mode?', ('No', 'Yes'))
    return val == 'Yes'


def ciao():
    print('Ciao!')


def main():
    welcome()
    repeat = True
    while repeat:
        mode = set_mode()
        action[mode]()
        repeat = again()
    ciao()


if __name__ == '__main__':
    main()
