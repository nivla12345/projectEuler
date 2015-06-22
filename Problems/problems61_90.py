__author__ = 'Alvin'


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


# Given a Pell Equation, find the value of D that gives the maximum value of x for all minimal solutions.
# The gist of this solution is using a neat property involving continued fractions solving Pell Equations:
# The solution to the equation - "x**2 - d*y**2 = 1" - is Ak, Bk where k is the continued expansion of the continued
# fraction representation of d**0.5
def p66():
    for i in xrange(2, 11):
        # Check if perfect square, skip if it is
        if int(i ** 0.5) ** 2 == i:
            continue
        # Get Akr, Bkr, and Ak2r, Bk2r
        solutions = p66_continued_fraction(i)
        Akr = solutions[0]
        Bkr = solutions[1]
        if Akr ** 2 - i * (Bkr ** 2) == 1:
            print 'i: ', i, ' x = ', Akr, ' y = ', Bkr
            continue
        print 'i: ', i, ' x = ', solutions[2], ' y = ', solutions[3]
    return


# This function will
def p66_continued_fraction(x):
    solution = [0] * 4
    a_list = []
    m = 0
    d = 1
    a0 = int(x ** .5)
    a = a0
    a_list.append(a)
    end_point = a0 << 1
    # First we will fill up a_list with the first sequence of a's and double this list
    while a != end_point:
        m = d * a - m
        d = (x - m ** 2) / d
        a = int((a0 + m) / d)
        a_list.append(a)
    a_list_len = len(a_list)
    #    if a_list_len < 3:
    #    print a_list

    p0 = a0


"""
    running_continued_fraction = Fraction(a_list[a_list_len - 1])
    # Create fraction Akr, Bkr
    for i in xrange(a_list_len - 2, 1, -1):
        running_continued_fraction = a_list[i] + 1 / running_continued_fraction
    running_continued_fraction = a_list[0] + 1 / running_continued_fraction
    solution[0] = running_continued_fraction.numerator
    solution[1] = running_continued_fraction.denominator
    running_continued_fraction2r_p1 = Fraction(1, a_list[1])
    for j in xrange(2):
        for i in xrange(a_list_len - 2, 1, -1):
            running_continued_fraction2r_p1 = a_list[i] + 1 / running_continued_fraction2r_p1
    running_continued_fraction2r_p1 = a_list[0] + 1 / running_continued_fraction2r_p1
    solution[2] = running_continued_fraction2r_p1.numerator
    solution[3] = running_continued_fraction2r_p1.denominator
"""
    return solution