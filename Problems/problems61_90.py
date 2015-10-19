__author__ = 'Alvin'

import math
import copy
from fractions import Fraction

import Tools


def p61_fill_dict(starting_n, diff, inc, lsd_dict, msd_dict):
    while starting_n < 10000:
        str_starting_n = str(starting_n)
        lsd = int(str_starting_n[2:])
        if lsd > 9:
            if lsd in lsd_dict:
                lsd_dict[lsd].add(starting_n)
            else:
                lsd_dict[lsd] = set([starting_n])
            msd = int(str_starting_n[:2])
            if msd in msd_dict:
                msd_dict[msd].add(starting_n)
            else:
                msd_dict[msd] = set([starting_n])
        starting_n += diff
        diff += inc


def p61_get_lsd(n):
    return int(str(n)[2:])


def p61_get_msd(n):
    return int(str(n)[:2])


# Find the sum of the set of 6 4 digit numbers that cycle
def p61():
    # These lists contain dictionaries that map the least/most significant digits to the figurate number.
    lsd_dictionary_list = [None] * 6
    msd_dictionary_list = [None] * 6
    inc = 0
    # Fill figurate dictionaries
    # Starting figurates are the first figurate numbers that are 4 digits
    starting_figurates = [1035, 1024, 1001, 1035, 1071, 1045]
    starting_diffs = [46, 65, 79, 93, 106, 115]
    for i in xrange(6):
        inc += 1
        lsd_dict = dict()
        msd_dict = dict()
        p61_fill_dict(starting_figurates[i], starting_diffs[i], inc, lsd_dict, msd_dict)
        lsd_dictionary_list[i] = lsd_dict
        msd_dictionary_list[i] = msd_dict
    # Begin to construct working set
    octogonals = lsd_dictionary_list[5]
    cycle_lists = set()
    for octogonal_lsd in octogonals:
        values = octogonals[octogonal_lsd]
        for octogonal_value in values:
            cyclic_list = (octogonal_value,)
            octogonal_msd = p61_get_msd(octogonal_value)
            p61_find_cycle_set(octogonal_msd,
                               octogonal_lsd,
                               msd_dictionary_list[:5],
                               cyclic_list,
                               cycle_lists)
    return cycle_lists


def p61_find_cycle_set(octogonal_msd, this_msd, msd_dictionary_list, cyclic_tuple, cycle_lists):
    if len(cyclic_tuple) != len(set(cyclic_tuple)):
        return
    if len(cyclic_tuple) == 6:
        last_element = cyclic_tuple[-1]
        if octogonal_msd == p61_get_lsd(last_element):
            cycle_lists.add(cyclic_tuple)
        return
    for dictionary_i in xrange(len(msd_dictionary_list)):
        dictionary = msd_dictionary_list[dictionary_i]
        if this_msd in dictionary:
            for value in dictionary[this_msd]:
                next_msd = p61_get_lsd(value)
                next_msd_dict_list = msd_dictionary_list[:dictionary_i] + msd_dictionary_list[dictionary_i + 1:]
                p61_find_cycle_set(octogonal_msd, next_msd, next_msd_dict_list, cyclic_tuple + (value,), cycle_lists)


def p64_length(n):
    a = int(math.sqrt(n))
    a0 = a
    d = 1
    m = 0
    a_set = []
    while True:
        m = d * a - m
        d = (n - m ** 2) / d
        a = (a0 + m) / d
        if a == 2 * a0:
            a_set.append(a)
            return a_set
        a_set.append(a)


# Find the number of odd period length continued fraction representations for numbers under 10001
def p64():
    odd_period_count = 0
    for i in xrange(2, 10001):
        odd_period_count += (not Tools.is_perfect_square(i)) and (len(p64_length(i)) % 2)
    return odd_period_count


# Find the sum of the digits of the numerator of the continued fraction for the 100th term of e.
def p65():
    # Generate sequence
    e_list = [1, 1, 1] * 33
    e_list = e_list[:-1]
    add_by = 1
    for i in xrange(1, 100, 3):
        e_list[i] += add_by
        add_by += 2
    running_fraction = Fraction(1, 1)
    for i in reversed(e_list):
        running_fraction += i
        running_fraction = 1 / running_fraction
    e = 2 + running_fraction
    sum_numerator = 0
    for i in str(e.numerator):
        sum_numerator += int(i)
    return sum_numerator


# Given a Pell Equation, find the value of D that gives the maximum value of x for all minimal solutions.
# The gist of this solution is using a neat property involving continued fractions solving Pell Equations:
# The solution to the equation - "x**2 - d*y**2 = 1" - is Ak, Bk where k is the continued expansion of the continued
# fraction representation of d**0.5
def p66():
    max_d = 0
    max_x = 0
    for i in xrange(2, 1001):
        # Check if perfect square, skip if it is
        if int(i ** 0.5) ** 2 == i:
            continue
        # Get Akr, Bkr, and Ak2r, Bk2r
        solutions = p66_continued_fraction(i)
        x = solutions[0]
        if x > max_x:
            max_x = x
            max_d = i
    return max_d


# This function will
def p66_continued_fraction(x):
    a_list = []
    m = 0
    d = 1
    a0 = int(x ** .5)
    a = a0
    a_list.append(a)
    end_point = a0 << 1
    # First we will fill up a_list with the first sequence of a's and double this list if we need to
    while a != end_point:
        m = d * a - m
        d = (x - m ** 2) / d
        a = int((a0 + m) / d)
        a_list.append(a)
    a_list_len = len(a_list)
    # Construct the convergence coefficients
    r_len = a_list_len - 1
    even = False
    # If period is odd, we have to do more iterations and we need to extend the list being used accordingly
    if a_list_len % 2 == 0:
        even = True
        for i in xrange(1, a_list_len):
            a_list.append(a_list[i])
        a_list.append(a_list[1])
        r_len += a_list_len
    # Calculate p and q solution
    p = [0] * (r_len + 1)
    q = [0] * (r_len + 1)
    p[0] = a0
    p[1] = a0 * a_list[1] + 1
    q[0] = 1
    q[1] = a_list[1]
    for i in xrange(2, r_len + 1):
        p[i] = a_list[i] * p[i - 1] + p[i - 2]
        q[i] = a_list[i] * q[i - 1] + q[i - 2]
    if even:
        return p[a_list_len * 2 - 3], q[a_list_len * 2 - 3]
    return p[a_list_len - 2], q[a_list_len - 2]


# Find the largest string for a 5-gon adding up to 16
#
# The unwrapped indices will look as follows:
# graph index: 1 2 3 4 3 5 6 5 7 8 7 9 A 9 2
# index      : 0 1 2 3 4 5 6 7 8 9 A B C D E
# inner node :   i i   i i   i i   i i   i i
#
# This algorithm will work as follows:
#   0) Identify the element 1 by iterating from [6:1]. Remove
#
#   1) Using element 1 as an anchor, iterate over the permutation of the remaining available numbers and fill in element
#      2 and 3. At this point, we have identified the sum that can be used. We exclude 10 (*Note 10).
#
#   2) We will subtract the respective inner node from the current_sum and select from the remaining permutations.
#      This will be continued until the graph has been filled. If we iterate to the end, we jump back to 1).
#
#   3) If at any point in 2), there are no more valid digits, we return with no conclusive result and jump back to step
#      2). If we are able to fill out the graph in a valid manner, then the first answer we see is the correct answer
#      and we may halt the algorithm.
#
# An overview of the algorithm is that we work backwards from the largest possible combination of numbers to the first
# feasible 5-gon and that is our answer.
#
# Note 0: 10 cannot be an inner node otherwise it violates the 16 digit constraint.
#
# Running parameters:
# - Available digits == available_digits (bit array represented as an integer)
# - Current sum      == current_sum (int)
# - Current graph    == concatenated_graph (list)
# - Current index    == graph_index (int)
#
def p68():
    num_digits = 9

    for i in xrange(6, 0, -1):
        # Construct available_digits and remove the first node.
        available_digits = range(num_digits, 0, -1)
        del available_digits[num_digits - i]

        # Construct the current graph with the respective first elements in place.
        current_graph = [0] * 0xF
        current_graph[0] = i
        potential_answer = p68_construct_first_edge(available_digits, current_graph)
        if potential_answer:
            return potential_answer
    return []


# Here, we perform step 1) of the algorithm. We permute over the available_digits to find all candidates for elements 2
# and 3.
def p68_construct_first_edge(available_digits, current_graph):
    # How we got to 8 is we start with 10 available digits and subtract 1 for element 1 being used and subtract another
    # for how we can't use 10 (*Note 1).
    n_available_digits = 8

    # Hard code in the permutations as opposed to recursively generating only 2 permutations.
    for i in xrange(n_available_digits):
        # Select element 2
        element2 = available_digits[i]
        current_graph[1] = element2
        current_graph[-1] = element2

        # Construct latest available digits to use minus element 2.
        available_digits_e2 = copy.deepcopy(available_digits)
        del available_digits_e2[i]
        len_e2 = len(available_digits_e2)

        for j in xrange(len_e2):
            # Select element 3
            element3 = available_digits_e2[j]
            current_graph[2] = element3
            current_graph[4] = element3

            # Construct latest available digits to use minus element 3.
            available_digits_e3 = copy.deepcopy(available_digits_e2)
            del available_digits_e3[j]

            # Prepare to construct the remaining graph.
            current_sum = element2 + element3 + current_graph[0]
            graph_result = p68_construct_remaining_graph(current_sum, [10] + available_digits_e3, current_graph, 3)
            if graph_result:
                return graph_result
    return []


# At this point, we have the target sum, the available_digits, the graph with the appropriate digits, and the index to
# start from.
def p68_construct_remaining_graph(current_sum, available_digits, current_graph, current_index):
    # Base case we have a successful case
    if current_index == 0xC:
        last_digit = available_digits[0]
        # We have a successful graph.
        if (last_digit + current_graph[0xD] + current_graph[0xE]) == current_sum:
            current_graph[0xC] = last_digit
            return current_graph
        return []

    # Identify the remaining difference that needs to be filled to complete the graph.
    remaining_sum = current_sum - current_graph[current_index - 1]
    n_available_digits = len(available_digits)

    # Identify the outer node and consequently the inner node.
    for i in xrange(n_available_digits):
        outer_node = available_digits[i]
        if outer_node < current_graph[0]:
            continue

        # Perform checks on potential inner node
        potential_inner_node = remaining_sum - outer_node

        if potential_inner_node == outer_node or \
                        potential_inner_node not in available_digits or \
                        potential_inner_node == 10 or \
                        potential_inner_node > available_digits[0] or \
                        potential_inner_node <= 0:
            continue

        # Construct new available list
        available_digits_outer = copy.deepcopy(available_digits)
        del available_digits_outer[i]
        available_digits_outer.remove(potential_inner_node)

        # Update graph; no need to create a copy of the graph because the respective values will be written over.
        current_graph[current_index] = outer_node
        current_graph[current_index + 2] = potential_inner_node
        current_graph[current_index + 4] = potential_inner_node

        result = p68_construct_remaining_graph(current_sum, available_digits_outer, current_graph, current_index + 3)
        if result:
            return result
    return []


# Find the largest value for n = [1:1M] s.t. n / totient(n) is a maximum.
# Ultimately, find the largest product of consecutive prime factors that is less than 1M
def p69():
    million = 1000000
    primes = Tools.prime_sieve_atkins(100)
    current_product = primes[0]
    current_prime = primes[1]
    index = 1
    while current_product <= million:
        current_prime = primes[index]
        current_product *= current_prime
        index += 1
    return current_product / current_prime


# Find the n s.t. n/totient(n) is a minimum while totient(n) is a permutation of n.
# My solution was to generate products of pairs of primes and to search for an optimal totient result.
#
# Further optimization:
# This can actually be further optimized by searching for prime factors nearer sqrt(10M). However, I'm not very keen on
# guessing a window that would fit just right around the sqrt(10M) while at the same time I was too lazy to write a
# program that would dynamically expand the window should searching within too small a window failed.
def p70():
    upper_bound_ten_million = 10000000
    # Generate a list of products of primes.
    primes = Tools.prime_sieve_atkins(upper_bound_ten_million >> 1)
    prime_set = set(primes)
    product_primes = []
    num_primes = len(primes)
    for i in xrange(1, num_primes):
        i_val = primes[i]
        for j in xrange(i, num_primes):
            j_val = primes[j]
            current_index = i_val * j_val
            if current_index > upper_bound_ten_million:
                break
            product_primes.append(current_index)

    # Iterate through the product list to find the maximum totient value
    min_n_over_totient = 1.1
    min_index = 0
    for i in product_primes:
        current_totient = p70_totient(i, primes, prime_set)
        n_over_totient = float(i) / current_totient
        if min_n_over_totient > n_over_totient and Tools.is_permutation(current_totient, i):
            min_n_over_totient = n_over_totient
            min_index = i
    return min_index


# Uses euler's product formula to calculate the totient function.
# Euler's product formula:
# n * product((p - 1)/p) where p is are the primes that are <= n.
def p70_totient(n, primes, prime_set):
    orig_n = n
    limit = int(n ** 0.5)
    if n in prime_set:
        return n - 1
    running_denominator = 1
    running_numerator = 1
    for i in primes:
        if i > n:
            break
        if n % i == 0:
            running_numerator *= (i - 1)
            running_denominator *= i
            n /= i
    return orig_n * running_numerator / running_denominator


# Multiply numbers [1:1M] by 3.0/7 and check the upper round vs. lower round distance away from 3/7
def p71():
    million = 1000000
    three_over_seven = 3.0 / 7
    closest_numerator = 0
    delta = 10  # arbitrarily chosen large value
    # Set to 8 to skip 7 which is the base case. Will perform separate check if this isn't right.
    for i in xrange(3, million + 1):
        if i % 7 == 0:
            continue
        current_numerator = int(three_over_seven * i)
        current_value = float(current_numerator) / i
        current_delta = three_over_seven - current_value
        if current_delta < delta:
            delta = current_delta
            closest_numerator = current_numerator
    return closest_numerator


# Count the number of coprime elements under 1M
# My solution sums up the totient functions from [2:1M]
def p72():
    upper_limit = 100000
    # Generate a sorted list of products of primes.
    primes = Tools.prime_sieve_atkins(upper_limit)
    prime_set = set(primes)
    count = 0
    for i in xrange(2, upper_limit + 1):
        count += p70_totient(i, primes, prime_set)
    return count
