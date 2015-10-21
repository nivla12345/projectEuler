__author__ = 'alvinmao'

import math
import Tools


# Given the smallest number with 1 << 500500 divisors (n). Find n % 500500507.
#
# Plan:
#   Overall Plan:
#   The plan is to break up (1 << 500500) into its base divisors (described below). We then mod each base divisor by:
#   500500507 and take the product of the resulting mods. We follow this up by modding the resulting product to get our
#   final answer.
#
#   A further optimization that can be made would be to multiply base divisors until they're > 500500507 and take the
#   mod of the ensuing product before restarting.
#
#   Base Divisors:
#   The smallest number with n**2 divisors is always composed of combinations of base divisors ie.
#   2    -> 2
#   6    -> 2,3
#   24   -> 2,3,4
#   120  -> 2,3,4,5
#   840  -> 2,3,4,5,7
#   7560 -> 2,3,4,5,7,9
#   etc...
#
#   To get all the divisors you take the product combination of these base divisors. However, that's not pertinent to
#   our problem as we are only concerned with the base divisors as we can apply the approach detailed in the overall
#   plan to find the mod.
#
#   The plan to create the base divisors involves generating a sieve that can hold all 500500 base divisors.as
#   The sieve will be implemented by 2 lists. The list will be the sieve marking all seen divisors. The other list will
#   be implemented as a stack and will contain all base divisors.
#
# Note:
#  500500507 = 13 * 38500039 both of which are prime.
#  n % 500500507 == 13 * (n % 38500039)
#
#  and more importantly:
#  n % 500500507 == 38500039 * (n % 13)
#
# This will be O(n) where n = 1M or some number that can store the base divisors.
def p500():
    mod_by = 500500507
    upper_limit = 500500

    # Generate base divisors
    hard_coded_initial_seive_size = 1327503
    #hard_coded_initial_seive_size = 5
    divisor_list = [False] * hard_coded_initial_seive_size
    divisor_list[0] = True
    base_divisor_stack = [2]
    # Perform sieve
    for i in xrange(1, hard_coded_initial_seive_size):
        if not divisor_list[i]:
            current_divisor = i + 2
            divisor_list[i] = True

            # Look through previous base divisors, create combinations and multiply
            for base_divisor in base_divisor_stack:
                base_divisor_index = (base_divisor * current_divisor) - 2
                if base_divisor_index >= hard_coded_initial_seive_size:
                    break
                divisor_list[base_divisor_index] = True

            base_divisor_stack.append(current_divisor)
            # Done sieving
            if len(base_divisor_stack) >= upper_limit:
                # This line was used to obtain the hard_code_initial_seive_size...
                # print i
                break

    # product = 1
    # for i in base_divisor_stack:
    #     product *= i
    # print len(base_divisor_stack)
    # print base_divisor_stack
    # print product

    # Iterate over the base divisors and obtain the modulus
    mod_track = 1
    running_product = 1
    while base_divisor_stack:
        running_product *= base_divisor_stack.pop()
        if running_product > mod_by:
            mod_track *= (running_product % mod_by)
            running_product = 1
            if mod_track > mod_by:
                mod_track %= mod_by
    return (mod_track * running_product) % mod_by