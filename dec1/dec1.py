from typing import Dict, Iterable


def dec1_2(xs):
    '''
    The product of two expenses that sums to 2020
    Examples:
    >>> dec1_2([1721 , 979 , 366 , 299 , 675 , 1456])
    514579
    >>> dec1_2([1, 2, 3])
    '''
    for i, x1 in enumerate(xs[:-1]):
        for x2 in xs[i + 1:]:
            if x1 + x2 == 2020:
                return x1 * x2


def dec1_2_order_n(xs: Iterable[int], t: int):
    '''
    O(N) version instead of naive O(N2), using a dictionary
    which has O(1) lookup time to reuse checks
    "rewrite" sum rule:
    xi + xj = t, i /= j <=>
    xi = t - xj, i /=j
    and store t - xj as we go along for fast lookups
    Example:
    xs = [5, 1, 10, 9]
    t = 10
    steps:
    prev = {}
    x0 = 5
    prev.get(x0) -> None -> prev = {t - x0: x0} = {5: 5}
    x1 = 1
    prev.get(x1) -> None -> prev = {9: 1, 5: 5}
    x2 = 10
    prev.get(x2) -> None -> prev = {0: 10, 9: 1, 5: 5}
    x3 = 9
    prev.get(x3) -> 1 -> return 9 * 1
    '''
    lookup: Dict[int, int] = {}
    for xi in xs:
        xj = lookup.get(xi)
        if xj is not None:
            return xi * xj
        lookup[t - xi] = xi


def dec1_3(xs):
    '''
    The product of three  expenses that sums to 2020
    Examples:
    >>> dec1_3([1721 , 979 , 366 , 299 , 675 , 1456])
    241861950
    >>> dec1_3([1, 2, 3])
    '''
    for i1, x1 in enumerate(xs[:-2]):
        for i2, x2 in enumerate(xs[i1 + 1:-1], i1 + 1):
            for x3 in xs[i2 + 1:]:
                if x1 + x2 + x3 == 2020:
                    return x1 * x2 * x3


if __name__ == '__main__':
    xs = [1721, 979, 366, 299, 675, 1456]

    r2_sample = dec1_2(xs)
    print('sample answer (2 expenses):', r2_sample)

    with open('./dec1-input.txt') as f:
        ys = [int(line.strip()) for line in f]

    r2 = dec1_2(ys)
    print('answer (O(N^2))(2 expenses)', r2)

    r2_on = dec1_2_order_n(ys, 2020)
    print('answer (O(N))(2 expenses)', r2_on)

    r3_sample = dec1_3(xs)
    print('sample answer (3 expenses):', r3_sample)

    r3 = dec1_3(ys)
    print('answer (3 expenses)', r3)
