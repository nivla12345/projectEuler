__author__ = 'Alvin'

import time

import problems1_30
import problems31_60
import problems61_90
import problems481_510
import Tools
from PrimeSet import PrimeSet

constant_iterations = 1
# function_to_run = Tools.
result = None

t0 = time.time()
if constant_iterations == 1:
    result = problems481_510.p500()
    print result
else:
    for i in xrange(constant_iterations - 1):
        problems481_510.p500()
    print problems481_510.p500()
t1 = time.time()

print "time (s): ", t1 - t0
