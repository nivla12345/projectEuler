__author__ = 'Alvin'

import Tools
from ExpandingSet import ExpandingSet


class PrimeSet(ExpandingSet):
    def __init__(self, starting_value=2, starting_n=0):
        ExpandingSet.__init__(self, starting_value, starting_n)

    def sequence_function(self):
        return Tools.is_prime()
