__author__ = 'Alvin'
import math
import string

import Tools
from SequentialSet import SequentialSet
from TwiceSquareSet import TwiceSquareSet


# The problems that aren't in here were simple enough to do in the python command line.


# Find the number of different ways one can make 2 pounds given the following coins:
# 200, 100, 50, 20, 10, 5, 2, 1
# M = c0*x0 + c1*x1 + c2*x2 ....
# I have just written a generic solution for this problem
# def p31():
# return Tools.generic_ways_to_make_target(200, (200, 100, 50, 20, 10, 5, 2, 1))
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
    maximum_possible_number = 7 * math.factorial(9)
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
        count_cycle_primes += generate_and_test_cycle_primes(current_number * 10 + i, target_length)
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
        end_point = pow(10, i - 1) * 9
        for n in xrange(start_point, end_point, -1):
            pandigital = Tools.make_pandigital(n)
            if Tools.is_pandigital(pandigital):
                return pandigital


# Find the perimeter of a right triangle that yields the most pythagorian triplets.
# The algorithm here is to generate only pythagorian triplets. I do so by using Euclid's algorithm where:
# a = k * (m**2 - n**2)
# b = k * (2*m*n)
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
    num_perfect_square = [0] * 1001
    # This bound was derived given m = 31 would yield an a + b + c > 1000
    for m in xrange(2, 32):
        # Iterating up to m satisfies the m > n condition
        m_minus_n_odd = m % 2
        for n in xrange(1 + m_minus_n_odd % 2, m, 2):
            if Tools.euclid_gcd(m, n) != 1:
                continue
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n
            perimeter = a + b + c
            if perimeter > 1000:
                continue
            num_perfect_square[perimeter] += 1
            k = 2
            perimeter_copy = perimeter * k
            while perimeter_copy < 1000:
                num_perfect_square[perimeter_copy] += 1
                k += 1
                perimeter_copy = perimeter * k
    return num_perfect_square.index(max(num_perfect_square))


# Given a decimal consisting of concatenating consecutive decimal values, find d1*d10*...*d1000000
# Extremely lazy method... of brutally constructing the string
def p40():
    d = "."
    count = 1
    while len(d) < 1000001:
        d += str(count)
        count += 1
    return int(d[1]) * int(d[10]) * int(d[100]) * int(d[1000]) * int(d[10000]) * int(d[100000]) * int(d[1000000])


# Generates pandigital numbers and returns the largest prime
def generate_largest_pandigital_prime(available_digits="7654321", running_number=""):
    if available_digits == "":
        pandigital = int(running_number)
        if Tools.is_prime(pandigital):
            return pandigital
        return 0
    for i in xrange(len(available_digits)):
        pandigital = generate_largest_pandigital_prime(
            available_digits[0:i] + available_digits[i + 1:],
            running_number + available_digits[i])
        if pandigital:
            return pandigital
    return 0


# This is kind of cheating. To properly test, I should loop starting from available_digits = [0:9]
# However, I was testing this and tried submitting this as an answer and it worked out.
def p41():
    return generate_largest_pandigital_prime()
    return int(d[1]) * int(d[10]) * int(d[100]) * int(d[1000]) * int(d[10000]) * int(d[100000]) * int(d[1000000])


# Find the number of words that form triangle numbers
def p42():
    words = []
    num_triangle_words = 0
    with open('p042_words.txt', 'r') as f:
        for line in f:
            words = line.split(',')
            break
    # Its unlikely that words will be larger than this value
    triangle_numbers_to_generate = 1000
    tri_numbers = set()
    # Generate triangle numbers
    for i in xrange(1, triangle_numbers_to_generate):
        tri_numbers.add(Tools.summation(i))
    Tools.generate_letters_2_numbers()
    # Iterate over words
    for word in words:
        word = word.strip('"').lower()
        num_triangle_words += Tools.get_alphabetic_value_of_word(word) in tri_numbers
    return num_triangle_words


