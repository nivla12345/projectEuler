__author__ = 'Alvin'
import Tools
import math
from memoize import Memoize
# The problems that aren't in here were simple enough to do in the python command line.


# Find the number of different ways one can make 2 pounds given the following coins:
# 200, 100, 50, 20, 10, 5, 2, 1
# M = c0*x0 + c1*x1 + c2*x2 ....
# I have just written a generic solution for this problem
def p31():
    return Tools.generic_ways_to_make_target(200, (200, 100, 50, 20, 10, 5, 2, 1))


product_set = set()


def permute_over_values(choices, running_permutation):
    if not choices:
        p144 = int(running_permutation[0]) * int(running_permutation[1:5])
        if p144 == int(running_permutation[5:]):
            product_set.add(p144)
        p333 = int(running_permutation[0:3]) * int(running_permutation[3:6])
        if p333 == int(running_permutation[6:]):
            product_set.add(p333)
        p324 = int(running_permutation[0:3]) * int(running_permutation[3:5])
        if p324 == int(running_permutation[5:]):
            product_set.add(p324)
        return
    for i in xrange(len(choices)):
        permute_over_values(choices[0:i] + choices[i + 1:], running_permutation + str(choices[i]))


# Return the number of pandigital products ie. factor0 * factor1 = product where
# the digits of factor0, factor2 and product exactly comprise the digits 1-10
def p32():
    # Iterate over all permutations of 1-9
    permute_over_values((1, 2, 3, 4, 5, 6, 7, 8, 9), "")
    return sum(product_set)


# Consider the fraction 49/98. This fraction is unusual where if you were to remove a 9 in the numerator and a 9 in the
# denominator, you'd get the same reduced fraction. There are 4 such fraction with 2 digits in the numerator and
# denominator that are less than 1. Find the denominator of the product of these 4 fractions.
def p33():
    qualifying_fractions = set()
    for denominator in xrange(11, 100):
        for numerator in xrange(10, denominator):
            current_fraction = Tools.reduce_fraction(numerator, denominator)
            if numerator % 10 == 0 or denominator % 10 == 0:
                continue
            n0 = numerator / 10
            n1 = numerator % 10
            d0 = denominator / 10
            d1 = denominator % 10
            # At this point, all denominator values are non-zero
            if n0 == d0:
                if Tools.reduce_fraction(n1, d1) == current_fraction:
                    qualifying_fractions.add((numerator, denominator))
            if n0 == d1:
                if Tools.reduce_fraction(n1, d0) == current_fraction:
                    qualifying_fractions.add((numerator, denominator))
            if n1 == d0:
                if Tools.reduce_fraction(n0, d1) == current_fraction:
                    qualifying_fractions.add((numerator, denominator))
            if n1 == d1:
                if Tools.reduce_fraction(n0, d0) == current_fraction:
                    qualifying_fractions.add((numerator, denominator))
    final_fraction = [1, 1]
    for i in qualifying_fractions:
        final_fraction[0] *= i[0]
        final_fraction[1] *= i[1]
    return Tools.reduce_fraction(final_fraction[0], final_fraction[1])[1]


# Find the sum of all numbers who's factorial sum of digits is equal to the number itself.
def p34():
    # This value is 7 digits meaning that any further values will cannot mathematically reach that value
    maximum_possible_number = 7*math.factorial(9)
    sum_of_qualifying_numbers = 0
    for i in xrange(10, maximum_possible_number):
        if Tools.permutation_sum_of_digits(i) == i:
            sum_of_qualifying_numbers += i
    return sum_of_qualifying_numbers


p35_viable_values = (1, 3, 7, 9)


def generate_and_test_cycle_primes(current_number, target_length):
    if Tools.num_base_ten_digits(current_number) == target_length:
        return Tools.is_n_cycle_prime(current_number)
    count_cycle_primes = 0
    for i in p35_viable_values:
        count_cycle_primes += generate_and_test_cycle_primes(current_number*10 + i, target_length)
    return count_cycle_primes


# Count the number of primes under 1,000,000 whose entire cycle is prime
def p35():
    number_of_cycle_primes = 0
    for i in xrange(1, 10):
        number_of_cycle_primes += Tools.is_prime(i)
    # Now we can iterate over only the logical values
    # Iterate from 2 digits to 5 digits
    for i in xrange(2, 7):
        number_of_cycle_primes += generate_and_test_cycle_primes(0, i)
    return number_of_cycle_primes


def p36():
    sum_binary_and_decimal = 0
    for i in xrange(1, 7):
        palindromes = Tools.generate_palindromes(i)
        for p in palindromes:
            binary_p = bin(p)[2:]
            if binary_p == binary_p[::-1]:
                sum_binary_and_decimal += p
    return sum_binary_and_decimal