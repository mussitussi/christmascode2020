

def periodic(xs):
    '''
    >>> periodic('abc')(3)
    'a'
    >>> periodic('abc')(-1)
    'c'
    '''
    n = len(xs)
    return lambda i: xs[i % n]


def dec3(rows):
    '''
    Examples
    >>> dec3(['..##.......',  '#...#...#..', '.#....#..#.', '..#.#...#.#', '.#...##..#.'])
    2
    '''
    ncrosses = 0
    p = 3
    for row in rows[1:]:
        if periodic(row)(p) == '#':
            ncrosses += 1
        p += 3

    return ncrosses


def dec3_part2():
    '''
    Examples
    '''
    pass


if __name__ == '__main__':
    samplemap = '''
    ..##.......
    #...#...#..
    .#....#..#.
    ..#.#...#.#
    .#...##..#.
    ..#.##.....
    .#.#.#....#
    .#........#
    #.##...#...
    #...##....#
    .#..#...#.#'''
    sample_rows = [r for x in samplemap.split('\n') if (r := x.strip())]

    r_sample_part1 = dec3(sample_rows)
    print(f'{r_sample_part1=}')

    with open('./dec3-input.txt') as f:
        rows = [row.strip() for row in f]

    r_part1  = dec3(rows)

    print(f'{r_part1=}')
