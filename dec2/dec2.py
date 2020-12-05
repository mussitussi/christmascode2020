def dec2(xs) -> int:
    '''
    Examples:
    >>> dec2(['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc'])
    2
    '''
    nvalid = 0
    for x in xs:
        limits, (lett, _), password = x.split()
        n1, n2 = (int(n) for n in limits.split('-'))
        if n1 <= password.count(lett) <= n2:
            nvalid += 1

    return nvalid


if __name__ == '__main__':
    xs = ['1-3 a: abcde',
          '1-3 b: cdefg',
          '2-9 c: ccccccccc']

    r_part1_sample = dec2(xs)
    # print(xs)
    print(r_part1_sample)

    with open('./dec2-input.txt') as f:
        ys = [line.strip() for line in f]

    r_part1 = dec2(ys)
    print(r_part1)
