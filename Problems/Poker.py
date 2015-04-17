__author__ = 'Alvin'


class Poker:
    card_ranks = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14
    }

    def __init__(self):
        return

    @staticmethod
    def get_values(self, hand):
        """
        Returns a sorted hand value
        :param hand:
        :return:
        """
        values = []
        for i in hand:
            values.append(self.card_ranks[i[:-1]])
        return sorted(values)

    @staticmethod
    def flush(hand):
        """
        :param hand:
        :return: True if flush, False otherwise
        """
        suit_set = set()
        for i in hand:
            suit_set.add(i[-1])
        return len(suit_set) > 1

    @staticmethod
    def straight(self, hand):
        """
        Returns if value is straight, does not recognize Ace, 2, 3, 4, 5 as a straight.
        :param hand:
        :return: 0 is not straight, largest number in straight if straight.
        """
        values = self.get_values(hand)
        tracking_value = values[0]
        for i in xrange(1, len(values)):
            if values[i] != tracking_value + 1:
                return False
            tracking_value += 1
        return tracking_value

    @staticmethod
    def straight_flush(self, hand):
        """
        If this returns true, it is the largest hand available given there are no ties.
        :param hand: The hand to test
        :return: The largest value in the straight or 0 if not straight flush
        """
        flush = self.is_flush(hand)
        straight = self.is_straight(hand)
        return flush and straight

    @staticmethod
    def royal_flush(self, hand):
        """
        If this returns true, it is the largest hand available given there are no ties.
        :param hand: The hand to test
        :return: Where there is in fact a royal flush
        """
        flush = self.is_flush(hand)
        straight = self.is_straight(hand)
        return flush and straight == self.card_ranks["A"]

    @staticmethod
    def triple(self, hand):
        """
        This method call returns a 3 element list. The list works as follows:
        0: value of the number composing the triple, 0 if no triple
        1: next largest number
        2: smallest non-triple number
        :param hand:
        :return: list described above
        """
        values_dict = dict()
        for i in self.get_values(hand):
            if i in values_dict:
                values_dict[i] = 1
            else:
                values_dict[i] += 1
        return_list = [0, 0, 0]
        for i in values_dict:
            if values_dict[i] == 3:
                return_list[0] = i
                del values_dict[i]
        return_list[1] = max(values_dict.keys())
        return_list[2] = min(values_dict.keys())
        return return_list

    @staticmethod
    def pair(self, hand):
        values_dict = dict()
        return_list = [0] * 4
        for i in self.get_values(hand):
            if i in values_dict:
                values_dict[i] = 1
            else:
                values_dict[i] += 1
                return_list[0] = i
        if return_list[0]:
            del values_dict[return_list[0]]
            return_list[1] = max(values_dict.keys())
            del values_dict[return_list[1]]
            return_list[2] = max(values_dict.keys())
            del values_dict[return_list[2]]
            return_list[3] = max(values_dict.keys())
            del values_dict[return_list[3]]
        return return_list

    @staticmethod
    def full_house(self, hand):
        triple = self.triple(hand)
        if triple[1] == triple[2]:
            return triple[0], triple[1]
        return 0, 0, 0

    @staticmethod
    def two_pair(self, hand):
        values_dict = dict()
        for i in self.get_values(hand):
            if i in values_dict:
                values_dict[i] = 1
            else:
                values_dict[i] += 1
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

    @staticmethod
    def quadruple(self, hand):
        """
        :param hand:
        :return: If the first element is 0, not a quadruple.
        """
        values_dict = dict()
        for i in self.get_values(hand):
            if i in values_dict:
                values_dict[i] = 1
            else:
                values_dict[i] += 1
        return_list = [0, 0]
        for i in values_dict:
            if values_dict[i] == 4:
                return_list[0] = i
            else:
                return_list[1] = i
        return return_list

    @staticmethod
    def high_card(self, hand):
        return self.get_values(hand)[-1]

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

    @staticmethod
    def compare(self, hand1, hand2):
        return


