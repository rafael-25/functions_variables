import pytest

def get_kth_digit(n,k):
    """
    Write the function get_kth_digit(n, k) which takes a possibly-negative int n and a
    non-negative int k, and returns the kth digit in n. The 0th digit is the rightmost digit,
    and counting goes right to left.
    """

def set_kth_digit(n,k,d):
    """
    Write the function setKthDigit(n, k, d) which takes a non-negative int n, a non-negative int k,
    and a non-negative single digit int d. Return the number n with the kth digit replaced with d.
    The 0th digit is the rightmost digit, and counting goes right to left.
    """

def test_get_kth_digit():
    assert get_kth_digit(95, 0) == 5
    assert get_kth_digit(2007, 1) == 0
    assert get_kth_digit(115, 2) == 1
    assert get_kth_digit(23023, 3) == 3
    assert get_kth_digit(19671969, 4) == 7
    assert get_kth_digit(19671969, 5) == 6
    assert get_kth_digit(19671969, 6) == 9
    assert get_kth_digit(19671969, 7) == 1


def test_set_kth_digit():
    assert set_kth_digit(5015,0,6) == 5016
    assert set_kth_digit(5015,1,4) == 5045
    assert set_kth_digit(5015,2,8) == 5815
    assert set_kth_digit(5015,3,9) == 9015
    
