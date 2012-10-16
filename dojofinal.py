DEFAULT_RULE = 24
DEFAULT_LEN = 3
RULE_LEN = 2 ** 3


def int_to_rule(idx):
    bin_st = bin(idx)[2:]
    return map(int, bin_st.zfill(RULE_LEN))


def bin_to_index(bin_list):
    bin_string_list = ''.join(map(str, bin_list))
    return int(bin_string_list, 2)


class Line(object):
    def __init__(self, rule=DEFAULT_RULE):
        self.rule = rule

    def next_cell(self, sub_list):
        rule = int_to_rule(self.rule)
        return rule[bin_to_index(sub_list)]

    def next_line(self, current):
        def _prev(idx): return idx - 1
        def _next(idx): return (idx+1) % 2

        def _transform(cell_idx):
            to_transform = [current[_prev(cell_idx)],
                            current[cell_idx],
                            current[_next(cell_idx)]]

            return self.next_cell(to_transform)

        return map(_transform, current)


# Local Variables:
# compile-command: "python2 test_dojo_final.py"
# End:
