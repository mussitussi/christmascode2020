from functools import reduce


def periodic(xs):
    n = len(xs)
    return lambda i: xs[i % n]


def dec3(rows):
    '''
    Examples
    >>> dec3(['..##.......',  '#...#...#..', '.#....#..#.', '..#.#...#.#', '.#...##..#.'])
    2
    '''
    return sum(1 for i, row in enumerate(rows[1:], start=1)
               if periodic(row)(i * 3) == '#')


def dec3_part2(rows, rds):
    def fun(rows, r, d):
        return sum(1 for i, row in enumerate(rows[d::d], start=1)
                   if periodic(row)(i * r) == '#')

    ncrosses = [fun(rows, r, d) for r, d in rds]
    prod = reduce(lambda a, b: a * b, ncrosses, 1)

    return prod, ncrosses


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
    print(f'part1: {r_sample_part1=}')

    with open('./dec3-input.txt') as f:
        rows = [row.strip() for row in f]

    r_part1 = dec3(rows)

    print(f'part1: {r_part1=}')

    rds = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    prod_sample, r_sample_part2 = dec3_part2(sample_rows, rds)
    print(f'part2: {prod_sample=}, {r_sample_part2=}')

    prod, r_part2 = dec3_part2(rows, rds)
    print(f'part2: {prod=}')
