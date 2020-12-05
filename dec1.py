def dec1(xs):
    '''
    The product of two expenses that sums to 2020
    Examples:
    >>> dec1([1721 , 979 , 366 , 299 , 675 , 1456])
    514579
    >>> dec1([1, 2, 3])
    '''
    for i, x1 in enumerate(xs[:-1]):
        for x2 in xs[i + 1:]:
            if x1 + x2 == 2020:
                return x1 * x2


if __name__ == '__main__':
    xs = [1721, 979, 366, 299, 675, 1456]
    r = dec1(xs)
    print(r)
