def solve(txt):
    passports = txt.split('\n\n')
    required = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

    count = 0
    for c in passports:
        fields = set([kvp.split(':')[0] for kvp in c.split()])
        if required.issubset(fields):
            count += 1

    return count


def is_hgt_ok(hgt: str) -> bool:
    '''
    >>> is_hgt_ok('150cm')
    True
    >>> is_hgt_ok('150')
    False
    >>> is_hgt_ok('in')
    False
    >>> is_hgt_ok('190in')
    False
    >>> is_hgt_ok('70in')
    True
    '''
    def isok(unit, low, up):
        return (hgt.endswith(unit) and len(hgt) > 2
                and low <= int(hgt[:-2]) <= up)

    return isok('cm', 150, 193) or isok('in', 59, 76)


def is_xyr_ok(byr, iyr, eyr):
    '''
    >>> is_xyr_ok('2002', '2010', '2020')
    True
    >>> is_xyr_ok('2003', '2010', '2020')
    False
    >>> is_xyr_ok('192', '2010', '2020')
    False
    >>> is_xyr_ok('1920', '2010', '2020')
    True
    '''
    conds = [len(byr) == 4,
             len(iyr) == 4,
             len(eyr) == 4,
             1920 <= int(byr) <= 2002,
             2010 <= int(iyr) <= 2020,
             2020 <= int(eyr) <= 2030]

    return all(conds)


def is_hcl_ok(hcl):
    '''
    >>> is_hcl_ok('#123abc')
    True
    >>> is_hcl_ok('123abc')
    False
    '''
    if not (hcl.startswith('#') and len(hcl) == 7):
        return False

    def validchar(x):
        return ('a' <= x <= 'z') or ('0' <= x <= '9')

    return all(validchar(x) for x in hcl[1:])


def is_ecl_ok(ecl):
    '''
    >>> is_ecl_ok('amb')
    True
    >>> is_ecl_ok('fdz')
    False
    '''
    return ecl in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}


def is_pid_ok(pid):
    '''
    >>> is_pid_ok('000000001')
    True
    >>> is_pid_ok('00000001a')
    False
    '''
    return (len(pid) == 9 and
            all('0' <= x <= '9' for x in pid))


def solve2(txt):
    passports = txt.split('\n\n')
    required = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

    def isvalid(x):
        fields = dict([kvp.split(':') for kvp in x.split()])
        if not required.issubset(fields.keys()):
            return False

        f = fields
        return all([is_xyr_ok(f['byr'], f['iyr'], f['eyr']),
                    is_hgt_ok(f['hgt']),
                    is_ecl_ok(f['ecl']),
                    is_hcl_ok(f['hcl']),
                    is_pid_ok(f['pid'])])

    count = 0
    for passport in passports:
        if isvalid(passport):
            count += 1

    return count


if __name__ == '__main__':

    sample = '''ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
    byr:1937 iyr:2017 cid:147 hgt:183cm

    iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
    hcl:#cfa07d byr:1929

    hcl:#ae17e1 iyr:2013
    eyr:2024
    ecl:brn pid:760753108 byr:1931
    hgt:179cm

    hcl:#cfa07d eyr:2025 pid:166559648
    iyr:2011 ecl:brn hgt:59in'''

    print(f'{solve(sample)=}')

    with open('./puzzle-input.txt') as f:
        puzzleinput = f.read()

    print(f'{solve(puzzleinput)=}')

    with open('./sample-invalid.txt') as f:
        sampleinvalid = f.read()

    print(f'{solve2(sampleinvalid)=}')

    with open('./sample-valid.txt') as f:
        samplevalid = f.read()

    print(f'{solve2(samplevalid)=}')

    print(f'{solve2(puzzleinput)=}')
