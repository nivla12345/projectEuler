__author__ = 'Alvin'
import Tools

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