import unittest

import dojo1


class TestDojo1(unittest.TestCase):
    def test_all0_gives_0(self):
        self.assertEqual(dojo1.future([0, 0, 0]), 0)

    def test_mixed(self):
        t = [1, 1, 0]
        self.assertEqual(dojo1.future(t), 0)

    def test_next_takes_3_elements(self):
        with self.assertRaises(AssertionError):
            dojo1.future(range(10))

    def test_simplest_list_next(self):
        l = [0, 0, 0]
        self.assertEqual(dojo1.next(l), l)

    def test_not_as_simple(self):
        l = [0, 0, 1]
        self.assertEqual(dojo1.next(l), [1, 0, 0])

    def test_next_pass_only_zero_and_one(self):
        with self.assertRaises(AssertionError):
            self.assertEqual(len(dojo1.next(range(5))), 5)

    def test_next_same_size(self):
        self.assertEqual(len(dojo1.next([1] * 5)), 5)

    def test_long_sequence_gives_correct_middle_value(self):
        l = [0] * 5
        l[2] = 1; l[0] = 1
        self.assertEqual(dojo1.next(l)[2], 0)

    def test_long_sequence_on_edge(self):
        l = [1, 0, 1, 0, 0]
        self.assertEqual(dojo1.next(l)[0], 0)


if __name__ == '__main__':
    unittest.main()
