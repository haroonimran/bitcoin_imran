##############################################################################################
# HAROON IMRAN
# haroon.imran@gmail.com
# Setting up a FiniteField of numbers
##############################################################################################

import ecc
from ecc import Point


point1 = Point(-1,-1,5,7)
print(point1)
point2 = Point(-1,1,5,7)
print(point2)
point3 = point1+point2
print(point3)
