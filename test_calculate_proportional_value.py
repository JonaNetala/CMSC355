# -*- coding: utf-8 -*-
# test_calculate_proportional_value.py
from proportionalrelationship import calculate_proportional_value

def test_calculate_proportional_value():
    assert calculate_proportional_value(10, 0.05) == 0.5
    assert calculate_proportional_value(5, 0.05) == 0.25
    assert calculate_proportional_value(10, 0.05) == 0.6
    # Add more test cases as needed
