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

x1 = FieldElement(192,223)
y1 = FieldElement(105,223)
a1 = FieldElement(0,223)
b1 = FieldElement(7,223)

p1 = Point(x1,y1,a1,b1)
print(p1)

x2 = FieldElement(17,223)
y2 = FieldElement(56,223)
a2 = FieldElement(0,223)
b2 = FieldElement(7,223)

p2 = Point(x2,y2,a2,b2)
print(p2)

x3 = None
y3 = None
a3 = FieldElement(0,223)
b3 = FieldElement(7,223)

p6 = p1 + p1
print("p6=",p6)

p8 = p1+p2
print("p8=",p8)

x4 = FieldElement(200,223)
y4 = FieldElement(119,223)
a4 = FieldElement(0,223)
b4 = FieldElement(7,223)

p4 = Point(x2,y2,a2,b2)
print("p4=",p4+p4)