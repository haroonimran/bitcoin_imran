##############################################################################################
# HAROON IMRAN
# haroon.imran@gmail.com
# Setting up a FiniteField of numbers
##############################################################################################

import ecc
from ecc import Point
from ecc import FieldElement


x8 = FieldElement(47,223)
y8 = FieldElement(71,223)
a = FieldElement(0,223)
b = FieldElement(7,223)
p8 = Point(x8,y8,a,b)

print("p8 =",p8)
print("2 * p8 =",p8+p8)
