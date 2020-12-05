def dec2(xs) -> int:
    '''
    Examples:
    >>> dec2(['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc'])
    2
    '''
    nvalid = 0
    for x in xs:
        (n1, _, n2), (lett, _), password = x.split()
        if int(n1) <= password.count(lett) <= int(n2):
            nvalid += 1

    return nvalid


if __name__ == '__main__':
    xs = ['1-3 a: abcde',
          '1-3 b: cdefg',
          '2-9 c: ccccccccc']

    r = dec2(xs)
    print(xs)
    print(r)
