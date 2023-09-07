from functools import reduce
from itertools import groupby, pairwise, product

# vowels denote a word consisting of all 1's
# what a lovely coincidence

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


def bonds():
    print('Lookup table for knave* bonds:')
    print('--------')
    print('bond = {')
    for s in symbols:
        desc = knave_star(bits[s])
        v = desc[-1] if desc != '' else ''
        v = v if f in ('a', 'e', 'i') else ''
        print(f"        '{s}': '{v}'")
    print('}')


def knave_no_bleed(bond):
    print(f'Lookup table for knave* descriptions, vowels removed, bond = {bond}:')
    print('--------')
    print(f'desc_{bond} = {{')
    for s in symbols:
        desc = knave_star(bits[bond] + bits[s]) if s != '|' else '|'
        v = desc[-1]
        if v not in {'a', 'e', 'i'}:
            v = ''
        print(f"          '{s}': '{desc.removesuffix(v)}'")
    print('}')


def main():
    bonds()
    print()
    for bond in ('a', 'e', 'i'):
        knave_no_bleed(bond)

if __name__ == "__main__":
    main()
