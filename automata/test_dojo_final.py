import unittest

from dojofinal import *


class TestDojoFinal(unittest.TestCase):
    def test_rule_int_to_binary(self):
        rule_to_int = {
            1:  [0, 0, 0, 0, 0, 0, 0, 1],
            24: [0, 0, 0, 1, 1, 0, 0, 0],
        }

        for idx, arr in rule_to_int.items():
            self.assertEqual(int_to_rule(idx, 2 ** DEFAULT_LEN), arr)

    def test_indexes_centered(self):
        self.assertEqual(list(indexes_centered(2, 3)), [1, 2, 0])
        self.assertEqual(list(indexes_centered(3, 3)), [2, 0, 1])
        self.assertEqual(list(indexes_centered(0, 3)), [-1, 0, 1])

    def test_bin_to_index(self):
        bin_index = (
            [(0, 1, 1), 3],
            [(1, 1, 0), 6],
        )
        for inp, out in bin_index:
            self.assertEqual(bin_to_index(inp), out)

    def test_next_val_rule24(self):
        triple_to_val = {
            (0, 0, 0): 0,
            (1, 0, 1): 0,
            (0, 1, 1): 1,
            (1, 0, 0): 1,
        }

        for inp, out in triple_to_val.items():
            self.assertEqual(Line().next_cell(inp), out)

    def test_simple_transformation(self):
        ll = [0, 0, 0, 0]
        self.assertEqual(Line().next(ll), ll)

    def test_next_cell_idx(self):
        ll = [1, 0, 0]
        self.assertEqual(Line()._next(ll, 1), 1)

if __name__ == '__main__':
    unittest.main()

# Local Variables:
# compile-command: "python2 test_dojo_final.py"
# End:
