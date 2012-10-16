DEFAULT_RULE = 24
DEFAULT_LEN = 3
RULE_LEN = 2 ** 3


def int_to_rule(idx):
    bin_st = bin(idx)[2:]
    return map(int, bin_st.zfill(RULE_LEN))


def bin_to_index(bin_list):
    bin_string_list = ''.join(map(str, bin_list))
    return int(bin_string_list, 2)


def next_cell(current, rule=DEFAULT_RULE):
    rule = int_to_rule(rule)
    return rule[bin_to_index(current)]


def next_line(current, rule=DEFAULT_RULE):
    def _prev(idx): return idx - 1

    def _next(idx): return (idx+1) % 2

    def _transform(cell_idx):
        to_transform = [current[_prev(cell_idx)],
                        current[cell_idx],
                        current[_next(cell_idx)]]

        return next_cell(to_transform, rule)

    return map(_transform, current)


# Local Variables:
# compile-command: "python2 test_dojo_final.py"
# End:
