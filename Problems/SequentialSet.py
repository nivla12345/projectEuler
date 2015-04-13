__author__ = 'Alvin'

from ExpandingSet import ExpandingSet


class SequentialSet(ExpandingSet):
    def __init__(self, starting_value, difference, starting_n=0):
        ExpandingSet.__init__(self, starting_value, starting_n)
        self.increment_by = 1 + difference
        self.difference = difference

    def sequence_function(self):
        tmp_increment_by = self.increment_by
        self.increment_by += self.difference
        return self.sequence_list[-1] + tmp_increment_by