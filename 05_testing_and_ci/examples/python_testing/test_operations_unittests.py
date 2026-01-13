"""
Tests for mathematical operations functions.
"""
from operations import MathOperations
import unittest
from unittest import TestCase
from unittest.mock import MagicMock
import csv


class TestOperations(TestCase):
    """
    Test suite for mathematical operations functions.
    """
    def setUp(self):
        # Fixture
        self._data = [43, 32, 167, 18, 1, 209, 17]
        self._math_ops = MathOperations(self._data)

    # Unit test
    def test_find_max(self):
        """
        Test operations.find_max 
        """
        # Expected result
        expected_max = 209

        # Actual result
        actual_max = self._math_ops.find_max()

        # Test
        self.assertEqual(actual_max, expected_max)

    # Unit test
    def test_find_mean(self):
        """
        Test operations.find_mean
        """
        # Expected result
        expected_mean = 69.57

        # Actual result
        actual_mean = self._math_ops.find_mean()

        # Test
        self.assertAlmostEqual(actual_mean, expected_mean, 2)

    # Unit test
    def test_unit_find_median(self):
        """
        Test operations.find_median
        """
        # Expected result
        expected_median = 32

        # Mock reorder_data to isolate the test
        self._math_ops.reorder_data = MagicMock(return_value=[1, 17, 18, 32, 43, 167, 209])

        # Actual result
        actual_median = self._math_ops.find_median()

        # Test
        self.assertEqual(actual_median, expected_median)

    # Integration test
    def test_median(self):
        """
        Test operations.find_median
        """
        # Expected result
        expected_median = 32

        # Actual result
        actual_median = self._math_ops.find_median()

        # Test
        self.assertEqual(actual_median, expected_median)

    # Regression test
    def test_reg_reorder_data(self):
        """
        Test operations.reorder_data with data from CSV file
        """
        with open("reordered_data.csv") as f:
            rows = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
        
            for row in rows:
                expected_reordered_data = row

        # Actual result
        self._math_ops.reorder_data()
        actual_reordered_data = self._math_ops._data

        # Test
        self.assertEqual(actual_reordered_data, expected_reordered_data)

if __name__ == "__main__":
    # Run the tests
    unittest.main()
