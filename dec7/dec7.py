from typing import Dict, List, Set, Tuple, Union


# def parse_r(r: str) -> Union[None, Tuple[int, str]]:
#     '''
#     >>> parse_r('1 bright white bag')
#     (1, 'bright white')
#     >>> parse_r('2 muted yellow bags')
#     (2, 'muted yellow')
#     >>> parse_r('no other bags.') is None
#     True
#     '''
#     xs = r.strip()
#     if not xs[0].isnumeric():
#         return None

#     number, color1, color2, *_ = xs.split()
#     count = int(number)
#     bagtype = color1 + ' ' + color2
#     return (count, bagtype)


def parse_innerbag(r: str) -> Union[None, str]:
    '''
    >>> parse_innerbag('1 bright white bag')
    'bright white'
    >>> parse_innerbag('2 muted yellow bags')
    'muted yellow'
    >>> parse_innerbag('no other bags.') is None
    True
    '''
    xs = r.strip()
    if xs == 'no other bags.':
        return None

    _, color1, color2, *_ = xs.split()
    bagtype = color1 + ' ' + color2
    return bagtype


def into_outer_innerbags(rule: str) -> Tuple[str, List[str]]:
    '''
    >>> r = 'light red bags contain 1 bright white bag, 2 muted yellow bags.'
    >>> into_outer_innerbags(r)
    ('light red', ['1 bright white bag', '2 muted yellow bags.'])
    >>> r = 'faded blue bags contain no other bags.'
    >>> into_outer_innerbags(r)
    ('faded blue', ['no other bags.'])
    '''
    outer, rest = rule.split('contain')
    outerbag = outer.replace('bags', '').strip()
    innerbags = [x.strip() for x in rest.split(',')]
    return outerbag, innerbags


def rules2map(rules: List[str]) -> Dict[str, List[str]]:
    bags = {}
    for rule in rules:
        outerbag, innerbags = into_outer_innerbags(rule)
        bags[outerbag] = [parsed for innerbag in innerbags
                          if (parsed := parse_innerbag(innerbag))]
    return bags


def bag_in_outerbag(bagmap: Dict[str, List[str]], outerbag, bag) -> bool:
    innerbags = bagmap[outerbag]
    return (bag in innerbags or
            any(bag_in_outerbag(bagmap, b, bag) for b in innerbags))


def outerbagscontaining(bag, rules) -> Set[str]:
    bagmap = rules2map(rules)
    bags = set()
    for outerbag in bagmap.keys():
        if bag_in_outerbag(bagmap, outerbag, bag):
            bags.add(outerbag)
    return bags


def readsample():
    with open('./sample-input.txt') as f:
        return [line.strip() for line in f]


def readpuzzle():
    with open('./puzzle-input.txt') as f:
        return [line.strip() for line in f]


if __name__ == '__main__':
    lines = readsample()
    outerbags = outerbagscontaining('shiny gold', lines)
    nouterbags = len(outerbags)
    print(f'{nouterbags=}')

    lines2 = readpuzzle()
    outerbags2 = outerbagscontaining('shiny gold', lines2)
    nouterbags2 = len(outerbags2)
    print(f'{nouterbags2=}')
