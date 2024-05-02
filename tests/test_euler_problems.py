from euler_lib import *


def test_sum_of_digits():
    assert sum_of_digits(100) == 1
    assert sum_of_digits(12) == 3
    assert sum_of_digits(0) == 0
    assert sum_of_digits(99) == 18
def test_factorial():
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(5) == 120
def test_isLeapYear():
    assert isLeapYear(1900) == False
    assert isLeapYear(1989) == False
    assert isLeapYear(2000) == True
    assert isLeapYear(1988) == True
def test_day_in_month():
    assert days_in_month(2,2000) == 29
    assert days_in_month(3,2000) == 31
    assert days_in_month(6) == 30
    assert days_in_month(12) == 31