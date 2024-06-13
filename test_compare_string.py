from unittest import TestCase

from compare_string import compare_string


class Test(TestCase):
    def test_invalid_arguments(self):
        invalid_arguments = ("ab", "a1", "12", "-")
        valid_argument = "A"

        with self.assertRaises(ValueError):
            for invalid_argument in invalid_arguments:
                compare_string(valid_argument, invalid_argument)
                compare_string(invalid_argument, valid_argument)

    def test_length(self):
        expected_to_argument_pairs = {
            60.0: (("AB", "CD"), ("EF", "ZO"), ("RC", "BQ")),
            60.0 * (1 - 2/5): (("AAABB", "CCD"),),
            60.0 * (1 - 1/3): (("AAB", "CC"),),
            0.0: (("A", "BCD"), ("RZAB", "QWERTYUIO"), ("ZXC", "ASDFGH")),
        }

        for expected, argument_pairs in expected_to_argument_pairs.items():
            for args in argument_pairs:
                self.assertEqual(expected, compare_string(*args))
