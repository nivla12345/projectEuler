__author__ = 'Alvin'

import math
import string

from contracts import pre_condition
from contracts import post_condition
from memoize import Memoize


PHI = (1 + math.sqrt(5)) / 2
ALL_DIGITS = string.digits + string.letters
PRIMES = set()


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
    if x in PRIMES:
        return True
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
    PRIMES.add(x)
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


# Performs Euclid's greatest common divisor problem
def euclid_gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


# Reduces a fraction to the lowest terms
@pre_condition(lambda numerator, denominator: type(numerator) is int and type(denominator) is int and denominator != 0)
@post_condition(lambda ret: type(ret) is tuple and len(ret) == 2)
def reduce_fraction(numerator, denominator):
    gcd = euclid_gcd(numerator, denominator)
    while gcd > 1:
        numerator /= abs(gcd)
        denominator /= abs(gcd)
        gcd = euclid_gcd(numerator, denominator)
    return numerator, denominator


permutation_sum_of_digits_factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]


@pre_condition(lambda n: type(n) is int)
@post_condition(lambda ret: type(ret) is int and ret > 0)
def permutation_sum_of_digits(n):
    if n == 0:
        return 1
    n = abs(n)
    sum_factorial_digits = 0
    while n > 0:
        sum_factorial_digits += permutation_sum_of_digits_factorials[n % 10]
        n /= 10
    return sum_factorial_digits


# Rotates to the right
def rotate_number(n, num_digits):
    digit_to_move = n % 10
    n /= 10
    n += digit_to_move * pow(10, num_digits-1)
    return n


@pre_condition(lambda n: type(n) is int and n >= 10)
def is_n_cycle_prime(n):
    num_digits = num_base_ten_digits(n)
    for i in xrange(num_digits):
        if not is_prime(n):
            return False
        n = rotate_number(n, num_digits)
    return True


# Generate all palindromes n digits long in order of size
@pre_condition(lambda n: type(n) is int and n >= 1)
def generate_palindromes(n):
    if n == 1:
        return range(1, 10)
    even = n % 2
    iter_length = n/2
    starting_point = pow(10, iter_length-1)
    end_point = pow(10, iter_length)
    palindromes = range(starting_point, end_point)
    if not even:
        for i in xrange(len(palindromes)):
            palindromes[i] = int(str(palindromes[i]) + str(palindromes[i])[::-1])
        return palindromes
    else:
        odd_digits_palindromes = []
        for i in xrange(len(palindromes)):
            for j in xrange(10):
                odd_digits_palindromes.append(int(str(palindromes[i]) + str(j) + str(palindromes[i])[::-1]))
        return odd_digits_palindromes


# Converts a base 10 value x to the corresponding base
# Modified from a post on stack overflow
def int2base(x, base, digit_choices=ALL_DIGITS):
    if x < 0: sign = -1
    elif x == 0: return digit_choices[0]
    else: sign = 1
    x *= sign
    digits = []
    while x:
        digits.append(digit_choices[x % base])
        x /= base
    if sign < 0:
        digits.append('-')
    digits.reverse()
    return ''.join(digits)


# Prepends "0's" to the MSB position of the number.
# digits - the number of digits to display ie. the number of bits the specified value is
def int2base_disp_zeroes(x, base, digits, digit_choices=ALL_DIGITS):
    based_number = int2base(x, base, digit_choices)
    digit_length_difference = digits - len(based_number)
    if digit_length_difference > 0:
        return digit_length_difference*digit_choices[0] + based_number
    elif digit_length_difference < 0:
        return based_number[0:digits]
    else:
        return based_number


is_truncatable_prime_allowable_msd = set([2, 3, 5, 7])


def is_truncatable_prime(n):
    n = abs(n)
    if n < 10:
        return False
    otherside_truncate = n
    if not is_prime(n):
        return False
    otherside_truncate = reverse_int(reverse_int(otherside_truncate)/10)
    n /= 10
    while n > 0:
        if not is_prime(n):
            return False
        if not is_prime(otherside_truncate):
            return False
        otherside_truncate = reverse_int(reverse_int(otherside_truncate)/10)
        n /= 10
    return True


def reverse_int(n):
    sign = 1
    if n < 0:
        sign = -1
    return sign*int((str(n)[::-1]))


is_pandigital_constant_set = set(['1', '3', '2', '5', '4', '7', '6', '9', '8'])


# Returns whetehr a number is 1 through 9 pandigital
def is_pandigital(n):
    str_n = str(n)
    if len(str_n) != 9:
        return False
    return set(str_n) == is_pandigital_constant_set


def make_pandigital(n):
    pandigital_value = ""
    count = 1
    while len(pandigital_value) < 9:
        pandigital_value += str(count*n)
        count += 1
    return int(pandigital_value)


letters_2_numbers = dict()


def generate_letters_2_numbers():
    count = 0
    for letter in string.ascii_lowercase:
        count += 1
        letters_2_numbers[letter] = count


# Returns the alphabetic value of a word
def get_alphabetic_value_of_word(word):
    word_value = 0
    for letter in word:
        word_value += letters_2_numbers[letter]
    return word_value


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
