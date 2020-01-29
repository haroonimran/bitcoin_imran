##############################################################################################
# HAROON IMRAN
# haroon.imran@gmail.com
# Setting up a FiniteField of numbers
##############################################################################################

import ecch
from ecch import Point
from ecch import FieldElement


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



x = FieldElement(1,223)
y = FieldElement(193,223)
a = FieldElement(0,223)
b = FieldElement(7,223)

p4 = Point(x,y,a,b)
print(p4)

"""
x = FieldElement(42,223)
y = FieldElement(99,223)
a = FieldElement(0,223)
b = FieldElement(7,223)

p5 = Point(x,y,a,b)
print(p4)

x = FieldElement(200,223)
y = FieldElement(119,223)
a = FieldElement(0,223)
b = FieldElement(7,223)

p3 = Point(x,y,a,b)
print(p3)
"""
print(p1+p2)