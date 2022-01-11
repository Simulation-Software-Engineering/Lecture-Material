"""
Tests for mathematical operations functions.
"""

from operations import find_max, find_mean
import pytest
import csv


# Unit test
def test_find_max():
    """
    Test operations.find_max 
    """
    # Fixture
    data = [43, 32, 167, 18, 1, 209]

    # Expected result
    expected_max = 209

    # Actual result
    actual_max = find_max(data)

    # Test
    assert actual_max == expected_max


# Unit test
def test_find_mean():
    """
    Test operations.find_mean
    """
    # Fixture
    data = [43, 32, 167, 18, 1, 209]
    
    # Expected result
    expected_mean = 78.33
    # expected_result = pytest.approx(78.33, abs=0.01)
    
    # Actual result
    actual_mean = find_mean(data)
    
    # Test
    assert actual_mean == expected_mean


# Integration test
def test_max_mean():
    """
    Test if mean of a data set is always lesser than the maximum
    """
    # Fixture
    data1 = [43, 32, 167, 18, 1, 209]
    data2 = [3, 13, 33, 23, 498]

    # Expected result
    expected_mean = 353.5

    maximum1 = find_max(data1)
    maximum2 = find_max(data2)

    # Actual result
    actual_mean = find_mean([maximum1, maximum2])
    
    # Test
    assert actual_mean == expected_mean


# Regression test
def test_regression_mean():
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
    
    expected_mean = pytest.approx(reference_mean, abs=0.01)
    
    # Test
    assert actual_mean == expected_mean
