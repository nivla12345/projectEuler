__author__ = 'Alvin'
import math
import string
import copy

import Tools
from SequentialSet import SequentialSet
from TwiceSquareSet import TwiceSquareSet
from PrimeSet import PrimeSet








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
# c = m**2 + n**2
# The conditions being:
# m > n
# m and n must be coprime
# m - n is odd
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


def p48():
    sum_powers = 0
    for i in xrange(1, 1001):
        sum_powers += pow(i, i)
    sum_powers_str = str(sum_powers)
    return sum_powers_str[len(sum_powers_str) - 10:]


def p49():
    # This dictionary maps 4 unique digits to the number of prime pandigital values that appear
    prime_pandigital_dict = dict()
    for i in xrange(1001, 9998):
        if Tools.is_prime(i):
            str_i = str(i)
            key = "".join(sorted(str_i))
            prime_pandigital_dict[key] = prime_pandigital_dict.get(key, []) + [i]
    # Iterate through keys find sequences with 2 or more differences
    sequences_with_dup_diffs = []
    for key in prime_pandigital_dict:
        choices = prime_pandigital_dict[key]
        num_choices = len(choices)
        if num_choices > 2:
            differences = []
            for i in xrange(1, num_choices):
                for j in xrange(i):
                    difference = choices[i] - choices[j]
                    if 4500 > difference:
                        differences.append(difference)
            duplicates = Tools.get_duplicates(differences)
            if len(duplicates):
                sequences_with_dup_diffs.append((choices, duplicates))
    # Test the duplicate differences
    qualifying_sequence = []
    for potential in sequences_with_dup_diffs:
        actual_numbers = potential[0]
        duplicates = potential[1]
        for duplicate in duplicates:
            for number in actual_numbers:
                potential_sum0 = number + duplicate
                potential_sum1 = potential_sum0 + duplicate
                if potential_sum0 in actual_numbers and potential_sum1 in actual_numbers:
                    qualifying_sequence.append(str(number) + str(potential_sum0) + str(potential_sum1))
    return qualifying_sequence


# Find the largest prime under 1 million that can be written as the sum of the most consecutive primes
def p50():
    list_prime = []
    set_prime = set()
    # Generate primes under 1,000,000.
    for i in xrange(2, 1000000):
        if Tools.is_prime(i):
            list_prime.append(i)
            set_prime.add(i)
    longest_sequence_length = 0
    longest_prime_sum = 0
    # Handle the 2 is prime case
    starting_prime = 2
    sequence_length = 1
    sum_longest_prime = starting_prime
    for i in xrange(2, len(list_prime), 2):
        sum_longest_prime += list_prime[i - 1] + list_prime[i]
        sequence_length += 2
        if sum_longest_prime in set_prime:
            if sequence_length > longest_sequence_length:
                longest_prime_sum = sum_longest_prime
                longest_sequence_length = sequence_length
    # Find the longest consecutive sequence
    for n in xrange(1, len(list_prime)):
        # generate sequence
        starting_prime = list_prime[n]
        sequence_length = 1
        sum_longest_prime = starting_prime
        for i in xrange(n + 2, len(list_prime), 2):
            sum_longest_prime += list_prime[i - 1] + list_prime[i]
            sequence_length += 2
            if sum_longest_prime in set_prime and sequence_length > longest_sequence_length:
                longest_prime_sum = sum_longest_prime
                longest_sequence_length = sequence_length
            if sum_longest_prime > 999999:
                break
    return longest_prime_sum


def p51_test(n, primes):
    num_digits = Tools.num_base_ten_digits(n) - 1
    num_transformations = pow(2, num_digits)
    # Iterates through the number of transformations
    for i in xrange(1, num_transformations):
        bin_val = bin(i)[2:]
        i_bin = '0' * (num_digits - len(bin_val)) + bin_val + '0'
        nine_choices = i_bin[0] == '1'
        # Zero out corresponding digits
        int_i_bin = int(i_bin)
        n_cp = zero_out_digits(n, int_i_bin, len(i_bin)) + nine_choices * int_i_bin
        n_cp_cp = n_cp
        # Start testing sequence
        sequence_length = 0
        for j in xrange(nine_choices, 10):
            if primes.contains_value(n_cp):
                sequence_length += 1
            n_cp += int_i_bin
        if sequence_length == 8:
            return n_cp_cp
    return 0