# Constructs a dictionary of the following format:
# key (2 least significant digits for to test factors)
# value is a 2 element tuple
# 0) The current running potential pandigital number
# 1) The digits left to test
def p43_generate_next_dict(previous_dict, current_factor):
    i13dict = dict()
    for lsd2 in previous_dict:
        viable_digits = previous_dict[lsd2][1]
        for digit in viable_digits:
            potential_match = digit + lsd2
            if int(potential_match) % current_factor == 0:
                new_set = viable_digits.difference(set(digit))
                i13dict[digit + lsd2[0]] = (digit + previous_dict[lsd2][0], new_set)
    return i13dict


# Find the sum of all pandigital numbers who's 3 digit products are divisible by primes.
# In other words, find the pandigital number d1d2d3...d10 where the following mods = 0
# d2d3d4  % 2 
# d3d4d5  % 3
# d4d5d6  % 5 
# d5d6d7  % 7 
# d6d7d8  % 11
# d7d8d9  % 13
# d8d9d10 % 17
# My algorithm is to generate dictionaries of only divisible pandigital numbers
def p43():
    i17dict = dict()
    base_set = set(string.digits)
    i = 0
    # Generate a dictionary of choices for d8d9d10 that contain unique digits and are % 17.
    # The dictionary is described in p43_generate_next_dict
    while i * 17 < 1000:
        i7 = str(i * 17)
        i7 = (3 - len(i7)) * '0' + i7
        i7set = set(i7)
        if len(i7set) == 3:
            i17dict[i7[:2]] = (i7, base_set.difference(set(i7set)))
        i += 1
    # Iterate over the rest of the factors
    factors_to_test = (13, 11, 7, 5, 3, 2)
    dict_2_test = i17dict
    for factor in factors_to_test:
        dict_2_test = p43_generate_next_dict(dict_2_test, factor)
    # Sum up the remaining pandigital solutions.
    sum_pandigital_values = 0
    for value in dict_2_test.values():
        # At this point there's only a single digit that hasn't been tried yet
        digit_left = ""
        for i in value[1]:
            digit_left = i
        sum_pandigital_values += int(digit_left + value[0])
    return sum_pandigital_values


# Find the difference between the pair of numbers who's sum and difference is pentagonal
def p44():
    n = 2
    pentagonal_set = SequentialSet(1, 3)
    while True:
        pj = pentagonal_set.get_nth(n)
        n_pk = n - 1
        while True:
            pk = pentagonal_set.get_nth(n_pk)
            if pk < pentagonal_set.increment_by:
                break
            if pentagonal_set.contains_value(pj + pk, abs(pj - pk)):
                return abs(pj - pk)
            n_pk -= 1
        n += 1


# Find the number after 40755 that's a triangle, pentagonal, and hexagonal number
def p45():
    t = 40755
    p = 40755
    h = 40755
    tn = 285
    pn = 165
    hn = 143
    td = 1
    pd = 3
    hd = 4
    t_diff = tn + td
    p_diff = pn * pd + 1
    h_diff = hn * hd + 1
    t += t_diff
    p += p_diff
    h += h_diff
    h_diff += hd
    t_diff += td
    p_diff += pd
    while True:
        while h > p:
            p += p_diff
            p_diff += pd
        # If h == p, iterate t and test
        if h == p:
            while h > t:
                t += t_diff
                t_diff += td
            if t == p:
                return t
        # Otherwise, increment h and repeat
        h += h_diff
        h_diff += hd


def p46_test(composite, twice_square_set):
    nth_square = 0
    while True:
        twice_square = twice_square_set.get_nth(nth_square)
        if Tools.is_prime(composite - twice_square):
            return False
        if twice_square >= composite:
            return True
        nth_square += 1


# Find the largest odd composite that cannot be made from the sum of a prime and 2x a square
def p46():
    smallest_composite = 33
    twice_square_set = TwiceSquareSet()
    while True:
        if not Tools.is_prime(smallest_composite):
            if p46_test(smallest_composite, twice_square_set):
                return smallest_composite
        smallest_composite += 2


def p47():
    n = 644
    n0 = len(Tools.prime_factors(n))
    n1 = len(Tools.prime_factors(n + 1))
    n2 = len(Tools.prime_factors(n + 2))
    n3 = len(Tools.prime_factors(n + 3))
    while True:
        if n0 == n1 == n2 == n3 == 4:
            return n
        n += 1
        n0 = n1
        n1 = n2
        n2 = n3
        n3 = len(Tools.prime_factors(n + 3))