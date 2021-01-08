from collections import namedtuple
from typing import List, Set

Op = namedtuple('Op', ['number', 'move'])

def parse(line) -> Op:
    '''
    >>> parse('nop +0')
    Op(number=0, move=1)
    >>> parse('jmp +3')
    Op(number=0, move=3)
    >>> parse('jmp -3')
    Op(number=0, move=-3)
    >>> parse('acc +5')
    Op(number=5, move=1)
    '''
    op, n = line.split()
    number = int(n)
    if op  == 'nop':
        return Op(0, 1)
    elif op  == 'acc':
        return Op(number, 1)
    elif op  == 'jmp':
        return Op(0, number)
    else:
        raise ValueError(f'operation {op=}') 


class Runner:
    def __init__(self, lines: List[str]):
        self._lines = lines
        self._max_line_number = len(lines)
        self._acc = 0
        self._current_line = 0
        self._visited_lines: Set[int] = set()

    def clear(self):
        self._visited_lines.clear()
        self._acc = 0
        self._current_line = 0

    def run(self):
        next_line = self._current_line
        while True:
            if self._current_line in self._visited_lines:
                # print(f'line already visited: {next_line=}')
                break
            if  not (0 <= self._current_line < self._max_line_number):
                # print('out of bounds', f'{next_line=}')
                break

            self._visited_lines.add(self._current_line)

            line = self._lines[self._current_line]
            op = parse(line)
            self._acc += op.number
            self._current_line += op.move

        return self.accumulated

    @property
    def accumulated(self) -> int:
        return self._acc


if __name__ == '__main__':
    sample='''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''
    r = Runner(sample.splitlines())
    result = r.run()
    print(f'{result=}')
    with open('sample.txt') as f:
        puzzle_lines = [line.strip() for line in f]

    r2 = Runner(puzzle_lines)
    result_puzzle = r2.run()
    print(f'{result_puzzle=}')