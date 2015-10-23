import time

import problems1_30
import problems31_60
import problems61_90
import problems211_240
import problems241_270
import problems481_510
import Tools
from PrimeSet import PrimeSet

__author__ = 'Alvin'

constant_iterations = 1
# function_to_run = Tools.
result = None

t0 = time.time()
if constant_iterations == 1:
    result = problems241_270.p243()
    print result
else:
    for i in xrange(constant_iterations - 1):
        problems241_270.p243()
    print problems241_270.p243()
t1 = time.time()

print "time (s): ", t1 - t0
