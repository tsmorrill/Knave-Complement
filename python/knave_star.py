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


bond = {'|': '|',
        '.': 'a',
        '?': '',
        '!': 'e',
        ',': '',
        ';': 'a',
        'a': '',
        'b': '',
        'c': '',
        'd': '',
        'e': '',
        'f': '',
        'g': '',
        'h': '',
        'i': '',
        'j': '',
        'k': '',
        'l': '',
        'm': '',
        'n': '',}

desc_0 = {'|': '||',
          '.': '',
          '?': 'b',
          '!': '',
          ',': 'c',
          ';': 'a',
          'a': 'a?',
          'b': 'aa.',
          'c': 'a!',
          'd': 'ab.',
          'e': 'b?',
          'f': 'ba.',
          'g': 'b!',
          'h': 'e?',
          'i': 'ea.',
          'j': 'e!',
          'k': 'c?',
          'l': 'ca.',
          'm': 'c!',
          'n': 'aa?',
}

desc_a = {'|': 'a|',
          '.': 'ah',
          '?': 'a',
          '!': 'ak',
          ',': 'aj',
          ';': 'ah',
          'a': 'ah?',
          'b': 'aha.',
          'c': 'ah!',
          'd': 'ahb.',
          'e': 'ai?',
          'f': 'aia.',
          'g': 'ai!',
          'h': 'ak?',
          'i': 'aka.',
          'j': 'ak!',
          'k': 'aj?',
          'l': 'aja.',
          'm': 'aj!',
          'n': 'aha?',}

desc_e = {'|': 'e|',
          '.': 'bh',
          '?': 'b',
          '!': 'bk',
          ',': 'bj',
          ';': 'bh',
          'a': 'bh?',
          'b': 'bha.',
          'c': 'bh!',
          'd': 'bhb.',
          'e': 'bi?',
          'f': 'bia.',
          'g': 'bi!',
          'h': 'bk?',
          'i': 'bka.',
          'j': 'bk!',
          'k': 'bj?',
          'l': 'bja.',
          'm': 'bj!',
          'n': 'bha?',
}

desc_i = {'|': 'i|',
          '.': 'ea',
          '?': 'eaf',
          '!': 'eah',
          ',': 'eag',
          ';': 'eae',
          'a': 'eae?',
          'b': 'eaea.',
          'c': 'eae!',
          'd': 'eaeb.',
          'e': 'eaf?',
          'f': 'eafa.',
          'g': 'eaf!',
          'h': 'eah?',
          'i': 'eaha.',
          'j': 'eah!',
          'k': 'eag?',
          'l': 'eaga.',
          'm': 'eag!',
          'n': 'eaea?',
}

# Tammy what you need to do here is split the logic to alow both a bond of
# '|' or a bond of ''. The step that adds the outside bars is redundant
# now that you found the bug in helper.py. You may need to write a new table
# there first.

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
                'Knave* Map': 'Input a word using the letters a-n;'}
    prompt = {'Knave Map': 'Just zeroes and ones, thank you.\n',
              'Knave* Map': 'Exactly one of .?!,; may occur at the end of the word.\n'}
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
        '.': '1',
        '?': '11',
        '!': '111',       
        ',': '1111',
        ';': '11111',
        'a': '10',
        'b': '100',
        'c': '1000',
        'd': '10000',
        'e': '110',
        'f': '1100',
        'g': '11000',
        'h': '1110',
        'i': '11100',
        'j': '111000',
        'k': '11110',
        'l': '111100',
        'm': '1111000',
        'n': '111110',}

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
