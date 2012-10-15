from random import choice

RULE_24 = [0, 0, 0, 1, 1, 0, 0, 0]
# RULE_STUPID = [0] * 8

def tuple_to_int(bt):
    res = 0
    for idx, val in enumerate(reversed(bt)):
        res += val * (2 ** idx)
    return res


class Cell:
    def __init__(self, value):
        assert value == 0 or value == 1
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def next(self, prev, nxt):
        triple = [prev.value, self.value, nxt.value]
        return RULE_24[tuple_to_int(triple)]


class Line:
    def __init__(self, cells):
        self.cells = cells

    def __len__(self):
        return len(self.cells)

    def __eq__(self, other):
        return self.cells == other.cells

    def next(self):
        res = []
        for idx in range(len(self)):
            prev = self.cells[idx-1]
            nxt = self.cells[(idx+1) % len(self)]
            res.append(self.cells[idx].next(prev, nxt))

        return res


def next(lis):
    line = Line([Cell(x) for x in lis])
    return line.next()


def is_converging(lis, limit=1000):
    idx = 0
    old = Line([Cell(x) for x in lis])
    while idx < limit:
        after = Line([Cell(x) for x in old.next()])
        if old == after:
            return idx

        idx += 1
        old = after
        
    return False
        


def gen_random_sequence(length):
    return [choice([0, 1]) for _ in range(length)]


if __name__ == '__main__':
    size = 10
    for i in range(100):
        seq = gen_random_sequence(size)
        print("sequence %s is converging?: %s\n" % (str(seq), is_converging(seq)))
