__author__ = 'not Alvin'


import functools


def pre_condition(check):
    return condition(pre_condition=check)


def post_condition(check):
    return condition(post_condition=check)


# Taken from: https://stackoverflow.com/questions/12151182/python-precondition-postcondition-for-member-function-how
def condition(pre_condition=None, post_condition=None):
    def decorator(func):
        @functools.wraps(func)  # preserver name, docstring, etc
        def wrapper(*args, **kwargs):  # NOTE: no self
            if pre_condition is not None:
                assert pre_condition(*args, **kwargs)
            return_value = func(*args, **kwargs)  # call original function or method
            if post_condition is not None:
                assert post_condition(return_value)
            return return_value
        return wrapper
    return decorator

