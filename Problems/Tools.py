__author__ = 'Alvin'

import math

from contracts import pre_condition
from contracts import post_condition
from memoize import Memoize


PHI = (1 + math.sqrt(5)) / 2


# Only works up to n == 1474
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
    return int(round((PHI ** n) / (PHI + 2)))


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


# Performs summation of positive integer n
def summation(n):
    if n <= 0:
        return 0
    if n & 1 == 0:
        return (n + 1) * (n >> 1)
    else:
        return (n + 1) * (n >> 1) + (n >> 1) + 1


# Returns a permutations lexicographic ordering
def check_permutation(p):
    count = len(p) - 1
    sum_p = 0
    digits = range(len(p))
    for i in xrange(len(p)):
        current_digit = int(p[i])
        digit = digits[current_digit]
        sum_p += digit * math.factorial(count)
        for j in xrange(current_digit + 1, len(digits)):
            digits[j] -= 1
        count -= 1
    return sum_p


# Counts the number of digits in a base 10 number.
def num_base_ten_digits(n):
    n = int(math.fabs(n))
    if n == 0:
        return 1
    num_digits = 0
    while n > 0:
        n /= 10
        num_digits += 1
    return num_digits


# Returns the cycle length of 1/d, if does not cycle returns 0
def get_cycle_length(divisor):
    count = 0
    dividend_length = dict()
    dividend = 1
    # Perform division, if there is a repeat dividend division then we have a cycle
    while dividend > 0:
        if dividend < divisor:
            dividend *= 10
        else:
            dividend = (dividend % divisor) * 10
        if dividend in dividend_length:
            return count - dividend_length[dividend]
        dividend_length[dividend] = count
        count += 1
    return 0


# Generic nth polynomial calculator, n is the value to plug into the polynomial and the variable args are the
# coefficients of the polynomial. Example:
# To calculate x^2 + 1 where x = 100
# nth_polynomial(100, 1, 0 , 1)
def nth_polynomial(n, *args):
    sum_polynomial = 0
    count = len(args) - 1
    for i in args:
        sum_polynomial += i * (n ** count)
        count -= 1
    return sum_polynomial


# Attempt at providing a generic solution to the how many ways can I make a dollar with X coins
# @param target refers to the amount that the arg coefficients are supposed to reach up to. ie. a dollar would be 100
# @param args is a generic value of coins. ie. a nickel would be 5 and a dollar coin would be 100. args must be sorted
@pre_condition(lambda target, args: target >= 0 and type(args) is tuple)
@post_condition(lambda ret: ret >= 0)
def generic_ways_to_make_target(target, args):
    if target == 0:
        return 1
    if len(args) == 0:
        return 0
    current_coin_value = args[0]
    # The current coin is larger than the target this means we should move on to the smaller coin
    if current_coin_value > target:
        return generic_ways_to_make_target(target, args[1:])
    if len(args) == 1:
        return target % current_coin_value == 0
    seen_values = 0
    while target >= 0:
        seen_values += generic_ways_to_make_target(target, args[1:])
        target -= current_coin_value
    return seen_values


generic_ways_to_make_target = Memoize(generic_ways_to_make_target)


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