# Retursn n with the one digits in i_bin zeroed out
def zero_out_digits(n, i_bin, num_digits):
    n_copy = n
    running_subtractor = 0
    for i in xrange(num_digits):
        running_subtractor += (i_bin & 1) * (n_copy % 10) * pow(10, i)
        n_copy /= 10
        i_bin /= 10
    return n - running_subtractor


# Find the smallest prime where changing certain digits yields the largest prime
def p51():
    n = 4
    primes = PrimeSet((2, 3, 5, 7, 11), 0)
    while True:
        nth_prime = primes.get_nth(n)
        if p51_test(nth_prime, primes):
            return nth_prime
        n += 1


def p52_test(n):
    n_cmp = sorted(str(n))
    for i in xrange(2, 7):
        if n_cmp != sorted(str(i * n)):
            return False
    return True


def p52():
    track = 10
    while True:
        if p52_test(track):
            return track
        track += 1


def p53():
    factorials = [math.factorial(x) for x in range(101)]
    over_million_count = 0
    for n in xrange(2, 101):
        for r in xrange(2, n):
            if Tools.n_choose_r(n, r, factorials) > 1000000:
                over_million_count += 1
    return over_million_count


def p54_test(p1hand, p2hand):
    return False


def p54():
    p1_wins = 0
    with open('p054_poker.txt', 'r') as f:
        for line in f:
            cards = line.split()
            p1hand = cards[0:5]
            p2hand = cards[5:10]
            p1_wins += p54_test(p1hand, p2hand)
    return p1_wins


def p55_is_lychrel(n):
    for i in xrange(51):
        n = n + Tools.reverse_int(n)
        if Tools.is_palindrome(n):
            return False
    return True


# Find the number of lychrel numbers below 10000
def p55():
    num_lychrels = 0
    for i in xrange(1, 10000):
        num_lychrels += p55_is_lychrel(i)
    return num_lychrels


# Find the largest sum of digits for a^b where a and b < 100
def p56():
    max_digits = 0
    for a in xrange(1, 100):
        for b in xrange(1, 100):
            sum_digits = Tools.sum_digits(pow(a, b))
            if sum_digits > max_digits:
                max_digits = sum_digits
    return max_digits


def p57_calculate_sequence(seq):
    current_op = "a"
    seq.reverse()
    denum = seq[0]
    num = seq[1]
    seq = seq[2:]
    for i in seq:
        if current_op == "a":
            num += i * denum
            current_op = "d"
        else:
            num_tmp = num
            num = denum
            denum = num_tmp
            num *= i
            current_op = "a"
    new_fraction = Tools.simplify_fraction(num, denum)
    return Tools.num_base_ten_digits(new_fraction[0]) > Tools.num_base_ten_digits(new_fraction[1])


# Find the number of cases where the root 2 sequence has a greater numberator than denominator
def p57():
    ngd_count = 0
    sequence = [1, 1, 2]
    for i in xrange(1000):
        ngd_count += p57_calculate_sequence(copy.deepcopy(sequence))
        sequence = sequence + [1, 2]
    return ngd_count


def p58():
    current_val = 3
    current_level = 1
    num_primes = 0
    net_amount = 1
    add_by = 2
    while True:
        for j in xrange(4):
            num_primes += Tools.is_prime(current_val + j * add_by)
        net_amount += 4
        current_level += 2
        current_val += (add_by * 3 + add_by + 2)
        add_by += 2
        if float(num_primes) / net_amount < 0.1:
            return current_level


