__author__ = 'alvinmao'

from ExpandingSet import ExpandingSet


class TwiceSquareSet(ExpandingSet):
    def __init__(self, starting_value=2, starting_n=0):
        ExpandingSet.__init__(self, starting_value, starting_n)

    def sequence_function(self):
        return (self.n + 2) * (self.n + 2) * 2