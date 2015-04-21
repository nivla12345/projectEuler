__author__ = 'Alvin'

card_ranks = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}


def get_values(hand):
    """
    Returns a sorted hand value
    :param hand:
    :return:
    """
    values = []
    for i in hand:
        values.append(card_ranks[i[:-1]])
    return sorted(values)


def flush(hand):
    """
    :param hand:
    :return: True if flush, False otherwise
    """
    suit_set = set()
    for i in hand:
        suit_set.add(i[-1])
    return [len(suit_set) == 1]


def straight(hand):
    """
    Returns if value is straight, does not recognize Ace, 2, 3, 4, 5 as a straight.
    :param hand:
    :return: 0 is not straight, largest number in straight if straight.
    """
    values = get_values(hand)
    tracking_value = values[0]
    for i in xrange(1, len(values)):
        if values[i] != tracking_value + 1:
            return [False]
        tracking_value += 1
    return [tracking_value]


def straight_flush(hand):
    """
    If this returns true, it is the largest hand available given there are no ties.
    :param hand: The hand to test
    :return: The largest value in the straight or 0 if not straight flush
    """
    is_flush = flush(hand)
    is_straight = straight(hand)
    return [is_flush[0] and is_straight[0]]


def royal_flush(hand):
    """
    If this returns true, it is the largest hand available given there are no ties.
    :param hand: The hand to test
    :return: Where there is in fact a royal flush
    """
    is_flush = flush(hand)
    is_straight = straight(hand)
    return [is_flush[0] and is_straight[0] == card_ranks["A"]]


def triple(hand):
    """
    This method call returns a 3 element list. The list works as follows:
    0: value of the number composing the triple, 0 if no triple
    1: next largest number
    2: smallest non-triple number
    :param hand:
    :return: list described above
    """
    values_dict = dict()
    for i in get_values(hand):
        if i in values_dict:
            values_dict[i] += 1
        else:
            values_dict[i] = 1
    return_list = [0, 0, 0]
    for i in values_dict:
        if values_dict[i] == 3:
            return_list[0] = i
    if return_list[0]:
        del values_dict[i]
    return_list[1] = max(values_dict.keys())
    return_list[2] = min(values_dict.keys())
    return return_list


def pair(hand):
    values_dict = dict()
    return_list = [0] * 4
    for i in get_values(hand):
        if i in values_dict:
            values_dict[i] += 1
            return_list[0] = i
        else:
            values_dict[i] = 1
    if return_list[0]:
        i = 1
        del values_dict[return_list[0]]
        while len(values_dict) > 0:
            return_list[i] = max(values_dict.keys())
            del values_dict[return_list[i]]
            i += 1
    return return_list


def full_house(hand):
    is_triple = triple(hand)
    if is_triple[1] == is_triple[2]:
        return is_triple[0], is_triple[1]
    return 0, 0, 0


def two_pair(hand):
    values_dict = dict()
    for i in get_values(hand):
        if i in values_dict:
            values_dict[i] += 1
        else:
            values_dict[i] = 1
    return_list = [0, 0, 0]
    twos = [0, 0]
    twos_index = 0
    for i in values_dict:
        if values_dict[i] == 2:
            twos[twos_index] = i
            twos_index += 1
        else:
            return_list[2] = i
    if 0 in twos:
        return [0, 0, 0]
    return_list[0] = max(twos)
    return_list[1] = min(twos)
    return return_list


def quadruple(hand):
    """
    :param hand:
    :return: If the first element is 0, not a quadruple.
    """
    values_dict = dict()
    for i in get_values(hand):
        if i in values_dict:
            values_dict[i] += 1
        else:
            values_dict[i] = 1
    return_list = [0, 0]
    for i in values_dict:
        if values_dict[i] == 4:
            return_list[0] = i
        else:
            return_list[1] = i
    return return_list


def high_card(hand):
    """
    Returns a sorted hand with the largest value being in 0
    :param hand:
    :return:
    """
    return get_values(hand)[::-1]


rank_functions = [
    royal_flush,
    straight_flush,
    quadruple,
    full_house,
    flush,
    straight,
    triple,
    two_pair,
    pair,
    high_card
]


def compare(hand1, hand2):
    """
    Returns if hand1 beats hand 2
    :param hand1:
    :param hand2:
    :return:
    """
    for i in rank_functions:
        hand1r = i(hand1)
        hand2r = i(hand2)
        if hand1r[0] == 0 and hand2r[0] == 0:
            continue
        for j in xrange(len(hand1r)):
            if hand1r[j] > hand2r[j]:
                return True
            elif hand1r[j] < hand2r[j]:
                return False
    print "\n\nSHOULD NEVER GET HERE\n\n"
    return False
