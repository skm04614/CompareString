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
