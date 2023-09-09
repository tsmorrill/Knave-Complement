from collections import namedtuple
from functools import reduce
from itertools import groupby, pairwise, product
from math import pow
from pprint import pprint
from random import choice

AUTHOR = 'Tamsyn Morrill'
TITLE = 'knave_star.py'
DESCRIPTION = "Let's have some knavery!"
VERSION = '0.4'

def compose(*funcs):
    if funcs == ():
        chain = lambda x: x
    else:
        head, *tail = funcs
        chain_t = compose(*tail)
        chain = lambda x: head(chain_t(x))
    return lambda x: chain(x)


def welcome():
    print(f'{AUTHOR} welcomes you to {TITLE}, v{VERSION}.')
    print('')
    print(DESCRIPTION)
    print('')


def oops():
    msg = choice(('Come again?',
                  "I didn't catch that.",
                  "Sorry, I'm only a simple script.",
                  "That's a typo.",
                  'Do me a solid and read those instructions again.',
                  'Are you doing this on purpose?',
                  "I'm a state machine, not a language model.",
                  "Honestly, I'm more of a parsnip than a parser.",
                  "Just how much spare time do you think Tammy put into these Easter Eggs?"))
    print(msg)


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


MODES = ('Knave Map',
         'Knave* Map',
         'Iterate w/ Stats',
         'Translation Dicitionary')


def set_mode():
    return pick('Select mode:', MODES)


def run_length(data: str):
    return ((sum(1 for _ in y), x) for x, y in groupby(data))


def knave_run(pair):
    run, char = pair
    lie = {'0': '1', '1': '0'}
    return '{0:b}'.format(run) + lie[char]


def knave(word:str):
    pairs = tuple(run_length(word))
    desc = reduce(lambda x, y: x+y, map(knave_run, pairs), '')
    return desc


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

desc_0 = {'|': '|', # Python does not like pipes in its names
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

table = {'': desc_0,
         'a': desc_a,
         'e': desc_e,
         'i': desc_i}


def knave_star(word: str):
    acc = '|'
    for pair in pairwise(word):
        val = bond[pair[0]]
        desc = table[val]
        acc += desc[pair[1]]
    return acc


def single(func, mode:str):
    helptext = {'Knave Map': 'Input a binary word.',
                'Knave* Map': 'Input a word using the letters a-m, p.'}
    prompt = {'Knave Map': 'Just zeroes and ones, thank you.\n',
              'Knave* Map': 'Vowels may only occur at the end of the word.\n'}
    adj = {'Knave Map': 'two-faced',
           'Knave* Map': 'star-eyed'}
    def dialogue():
        print(helptext[mode])
        word = input(prompt[mode])
        print()
        if mode == 'Knave* Map':
            word = '|' + word + '|'
        desc = func(word)
        print(f'The {adj[mode]} knave describes {word} as {desc}.')
    return dialogue


bits = {'|': '',
        'a': '1',
        'b': '10',
        'c': '100',
        'd': '1000',
        'e': '11',
        'f': '110',
        'g': '1100',
        'h': '11000',
        'i': '111',
        'j': '1110',
        'k': '11100',
        'l': '111000',
        'm': '11110',
        'n': '111100',
        'p': '1111000'
}

Stats_tuple = namedtuple('stats', ['zeroes', 'ones'], defaults=(0, 0))

counts = {'|': Stats_tuple(0, 0),
          'a': Stats_tuple(0, 1),
          'b': Stats_tuple(1, 1),
          'c': Stats_tuple(2, 1),
          'd': Stats_tuple(3, 1),
          'e': Stats_tuple(0, 2),
          'f': Stats_tuple(1, 2),
          'g': Stats_tuple(2, 2),
          'h': Stats_tuple(3, 2),
          'i': Stats_tuple(0, 3),
          'j': Stats_tuple(1, 3),          
          'k': Stats_tuple(2, 3),
          'l': Stats_tuple(3, 3),
          'm': Stats_tuple(1, 4),
          'n': Stats_tuple(2, 4),
          'p': Stats_tuple(3, 4),       
}

def stats(word):
    def stat_sum(acc:tuple, char:str):
        val = counts[char]
        return (acc[0] + val[0], acc[1] + val[1])

    if len(word) == 1:
        output = counts[word]
    else:
        output = (reduce(stat_sum, word, (0, 0)))
        output = Stats_tuple(*output)
    return output


def iterate_stats():
    in_word = input('Input a word using the letters a-m, p.\n')
    in_word = '|' + in_word + '|'
    n = int(input('How many iterations?\nn = '))
    queue = (knave_star for _ in range(n))
    multi = compose(*queue)
    out_word = multi(in_word)
    in_stats = stats(in_word)
    in_len = in_stats[0] + in_stats[1]
    in_density = in_stats[1] / in_len
    out_stats = stats(out_word)
    out_len = out_stats[0] + out_stats[1]
    out_density = out_stats[1] / out_len
    rate = pow(out_len/in_len, 1/n)
    print('')
    print(f'A party of {n} knaves depart with a word of bitlength {in_len} and density {in_density}.')
    print(f'They return with a word of bitlength {out_len} and density {out_density}.')
    print(f"The average knave extendeds the word's length by a factor of {rate}.\n")    


def print_dict():
    for key in bits.keys():
        print(f"'{key}' -> '{bits[key]}'")
    print()


action = {'Knave Map': single(knave, 'Knave Map'),
          'Knave* Map': single(knave_star, 'Knave* Map'),
          'Iterate w/ Stats': iterate_stats,
          'Translation Dicitionary': print_dict}


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
