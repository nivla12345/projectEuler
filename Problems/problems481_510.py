__author__ = 'alvinmao'


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

    # Refers to the current head/tail index. Will always be 0.
    tail = 0
    head = 4
    # Next and previous index
    next_index = 1
    previous_index = 0

    # Generate base divisors
    hard_coded_initial_seive_size = 7370028
    # hard_coded_initial_seive_size = 40

    # Divisor list is the sieve that indicates whether a data point has been marked or not.
    #   - Each element will be represented as [previous, next]
    divisor_list = [0] * hard_coded_initial_seive_size
    divisor_list[0] = [None, 1]
    divisor_list[1] = [0, 4]
    divisor_list[4] = [1, -1]
    base_divisor_stack = [2, 3]

    # Perform sieve
    for i in xrange(2, hard_coded_initial_seive_size):
        if not divisor_list[i]:
            current_divisor = i + 2

            # Will contain the indexes to add to the divisor_list
            to_add_values = [i]
            current_track_index = tail

            # Look through previous base divisors, create combinations and multiply
            while current_track_index >= 0:
                divisor_value = current_track_index + 2
                look_ahead_index = (current_divisor * divisor_value) - 2
                if look_ahead_index >= hard_coded_initial_seive_size:
                    break
                to_add_values += [look_ahead_index]
                current_track_index = divisor_list[current_track_index][next_index]

            # Add to the base divisor stack.
            base_divisor_stack.append(current_divisor)

            # Properly assign head index. If we have a new larger value we have a neww larger head
            potential_head_index = to_add_values[-1]
            if head <= potential_head_index:
                # Assign next value for previous head
                divisor_list[head][next_index] = potential_head_index
                # Assign new head previous pointer
                divisor_list[potential_head_index] = [head, -1]
                # Assign new head index
                head = potential_head_index
                # Remove head from the values to add
                to_add_values.pop()

            # Add the values to the divisor_list.
            while to_add_values:
                current_index = to_add_values.pop()

                # Find previous index
                running_index = current_index
                while not divisor_list[running_index] and running_index != tail:
                    running_index -= 1

                current_next_index = divisor_list[running_index][next_index]
                divisor_list[current_index] = [None, None]
                divisor_list[current_index][previous_index] = running_index
                divisor_list[current_index][next_index] = current_next_index
                divisor_list[running_index][next_index] = current_index
                divisor_list[current_next_index][previous_index] = current_index

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