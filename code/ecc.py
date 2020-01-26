######################################################################################################################
# 01/26/2020 | HAROON IMRAN | haroon.imran@gmail.com
# This library provides methods to ensure that "addition" and "multiplication" of elements in a Finite Field
# of prime order are "closed" (i.e. satisfy Closure as defined in point 1 below).
# 
# A Finite Field of prime order is a set of elements from "0" through "p" (a prime number) that satisfies the the following properties:
# If elements a and b exist in the set,
# 1. a+b and a*b must exist in the set (Additive and Multiplicative Closure)
# 2. the element 0 exists in the set such that a + 0 = a. (Additive Identity)
# 3. the element -a exists in the set such that a + (-a) = 0. (Additive Inverse)
# 4. the element 1 exists in the set such that (a * 1)  = a. (Multiplicative Identity)
# 5. element a**-1 exists in the set such that a * (a**-1) = 1. (Multiplicative Inverse)
#
# Example: F(7) = {0,1,2,3,4,5,6} / On this field, ordinary addition and multiplication are not "closed" e.g 4+5 = 9 or 3*4 = 12 
# are not elements of F(7). The Closure of addition and multiplication is acheived through modulo arithmetic.
#######################################################################################################################



#------------------------------------
# 1. Finite Field.
#------------------------------------
class FieldElement:
    
    # Constructor:
    def __init__(self,num,prime):
        if (num<0 and num>= prime):
            print("{} is not a valid element in a field of order {}".format(num,prime))
            raise ValueError("error")
        self.num = num
        self.prime = prime
  
    # Similarly overloading "+" (plus)
    def __add__(self, other):
        if self.prime != other.prime:
            raise TypeError("Cant add objects not of the same Field.")
        sum = (self.num + other.num) % self.prime
        return self.__class__(sum, self.prime)

    # Overloading minus "-"
    def __sub__(self, other):
        if self.prime != other.prime:
            raise TypeError("Cant subtract from object not of the same Field.")
        sum = (self.num - other.num) % self.prime
        return self.__class__(sum, self.prime)
    
    # Overloading " * "
    def __mul__(self, other):
        if self.prime != other.prime:
            raise TypeError("Cant multiply objects not of the same Field.")
        product = (self.num * other.num) % self.prime
        return self.__class__(product, self.prime)

    # Overloading " ** "
    def __pow__(self, exponent):
        power = (self.num ** exponent) % self.prime
        return self.__class__(power, self.prime)

    # Overloading the print() function for objects of class FieldElement.
    def __repr__(self):
        return 'FieldElement {}({})'.format(self.prime,self.num)

     # Overloading the "x == y" logical operation for objects of class FieldElement.
    def __eq__(self, other):
        if other == None:
            return False
        return self.num == other.num and self.prime == other.prime


#------------------------------------
# 2. Point.
#------------------------------------
class Point:

    def __init__(self, int x, y, a, b):
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        if ((self.y ** 2) != (self.x ** 3) + (self.a * x) + self.b):
            raise ValueError("The point ({},{}) does not lie on an elliptic curve".format(x,y))

    def __eq__(self,other):
        if other == None:
            return False
        if self.a == other.a and self.b == other.b and \
           self.x == other.x and self.y == other.y:
           return True
    
    def __ne__(self,other):
        if other == None:
            return False
        if self.a != other.a or self.b != other.b or \
           self.x != other.x or self.y != other.y:
           return True

    def __repr__(self):
        if self == None:
            raise TypeError("Cant print an undefined object.")
        return "The point is : (x={},y={},a={},b={})".format(self.x,self.y,self.a,self.b)