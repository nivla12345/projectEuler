__author__ = 'Alvin'

import math

PHI = (1 + math.sqrt(5)) / 2


def fibonacci(n):
    """
    Takes the nth fibonacci.
    n: 1 -> 0
    n: 2 -> 1
    n: 3 -> 1
    n: 4 -> 2
    ...
    :param n: the number of fibonacci
    :return: nth fibonacci
    """
    return round((PHI ** n) / (PHI + 2))


def is_prime(x):
    if x <= 1:
        return False
    if x <= 3:
        return True
    if x % 2 == 0:
        return False
    root = int(math.sqrt(x))
    for i in xrange(3, root + 1, 2):
        if x % i == 0:
            return False
    return True


# Returns the number of distinct divisors
def num_divisors(n):
    if n <= 0:
        return 0
    if n <= 1:
        return 1
    if n <= 3:
        return 2
    divisor_count = 0
    n_root = int(math.sqrt(n))
    inc_by = 1
    if n % 2 != 0:
        inc_by = 2
    if (n_root * n_root) == n:
        divisor_count = 1
    for i in xrange(1, n_root, inc_by):
        if n % i == 0:
            divisor_count += 2
    return divisor_count


# Returns the number of distinct divisors
def sum_divisors(n):
    if n <= 1:
        return 0
    if n <= 3:
        return 1
    divisor_sum = 1
    n_root = int(math.sqrt(n))
    inc_by = 1
    if n % 2 != 0:
        inc_by = 2
    if (n_root * n_root) == n:
        divisor_sum += n_root
    else:
        n_root += 1
    for i in xrange(1, n_root, inc_by):
        if n % i == 0 and i != 1:
            divisor_sum += i
            divisor_sum += (n / i)
    return divisor_sum


def is_palindrome(n):
    n_string = str(n)
    n_string_reversed = n_string[::-1]
    return n_string == n_string_reversed


# Prints the rows of a grid for better displaying
def print_grid(grid):
    for i in grid:
        print i


# #######################################################################################################################
# Date functions
def is_leap_year(n):
    if n % 4 == 0:
        if n % 400 == 0:
            return True
        if n % 100 == 0:
            return False
        return True
    return False


NORMAL_DAYS_IN_MONTH = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}


# Returns the number of days in the month
# month is bound to [1:12]
def days_in_month(month, year):
    if is_leap_year(year) and month == 2:
        return 29
    return NORMAL_DAYS_IN_MONTH[month]

"""
# Returns what day of the week a given date was
# 0: monday, 1: tuesday, etc...
def date_to_day_of_week(day, month, year):
    # 1/1/1901 == Tuesday (1)
    # Everything will be done with respect to 1/1/1901
    before_or_after = before_after_or_equal(1, 1, 1901)
    if before_or_after == 1:
        # Find the number of days from day, month, year to 1/1/1901
        num_days_apart = days_apart(1, 1, 1901, day, month, year, True)
        return (1 + (num_days_apart % 7)) % 7
    elif before_or_after == -1:
        # Find the number of days from day, month, year to 1/1/1901
        num_days_apart = days_apart(1, 1, 1901, day, month, year, False)
        return (1 - (num_days_apart % 7)) % 7
    else:
        return 1


# Number of days 2 dates are apart
def days_apart(day0, month0, year0, day1, month1, year1, ba):
    # After
    if ba:
        years_apart = year0 - year1
        num_leap_years = num_leap_years_in_range(year0, year1)
    # Before
    else:
        years_apart = year1 - year0
        num_leap_years = num_leap_years_in_range(year1, year0)
    return (years_apart - num_leap_years) * 365 + num_leap_years * 364


# Returns the number of leap years in between a range
def num_leap_years_in_range(year0, year1):
    diff = (year1 % 400) - (year0 % 400)
    if diff <= 3:
        if is_leap_year(year0):
            return 1


# Year0 ? Year1
# After  == ? returns  1
# Equals == ? returns  0
# Before == ? returns -1
def before_after_or_equal(day0, month0, year0, day1, month1, year1):
    if year0 > year1:
        return 1
    elif year0 < year1:
        return -1
    else:
        if month0 > month1:
            return 1
        elif month0 < month1:
            return -1
        else:
            if day0 > day1:
                return 1
            elif day0 < day1:
                return -1
            else:
                return 0
"""