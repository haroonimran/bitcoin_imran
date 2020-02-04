##############################################################################################
# HAROON IMRAN
# haroon.imran@gmail.com
# Setting up a FiniteField of numbers
##############################################################################################

from ecch import Point
from ecch import FieldElement

# Chapter 3 
# Exercise 1
#Evaluate whether thesr points are on the curve: y**2 = x**2 + ax + b (a=0 b=7, Fprime = 223)

# 1. (192,105) 2. (17,56) 3. (200,119) 4. (1, 193) 5. (42,99)


a = FieldElement(0,223)
b = FieldElement(7,223)

x1 = FieldElement(192,223)
y1 = FieldElement(105,223)
p1 = Point(x1,y1,a,b)

x2 = FieldElement(17,223)
y2 = FieldElement(56,223)
p2 = Point(x2,y2,a,b)

x3 = FieldElement(200,223)
y3 = FieldElement(119,223)
p3 = Point(x3,y3,a,b)

x4 = FieldElement(1,223)
y4 = FieldElement(193,223)
p4 = Point(x4,y4,a,b)

x5 = FieldElement(42,223)
y5 = FieldElement(99,223)
p5 = Point(x5,y5,a,b)

# Chapter 3 
# Exercise 2
#Evaluate whether thesr points are on the curve: y**2 = x**2 + ax + b (a=0 b=7, Fprime = 223)

# Find:
# 1. (170,142) + (60,139)
# 2. (47,71) + (17,56)
# 3. (143,98) + (76,66)
print("----------- EXERCISE 2 -----------------")
x6 = FieldElement(170,223)
y6 = FieldElement(142,223)
x7 = FieldElement(60,223)
y7 = FieldElement(139,223)

p6 = Point(x6,y6,a,b)
p7 = Point(x7,y7,a,b)
p67 = p6 + p7
print("The sum of {} and {} is {}".format(p6,p7,p67))

pa = Point(1,2,3,4)
pb = Point(77,2,3,4)

print(pa + pb)