# Decrypt the p059_cipher.txt. The key consists of 3 lower case letters.
# My plan is to look for some common words: the_, be_, to_, of_, and and_
# If there is a single hit, I will record the results
def p59():
    encrypted_message = []
    common_word = set([" the ", "the ", " the", "the"
                                                " be ", "be ", " be", "be"
                                                                      " to ", "to ", " to", "to"
                                                                                            " of ", "of ", " of", "of"
                                                                                                                  " and ",
                       "and ", " and", "and"])
    # Extract encrypted message to list
    with open('p059_cipher.txt', 'r') as f:
        for line in f:
            encrypted_message = line.split(',')
    # Decrypt message with potential key
    for key0 in string.lowercase:
        for key1 in string.lowercase:
            for key2 in string.lowercase:
                key = key0 + key1 + key2
                decrypt_message = ""
                i = 0
                for letter in encrypted_message:
                    decrypt_message += chr(int(letter) ^ ord(key[i]))
                    i = (i + 1) % 3
                count_word = 0
                # Check if common words are in the decrypted message
                for word in common_word:
                    if word in decrypt_message:
                        count_word += 1
                    if count_word > 3:
                        return sum([ord(i) for i in decrypt_message])


p60_qualifying_sets = set()

# Find the smallest sum of a set of 5 primes that can be pairwise concatenated in any way and remain prime
def p60():
    prime_limit = 100000000
    primes = Tools.prime_sieve_atkins(prime_limit)
    prime_set = set(primes)
    # Get sub primes that can be concatenated both ways to form the largest prime
    sub_primes_dict = dict()
    # At this point, all the primes are double digit or more
    for prime_i in xrange(4, len(primes)):
        current_prime_str = str(primes[prime_i])
        for sub_i in xrange(1, len(current_prime_str)):
            sub0 = str(int(current_prime_str[:sub_i]))  # Objective in doing this is to lop off any leading 0's
            sub1 = str(int(current_prime_str[sub_i:]))
            sub0_int = int(sub0)
            sub1_int = int(sub1)
            if int(sub1 + sub0) in prime_set in prime_set and sub0_int in prime_set and sub1_int in prime_set:
                if sub0_int in sub_primes_dict:
                    sub_primes_dict[sub0_int].add(sub1_int)
                else:
                    sub_primes_dict[sub0_int] = set([sub1_int])
                if sub1_int in sub_primes_dict:
                    sub_primes_dict[sub1_int].add(sub0_int)
                else:
                    sub_primes_dict[sub1_int] = set([sub0_int])
    # Delete all keys and remove all values that don't have at least 4 different values
    for k in sub_primes_dict.keys():
        values = sub_primes_dict[k]
        if len(values) < 4:
            del sub_primes_dict[k]
        else:
            new_values = set()
            for v in values:
                if len(sub_primes_dict.get(v, [])) >= 4:
                    new_values.add(v)
            sub_primes_dict[k] = new_values
    # At this point, all the keys and values are possible solutions
    for i in sub_primes_dict:
        running_set = sub_primes_dict[i]
        p60_recurse_through((i,), running_set, sub_primes_dict, p60_qualifying_sets)
    min_sum = 999999999
    min_tuple = ()
    for i in p60_qualifying_sets:
        sum_i = sum(i)
        if sum_i < min_sum:
            min_sum = sum_i
            min_tuple = i
        print i
    print min_tuple
    return min_sum


def p60_recurse_through(qualifying_primes, intersections, sub_primes_dict, qualifying_sets):
    if len(qualifying_primes) >= 5:
        qualifying_sets.add(qualifying_primes)
    for prime in intersections:
        if set(qualifying_primes).issubset(sub_primes_dict[prime]):
            p60_recurse_through(qualifying_primes + (prime,),
                                intersections.intersection(sub_primes_dict[prime]),
                                sub_primes_dict,
                                qualifying_sets)


def p60_matches_requirement(prime_set, primes):
    for i in prime_set:
        for j in prime_set:
            if i == j:
                continue
            if int(str(i) + str(j)) not in primes or int(str(j) + str(i)) not in primes:
                print i, j
                return False
    return True