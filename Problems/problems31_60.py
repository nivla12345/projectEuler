__author__ = 'Alvin'
import Tools
import math
from memoize import Memoize
# The problems that aren't in here were simple enough to do in the python command line.


# Find the number of different ways one can make 2 pounds given the following coins:
# 200, 100, 50, 20, 10, 5, 2, 1
# M = c0*x0 + c1*x1 + c2*x2 ....
# I have just written a generic solution for this problem
# def p31():
#     return Tools.generic_ways_to_make_target(200, (200, 100, 50, 20, 10, 5, 2, 1))
#
# Attempt #2 at solving using dynamic programming
def p31():
    options = (1, 2, 5, 10, 20, 50, 100, 200)
    target_value = 200
    results = [0] * (target_value + 1)
    results[0] = 1
    for coin in options:
        for i in xrange(coin, target_value + 1):
            results[i] += results[i - coin]
    print results
    return results[target_value]


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


truncatable_prime_set = set()


# Find the sume of all 11 truncatable sums. My solution currently is quite slow (1.04 seconds).
# One method to speed things up:
# The MSD must be one of the following: 2, 3, 5, 7
# The LSD must be one of the following: 3, 7 (Done with the incrementing)
# The middle digits must be:  1, 3, 7, 9
def p37():
    count = 13
    num_truncatable_primes = 0
    sum_truncatable_primes = 0
    while num_truncatable_primes < 11:
        if Tools.is_truncatable_prime(count):
            sum_truncatable_primes += count
            num_truncatable_primes += 1
            truncatable_prime_set.add(count)
        lsd = count % 10
        if lsd == 3:
            count += 4
        else:
            count += 6
    return sum_truncatable_primes


# Find the largest concatenated pandigital number formed by n * (1, 2, 3...)
# My strategy is as follows (Its kind of cheating). The problem example gave an example of n = 9 and the resulting
# pandigital number was 918273645. I tested this number and its not the answer meaning that n's MSD must begin with 9.
# This means that I can eliminate 90% of the tests who's MSD are not 9.
def p38():
    # Number of digits for n
    for i in xrange(6, 2, -1):
        start_point = pow(10, i) - 1
        end_point = pow(10, i-1)*9
        for n in xrange(start_point, end_point, -1):
            pandigital = Tools.make_pandigital(n)
            if Tools.is_pandigital(pandigital):
                return pandigital


# Find the perimeter of a right triangle that yields the most pythagorian triplets.
# The algorithm here is to generate only pythagorian triplets. I do so by using Euclid's algorithm where:
#   a = k * (m**2 - n**2)
#   b = k * (2*m*n)
#   c = m**2 + n**2
# The conditions being:
#   m > n
#   m and n must be coprime
#   m - n is odd
#   k can be any integer
# See: https://en.wikipedia.org/wiki/Pythagorean_triple
# Instead of using a hashtable, I just used an array that used the index as a key. This takes up more space but given we
# have a finite number of perfect squares being 1001 this was affordable.
def p39():
    num_perfect_square = [0]*1001
    # This bound was derived given m = 31 would yield an a + b + c > 1000
    for m in xrange(2, 32):
        # Iterating up to m satisfies the m > n condition
        m_minus_n_odd = m % 2
        for n in xrange(1 + m_minus_n_odd % 2, m, 2):
            if Tools.euclid_gcd(m, n) != 1:
                continue
            a = m*m - n*n
            b = 2*m*n
            c = m*m + n*n
            perimeter = a + b + c
            if perimeter > 1000:
                continue
            num_perfect_square[perimeter] += 1
            k = 2
            perimeter_copy = perimeter*k
            while perimeter_copy < 1000:
                num_perfect_square[perimeter_copy] += 1
                k += 1
                perimeter_copy = perimeter*k
    return num_perfect_square.index(max(num_perfect_square))


# Given a decimal consisting of concatenating consecutive decimal values, find d1*d10*...*d1000000
# Extremely lazy method... of brutally constructing the string
def p40():
    d = "."
    count = 1
    while len(d) < 1000001:
        d = d + str(count)
        count += 1
    return int(d[1])*int(d[10])*int(d[100])*int(d[1000])*int(d[10000])*int(d[100000])*int(d[1000000])