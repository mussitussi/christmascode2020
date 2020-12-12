
bagtypes = [
    'light red',
    'dark orange',
    'bright white',
    'muted yellow',
    'shiny gold',
    'dark olive',
    'vibrant plum',
    'faded blue',
    'dotted black']


def parse_r(r):
    '''
    >>> parse_r('1 bright white bag')
    (1, 'bright white')
    >>> parse_r('2 muted yellow bags')
    (2, 'muted yellow')
    >>> parse_r('no other bags.') is None
    True
    '''
    xs = r.strip()
    if not xs[0].isnumeric():
        return

    number, adjective, color, *_ = xs.split()
    count = int(number)
    bagtype = adjective + ' ' + color
    return (count, bagtype)


def split_start_rest(rule):
    '''
    >>> rule = 'light red bags contain 1 bright white bag, 2 muted yellow bags.'
    >>> split_start_rest(rule)
    ('light red', ['1 bright white bag', '2 muted yellow bags.'])
    >>> rule = 'faded blue bags contain no other bags.'
    >>> split_start_rest(rule)
    ('faded blue', ['no other bags.'])
    '''
    start, rest = rule.split('contain')
    start_bag = start.replace('bags', '').strip()
    rest_split = [x.strip() for x in rest.split(',')]
    return start_bag, rest_split


def solve_sample():
    pass


def readsample():
    with open('./sample-input.txt') as f:
        return [line.strip() for line in f]


if __name__ == '__main__':
    lines = readsample()
    line = lines[0]

    for line in lines:
        print(split_start_rest(line))
