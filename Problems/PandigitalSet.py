__author__ = 'Alvin'

from ExpandingSet import ExpandingSet


class PandigitalSet(ExpandingSet):
    def __init__(self):
        ExpandingSet.__init__(self, 1)
        self.increment_by = 4

    def sequence_function(self):
        tmp_increment_by = self.increment_by
        self.increment_by += 3
        return self.sequence_list[-1] + tmp_increment_by