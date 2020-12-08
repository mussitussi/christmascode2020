from functools import reduce
from typing import List


def word2set(word):
    '''
    >>> word2set('aabcb') == {'a', 'b', 'c'}
    True
    '''
    return set(list(word))


def yes_count_any(group: str) -> int:
    line = group.replace('\n', '')
    return len(word2set(line))


def solve(groups: List[str]) -> int:
    return sum(yes_count_any(group) for group in groups)


def yes_count_every(group: str) -> int:
    lines = group.split('\n')
    sets = [word2set(x) for line in lines if (x := line.strip()) != '']
    return len(reduce(set.intersection, sets, sets[0]))


def solve_part2(groups: List[str]) -> int:
    return sum(yes_count_every(group) for group in groups)


if __name__ == '__main__':
    with open('./puzzle-input.txt') as f:
        groups = [group for group in f.read().split('\n\n')]

    # for group in groups:
    #     print('-' * 40)
    #     print(group)
    #     print('-' * 40)

    print(f'{solve(groups)=}')
    test = '''abc'''
    print(f'{yes_count_every(test)=}')
    print(f'{solve_part2(groups)=}')
