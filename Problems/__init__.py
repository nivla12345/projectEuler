__author__ = 'Alvin'

import time

import problems1_30
import problems31_60
import Tools

constant_iterations = 1
# function_to_run = Tools.prime_factors(25)
function_to_run = problems31_60.p50()

t0 = time.time()
if constant_iterations == 1:
    print function_to_run
else:
    for i in xrange(constant_iterations - 1):
        function_to_run
    print function_to_run
t1 = time.time()

print "time (s): ", t1 - t0
