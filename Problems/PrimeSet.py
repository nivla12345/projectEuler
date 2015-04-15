__author__ = 'Alvin'

import Tools
from ExpandingSet import ExpandingSet


class PrimeSet(ExpandingSet):
    def __init__(self, starting_value=(2, 3), starting_n=1):
        ExpandingSet.__init__(self, starting_value, starting_n)

    def sequence_function(self):
        starting_value = self.sequence_list[-1] + 2
        while not Tools.is_prime(starting_value):
            starting_value += 2
        return starting_value