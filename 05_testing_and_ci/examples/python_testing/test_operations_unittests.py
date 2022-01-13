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
        self.data1 = [43, 32, 167, 18, 1, 209]
        self.data2 = [3, 13, 33, 23, 498]

    # Unit test
    def test_find_max(self):
        """
        Test operations.find_max 
        """
        # Expected result
        expected_max = 209

        # Actual result
        actual_max = find_max(self.data1)

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
        actual_mean = find_mean(self.data1)

        # Test
        self.assertAlmostEqual(actual_mean, expected_mean, 2)

    # Integration test
    def test_mean_of_max(self):
        """
        Test operations.find_max and operations.find_mean
        """
        # Expected result
        expected_mean_of_max = 353.5

        maximum1 = find_max(self.data1)
        maximum2 = find_max(self.data2)

        # Actual result
        actual_mean_of_max = find_mean([maximum1, maximum2])
        
        # Test
        self.assertEqual(actual_mean_of_max, expected_mean_of_max)

    # Regression test
    def test_regression_mean(self):
        """
        Test operations.find_mean on a previously generated dataset
        """
        with open("mean_data.csv") as f:
            rows = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
            # Fixture
            data = next(rows)
            
            # Expected result
            reference_mean = next(rows)

        # Actual result
        actual_mean = find_mean(data)

        # Test
        self.assertAlmostEqual(actual_mean, reference_mean[0], 2)
