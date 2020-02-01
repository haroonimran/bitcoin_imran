##############################################################################################
# HAROON IMRAN
# haroon.imran@gmail.com
# Setting up a FiniteField of numbers
##############################################################################################

import ecc
from ecc import Point
from ecc import FieldElement


#Chapter 3
#Exercise 1
# Evaluate whether the following points are on the curve y**2 = x**3 + 7 over F(223)
#(192,105) (17,56) (200,119) (1,193) (42,99)

#instantiate points

x = FieldElement(192,223)
y = FieldElement(105,223)
a = FieldElement(0,223)
b = FieldElement(7,223)

p1 = Point(x,y,a,b)
print(p1)

x = FieldElement(17,223)
y = FieldElement(56,223)
a = FieldElement(0,223)
b = FieldElement(7,223)

p2 = Point(x,y,a,b)
print(p2)

p3 = p1+p2
print(p3)