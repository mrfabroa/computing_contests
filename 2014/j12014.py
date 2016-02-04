__author__ = 'eric'

import sys

# get angles
val1 = int(sys.stdin.readline())
val2 = int(sys.stdin.readline())
val3 = int(sys.stdin.readline())

valsum = val1 + val2 + val3

if valsum != 180:
    print "Error"
elif val1 == 60 and val2 == 60 and val3 == 60:
    print "Equilateral"
elif val1 == val2 or val1 == val3 or val2 == val3:
    print "Isosceles"
else:
    print "Scalene"