"""
Tests for mathematical operations functions.
"""

from operations import find_max, find_average
import pytest
import csv


# Unit test
def test_find_max():
    data = [43, 32, 167, 18, 1, 209]
    expected_result = 209
    actual_result = find_max(data)
    assert actual_result == expected_result


# Unit test
def test_find_average():
    data = [43, 32, 167, 18, 1, 209]
    expected_result = 78.33
    # expected_result = pytest.approx(78.3, abs=0.01)
    actual_result = find_average(data)
    assert actual_result == expected_result


# Integration test
def test_max_avg_compare():
    """
    Test to check that the average of a data set is always lesser than the maximum
    """
    data = [43, 32, 167, 18, 1, 209]
    maximum = find_max(data)
    average = find_average(data)
    assert average < maximum


# Regression test
def test_average_reg():
    f = open("average_data.csv")
    rows = csv.reader(f)
    data = float(rows[0])
    old_average = float(rows[1])

    actual_average = find_avergae(data)
    expected_result = pytest.approx(old_average, abs=0.01)
    assert actual_average == expected_result
