__author__ = 'Alvin'

import time

import problems1_30
import problems31_60
import Tools
from PrimeSet import PrimeSet

constant_iterations = 1
# function_to_run = Tools.

t0 = time.time()
if constant_iterations == 1:
    print problems31_60.p60()
else:
    for i in xrange(constant_iterations - 1):
        problems31_60.p60()
    print problems31_60.p60()
t1 = time.time()

print "time (s): ", t1 - t0
