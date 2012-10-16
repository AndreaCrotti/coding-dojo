import unittest

from dojofinal import *


class TestDojoFinal(unittest.TestCase):
    def test_rule_int_to_binary(self):
        rule_to_int = {
            1:  [0, 0, 0, 0, 0, 0, 0, 1],
            24: [0, 0, 0, 1, 1, 0, 0, 0],
        }

        for idx, arr in rule_to_int.items():
            self.assertEqual(int_to_rule(idx), arr)

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
        }

        for inp, out in triple_to_val.items():
            self.assertEqual(Line().next_cell(inp), out)


    def test_full_transformation(self):
        transf = (
            ([0, 0, 0, 0], [0, 0, 0, 0]),
        )

        for inp, out in transf:
            self.assertEqual(Line().next_line(inp), out)


if __name__ == '__main__':
    unittest.main()

# Local Variables:
# compile-command: "python2 test_dojo_final.py"
# End:
