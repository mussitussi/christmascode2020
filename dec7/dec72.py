from typing import Callable, Dict, List, Tuple
from dec7 import into_outer_innerbags
BagMap = Dict[str, List[Tuple[int, str]]]


def parse_inner(inner: str):
    '''
    >>> parse_inner('2 dark red bags.')
    (2, 'dark red')
    '''
    if not inner[0].isnumeric():
        return None
    n, c1, c2, *_ = inner.split()
    return (int(n), c1 + ' ' + c2)


def rules2bagmap(rules: List[str]) -> BagMap:
    ''' Parses rules into a more structured format
    >>> rules2bagmap(['shiny gold bags contain 2 dark red bags.'])
    {'shiny gold': [(2, 'dark red')]}
    '''
    bagmap = {}
    for rule in rules:
        outer, inners = into_outer_innerbags(rule)
        inners_parsed = [y for x in inners if (y := parse_inner(x))]
        bagmap[outer] = inners_parsed
    return bagmap


class ABag:
    pass


class Bag(ABag):
    '''
    Tree like structure for bags
                           (1 shiny gold)
                            /           \
                      (1 dark olive)    (2 vibrant plum)
                       /         \             /    |     \
           (3 faded blue)   (4 dotted black)  (...) (...) (...)

    '''

    def __init__(self, number: int, color: str, bags: List[ABag]):
        self.number = number
        self.color = color
        self.bags = bags

    @property
    def count(self):
        return self.number * (1 + sum(bag.count for bag in self.bags))


def createbag(rules: List[str], firstbag: str):
    '''
    creates bag tree
    '''
    bagmap = rules2bagmap(rules)

    def addchilds(bag: Bag):
        innerbags = bagmap[bag.color]
        bag.bags = [Bag(i, c, []) for i, c in innerbags]
        for b in bag.bags:
            if isinstance(b, Bag):
                addchilds(b)

    rootbag = Bag(1, firstbag, [])
    addchilds(rootbag)
    return rootbag


if __name__ == '__main__':
    with open('sample-input.txt') as f:
        rules_sample = [rule.strip() for rule in f]

    bag_sample = createbag(rules_sample, 'shiny gold')
    print(f'sample result = {bag_sample.count - 1 = }')

    with open('puzzle-input.txt') as f:
        rules = [rule.strip() for rule in f]

    bag = createbag(rules, 'shiny gold')
    print(f'result = {bag.count - 1 = }')
