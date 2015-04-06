__author__ = 'Alvin'

import time

import problems1_30
import problems31_60


constant_iterations = 1


t0 = time.time()
if constant_iterations == 1:
    print problems31_60.p35()
else:
    for i in xrange(constant_iterations):
        problems31_60.p35()
t1 = time.time()

print "time (s): ", t1 - t0