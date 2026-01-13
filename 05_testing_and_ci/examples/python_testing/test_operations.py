"""
Tests for mathematical operations functions.
"""

from operations import MathOperations
import pytest
import csv


@pytest.fixture
def math_operations():
    """
    Fixture for MathOperations class
    """
    data = [43, 32, 167, 18, 1, 209, 17]
    return MathOperations(data)

# Unit test
def test_find_max(math_operations):
    """
    Test operations.find_max 
    """
    # Expected result
    expected_max = 209

    # Actual result
    actual_max = math_operations.find_max()

    # Test
    assert actual_max == expected_max

# Unit test
def test_reorder_data(math_operations):
    """
    Test operations.reorder_data
    """
    # Expected result
    expected_data = [1, 17, 18, 32, 43, 167, 209]

    # Actual result
    math_operations.reorder_data()
    actual_data = math_operations._data

    # Test
    assert actual_data == expected_data

# Unit test
def test_find_mean(math_operations):
    """
    Test operations.find_mean
    """
    # Expected result
    expected_mean = 69.57

    # Actual result
    actual_mean = math_operations.find_mean()

    # Test
    assert actual_mean == expected_mean

# Integration test
def test_find_median(math_operations):
    """
    Test operations.find_median
    """   
    # Expected result
    expected_median = 32
    
    # Actual result
    actual_median = math_operations.find_median()
    
    # Test
    assert actual_median == expected_median


# Regression test
def test_reg_reorder_data(math_operations):
    """
    Test operations.reorder_data with data from CSV file
    """
    with open("reordered_data.csv") as f:
        rows = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    
        for row in rows:
            expected_reordered_data = row

    # Actual result
    math_operations.reorder_data()
    actual_reordered_data = math_operations._data

    # Test
    assert actual_reordered_data == expected_reordered_data
