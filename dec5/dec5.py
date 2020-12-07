def nextlowup(low, up, takelow):
    '''
    >>> nextlowup(0, 127, True)
    (0, 63)
    >>> nextlowup(0, 127, False)
    (64, 127)
    >>> nextlowup(0, 63, False)
    (32, 63)
    >>> nextlowup(32, 63, True)
    (32, 47)
    >>> nextlowup(32, 47, False)
    (40, 47)
    '''
    n = up - low + 1
    m = n // 2
    if takelow:
        return low, low + m - 1
    else:
        return low + m, up


def col(seatid):
    '''
    >>> col('BFFFBBFRRR')
    7
    >>> col('BBFFBBFRLL')
    4
    '''
    ys = seatid[-3:]
    up, low = 0, 7
    for y in ys:
        up, low = nextlowup(up, low, y == 'L')

    assert up == low
    return up


def row(seatid):
    '''
    >>> row('BFFFBBFRRR')
    70
    >>> row('FFFBBBFRRR')
    14
    '''
    ys = seatid[:7]
    up, low = 0, 127
    for y in ys:
        up, low = nextlowup(up, low, y == 'F')

    assert up == low
    return up


def solve(lines):
    return max(8 * row(seatid) +  col(seatid)
               for seatid in lines)


def readlines(fname):
    with open(fname) as f:
        return [line.strip() for line in f]


if __name__ == '__main__':
    print(f'{row("BFFFBBFRRR") = }')
    print(f'{row("FFFBBBFRRR") = }')
    print(f'{row("BBFFBBFRLL") = }')

    lines = readlines('./puzze-input.txt')
    print(f'{solve(lines) = }')
