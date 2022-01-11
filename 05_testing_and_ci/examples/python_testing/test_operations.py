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
    # expected_result = pytest.approx(78.3, abs=0.01)
    
    # Actual result
    actual_mean = find_mean(data)
    
    # Test
    assert actual_mean == expected_mean


# Integration test
def test_max_mean_compare():
    """
    Test if mean of a data set is always lesser than the maximum
    """
    # Fixture
    data = [43, 32, 167, 18, 1, 209]
    
    maximum = find_max(data)
    mean = find_mean(data)
    
    # Test
    assert mean < maximum


# Regression test
def test_mean_reg():
    """
    Test operations.find_mean on a previously generated dataset
    """
    # Fixture

    f = open("average_data.csv")
    rows = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    i = 0
    for row in rows:
        if i == 0:
            data = row
        if i == 1:
            reference_mean = row
        i += 1

    # Actual result
    actual_mean = find_mean(data)
    
    # Expected result
    expected_mean = pytest.approx(reference_mean, abs=0.01)
    
    # Test
    assert actual_mean == expected_mean
