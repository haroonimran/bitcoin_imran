##############################################################################################
# HAROON IMRAN
# haroon.imran@gmail.com
# Setting up a FiniteField of numbers
##############################################################################################

import ecc

a = ecc.FieldElement(12, 19)
b = ecc.FieldElement(18, 19)

c = a + b
d = a * b
print(c)
print(d)
