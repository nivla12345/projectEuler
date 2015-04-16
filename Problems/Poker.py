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
    def flush(self, hand):
        return

    @staticmethod
    def straight(self, hand):
        return

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
        return

    @staticmethod
    def pair(self, hand):
        return

    @staticmethod
    def quadruple(self, hand):
        return

    @staticmethod
    def full_house(self, hand):
        return

    @staticmethod
    def compare(self, hand1, hand2):
        return

    rank_functions = [
        royal_flush,
        straight_flush,
        quadruple,
        full_house,
        flush,
        straight,
        triple,
        pair
    ]


