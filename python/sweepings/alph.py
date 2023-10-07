from functools import reduce
from itertools import groupby, pairwise, product

# vowels denote a word consisting of all 1's
# what a lovely coincidence

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
        'n': '111110',
}

symbols = tuple(bits.keys())


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


def guillotine(word:str):
    prefixes = (s for s in symbols[::-1] if bits[s] != '')
    for s in prefixes:
        p = bits[s]
        if word.startswith(p):
            return s, word.removeprefix(p)
    print(f'Cannot match word {word}')
    return None


def translate(word:str):
    acc = ''
    while len(word) > 0:
        s, word = guillotine(word)
        acc += s
    return acc    
                    

def knave_star(word:str):
    return translate(knave(word))


def main():
    print('Higher-order alphabet for the knave map:')
    print()
    for s in symbols:
        print(s, '=', f"'{bits[s]}'")
    print()
    print('Interaction of adjacent symbols (head, tail) under the knave map:')
    print()
    for head in symbols:
        print(f'head = {head}')
        print('----------------')
        for tail in symbols:
            word = bits[head] + bits[tail]
            print(f'    {head + tail}:', word, '->', knave(word))
            print(f'        {knave_star(word)}') 

        print()    


if __name__ == "__main__":
    main()
