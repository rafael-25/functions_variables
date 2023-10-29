import pytest

def get_kth_digit(n,k):
    """
    Write the function get_kth_digit(n, k) which takes a possibly-negative int n and a
    non-negative int k, and returns the kth digit in n.
    The 0th digit is the rightmost digit, and counting goes right to left.
    """

def set_kth_digit(n,k,d):
    """
    Write the function setKthDigit(n, k, d) which takes a non-negative int n, a non-negative int k, 
    and a non-negative single digit int d. Return the number n with the kth digit replaced with d. 
    The 0th digit is the rightmost digit, and counting goes right to left.
    """

def test_get_kth_digit():
    assert get_kth_digit(100, 0) == 0
    assert get_kth_digit(819, 2) == 8
    assert get_kth_digit(1897, 1) == 9
    assert get_kth_digit(54321, 3) == 4
    assert get_kth_digit(987654321, 4) == 5
    assert get_kth_digit(12345, 0) == 5
    assert get_kth_digit(987654321, 0) == 1
    assert get_kth_digit(987654321, 8) == 9
    assert get_kth_digit(123, 1) == 2
    assert get_kth_digit(0, 0) == 0

def test_set_kth_digit():
    assert get_kth_digit(100, 0) == 0
    assert get_kth_digit(819, 2) == 8
    assert get_kth_digit(1897, 1) == 9
    assert get_kth_digit(54321, 3) == 4
    assert get_kth_digit(987654321, 4) == 5
    assert get_kth_digit(12345, 0) == 5
    assert get_kth_digit(987654321, 0) == 1
    assert get_kth_digit(987654321, 8) == 9
    assert get_kth_digit(123, 1) == 2
    assert get_kth_digit(0, 0) == 0
