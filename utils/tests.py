import unittest

from fancy_time_formatting import *


class TestFancyTimeFormatting(unittest.TestCase):
    def test_fancy_time_to_seconds(self):
        test_case = [0, 1, 5, 10, 60, 90, 130, 360, 13000]
        result = [fancy_time_to_seconds(x) for x in test_case]
        solution = [0, 1, 5, 10, 60, 90, 90, 240, 5400]

        self.assertEqual(
            result,
            solution,
            result
        )

    def test_seconds_to_compact_time_string(self):
        test_case = [0, 5, 60, 90, 3600, 3600 * 49]
        result = [seconds_to_compact_time_string(x) for x in test_case]
        solution = ['0s', '5s', '1m', '1m30s', '1h', '2d1h']

        self.assertEqual(
            result,
            solution,
            result
        )

    def test_seconds_to_time_string(self):
        test_case = [0, 5, 60, 90, 3600, 3600 * 49]
        result = [seconds_to_time_string(x) for x in test_case]
        solution = ['0s', '5s', '1m 0s', '1m 30s', '1h 0m 0s', '2d 1h 0m 0s']

        self.assertEqual(
            result,
            solution,
            result
        )
