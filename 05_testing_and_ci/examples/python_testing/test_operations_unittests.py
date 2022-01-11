"""
Tests for mathematical operations functions.
"""
from operations import find_max, find_mean
from unittest import TestCase
import csv


class TestOperations(TestCase):
    """
    Test suite for mathematical operations functions.
    """
    def setUp(self):
        # Fixture
        self.data = [43, 32, 167, 18, 1, 209]

    # Unit test
    def test_find_max(self):
        """
        Test operations.find_max 
        """
        # Expected result
        expected_max = 209

        # Actual result
        actual_max = find_max(self.data)

        # Test
        self.assertEqual(actual_max, expected_max)

    # Unit test
    def test_find_mean(self):
        """
        Test operations.find_mean
        """
        # Expected result
        expected_mean = 78.33

        # Actual result
        actual_mean = find_mean(self.data)

        # Test
        self.assertAlmostEqual(actual_mean, expected_mean, 2)

    # Integration test
    def test_max_mean_compare(self):
        """
        Test if mean of a data set is always lesser than the maximum
        """
        maximum = find_max(self.data)
        mean = find_mean(self.data)

        # Test
        self.assertTrue(mean < maximum)

    # Regression test
    def test_average_reg(self):
        """
        Test operations.find_mean on a previously generated dataset
        """
        # Expected result
        f = open("average_data.csv")
        rows = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
        i = 0
        data, reference_mean = None, None
        for row in rows:
            if i == 0:
                data = row
            if i == 1:
                reference_mean = row
            i += 1

        # Actual result
        actual_mean = find_mean(data)

        # Test
        self.assertAlmostEqual(actual_mean, reference_mean[0], 2)
