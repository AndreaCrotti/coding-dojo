import unittest

import dojo2


class TestDojo2(unittest.TestCase):
    def test_cell_only_zero_and_one(self):
        with self.assertRaises(AssertionError):
            cell = dojo2.Cell(2)

    def test_simplest_list_next(self):
        l = [0, 0, 0]
        self.assertEqual(dojo2.next(l), l)

    def test_not_as_simple(self):
        l = [0, 0, 1]
        self.assertEqual(dojo2.next(l), [1, 0, 0])

    def test_long_sequence_gives_correct_middle_value(self):
        l = [0] * 5
        l[2] = 1; l[0] = 1
        self.assertEqual(dojo2.next(l)[2], 0)

    def test_long_sequence_on_edge(self):
        l = [1, 0, 1, 0, 0]
        self.assertEqual(dojo2.next(l)[0], 0)

    def test_binary_tuple_to_int(self):
        bt = (0, 1, 1)
        self.assertEqual(dojo2.tuple_to_int(bt), 3)

    def test_very_long_string(self):
        ll = [0] * 100
        self.assertEqual(dojo2.next(ll), ll)
        ll[50] = 1
        self.assertEqual(dojo2.next(ll)[51], 1)

    def test_equal_line_equal(self):
        l1 = dojo2.Line([dojo2.Cell(0)])
        l2 = dojo2.Line([dojo2.Cell(0)])
        self.assertEqual(l1, l2)

    def test_cell_equals(self):
        c1 = dojo2.Cell(1)
        c2 = dojo2.Cell(1)
        self.assertEqual(c1, c2)

    def test_simple_converging_one_step(self):
        l = [0, 0, 0]
        self.assertEqual(dojo2.is_converging(l), 1)


if __name__ == '__main__':
    unittest.main()

# Local Variables:
# compile-command: "python2 test_dojo2.py"
# End:
