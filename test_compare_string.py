from unittest import TestCase

from compare_string import compare_string, length_comparison_score, similarity_score


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
                self.assertEqual(expected, length_comparison_score(*args))

    def test_similarity(self):
        expected_to_argument_pairs = {
            0.0: (("AB", "CD"), ("EF", "ZO"), ("RC", "BQ")),
            40.0: (("A", "A"), ("AB", "BAA"), ("ACAAB", "ABC"), ("XXXXXXY", "YXXXXX")),
            40.0 * 1/3: (("AAAAA", "ABC"), ("ABC", "C"), ("AABBCCDDEEFF", "ABABABAB")),
            40.0 * 3/7: (("ABCD", "ABXYZD"), ("AABBCCDDEEFFGG", "EAB"), ("XXXXXYZAAAAA", "XZRTAB"))
        }

        for expected, argument_pairs in expected_to_argument_pairs.items():
            for args in argument_pairs:
                self.assertEqual(expected, similarity_score(*args))

    def test_total_score(self):
        expected_to_argument_pairs = {
            100.0: (("AAAAB", "BABBB"), ("A", "A")),
            60.0: (("AB", "CD"), ("EF", "ZO"), ("RC", "BQ")),
            40.0 + 60.0 * (1 - 1/7): (("XXXXXXY", "YXXXXX"),),
            40.0: (("AB", "BAAAAA"), ("ACCCCCCAAB", "ABC")),
            0.0: (("AAAAB", "C"), ("XYZXYZXXYYZZ", "ASDF"), ("RXY", "M"))
        }

        for expected, argument_pairs in expected_to_argument_pairs.items():
            for args in argument_pairs:
                self.assertEqual(expected, compare_string(*args))
