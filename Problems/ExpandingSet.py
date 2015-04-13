__author__ = 'Alvin'
"""
The purpose of this class is to have the class dynamically expand. While a good number of questions can be solved by
pre-allocating a large number of whatever the target number is, it is still sub optimal.

This class will effectively serve as a wrapper around a set and grow when requesting a value that is larger than the
largest value stored in the set.
"""

import abc


class ExpandingSet:

    def __init__(self, starting_value, starting_n=0):
        # sequence_set stores all values seen in the sequence thus far
        self.sequence_set = set([starting_value])
        # sequence list, think of as an index mapped dictionary
        self.sequence_list = [starting_value]
        # n refers to the current n value of the sequence
        self.starting_n = starting_n
        self.n = 0

    def get_nth(self, n):
        n -= self.starting_n
        if self.n < n:
            self.calculate_up_to_n(n-1)
        return self.sequence_list[n-1]

    # This functions only works if the sequence is increasing, it will need to be overriden if the sequence does not
    # increase.
    def contains_value(self, *values):
        for value in values:
            if self.sequence_list[-1] < value:
                self.calculate_up_to_value(value)
        return set(values).issubset(self.sequence_set)

    # Refers to the sequence function that should be implemented. Calling this finds the next element
    @abc.abstractmethod
    def sequence_function(self):
        return

    # If the set does not go up to the nth value, we calculate up to and including the nth term of the sequence.
    # This function only gets called if the self.n value is less than the given n
    # These should be private
    def calculate_up_to_n(self, n):
        while self.n < n:
            self.update_sequence_set_and_list(self.sequence_function())

    # If the set does not go up to the current value, we calculate up to and including the nth term of the sequence
    # These should be private
    def calculate_up_to_value(self, value):
        while self.value < value:
            self.update_sequence_set_and_list(self.sequence_function())

    def update_sequence_set_and_list(self, value):
        self.sequence_list.append(value)
        self.sequence_set.add(value)
        self.n += 1