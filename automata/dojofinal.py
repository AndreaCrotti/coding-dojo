DEFAULT_RULE = 24
DEFAULT_LEN = 3


def int_to_rule(idx, rule_len):
    bin_st = bin(idx)[2:]
    return map(int, bin_st.zfill(rule_len))


def bin_to_index(bin_list):
    bin_string_list = ''.join(map(str, bin_list))
    return int(bin_string_list, 2)


def indexes_centered(center, num):
    """Yield num indexes around the center, wrapping around when going
    after the bound
    """
    assert num % 2 == 1, "need an odd number to center"
    mid = num / 2
    for i in range(center-mid, center+mid+1):
        if i <= 0:
            yield i
        else:
            yield i % num


class Line(object):
    def __init__(self, rule=DEFAULT_RULE, rule_len=DEFAULT_LEN):
        self.rule = rule
        self.rule_bits = rule_len
        self.rule_len = 2 ** rule_len

    def next_cell(self, sub_list):
        rule = int_to_rule(self.rule, self.rule_len)
        return rule[bin_to_index(sub_list)]

    def next(self, current):
        def _transform(cell_idx):
            to_transform = [current[x] for x in indexes_centered(cell_idx, self.rule_bits)]
            return self.next_cell(to_transform)

        return [_transform(idx) for idx in range(len(current))]


# Local Variables:
# compile-command: "python2 test_dojo_final.py"
# End:
