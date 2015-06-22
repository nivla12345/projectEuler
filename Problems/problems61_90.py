__author__ = 'Alvin'
import math
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


