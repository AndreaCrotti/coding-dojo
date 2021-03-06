__metaclass__ = type

import argparse
import sys

DEFAULT_RULE = 24
DEFAULT_LEN = 3


def int_to_rule(idx, rule_len):
    bin_st = bin(idx)[2:]
    return [int(x) for x in bin_st.zfill(rule_len)]


def bin_to_index(bin_list):
    bin_string_list = ''.join(map(str, bin_list))
    return int(bin_string_list, 2)


def indexes_centered(center, num, tot_len):
    """Yield num indexes around the center, wrapping around when going
    after the bound
    """
    assert num % 2 == 1, "need an odd number to center"
    mid = num // 2
    for i in range(center-mid, center+mid+1):
        if i <= 0:
            yield i
        else:
            yield i % tot_len


class Line:
    def __init__(self, rule=DEFAULT_RULE, rule_len=DEFAULT_LEN):
        self.rule_bits = rule_len
        self.rule_len = 2 ** rule_len
        self.rule = int_to_rule(rule, self.rule_len)

    def next_cell(self, sub_list):
        return self.rule[bin_to_index(sub_list)]

    def _next(self, current, idx):
        to_transform = [current[x] for x in
                        indexes_centered(idx, self.rule_bits, len(current))]
        return self.next_cell(to_transform)

    def next(self, current):
        return [self._next(current, idx) for idx in range(len(current))]


def parse_arguments():
    parser = argparse.ArgumentParser(description='play around with cellular automata')

    parser.add_argument('-r', '--rule',
        type=int,
        default=DEFAULT_RULE)

    parser.add_argument('start',
        type=int,
        help='starting point')

    return parser.parse_args()


if __name__ == '__main__':
    ns = parse_arguments()
    curr = int_to_rule(ns.start, 2 ** DEFAULT_LEN)
    while True:
        print(','.join(map(str, curr)))
        curr = Line(rule=ns.rule).next(curr)


# Local Variables:
# compile-command: "python2 test_dojo_final.py"
# End:
