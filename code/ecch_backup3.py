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
        self.num = num
        self.prime = prime
        
        if self.num == None:
            return
        
        if (self.num<0 and self.num>= prime):
            print("{} is not a valid element in a field of order {}".format(self.num,self.prime))
            raise ValueError("error")
  
    # Overloading the "+" (plus) operator
    def __add__(self, other):
        if self.prime != other.prime:
            raise TypeError("Cant add objects not of the same Field.")
        sum = (self.num + other.num) % self.prime
        return self.__class__(sum, self.prime)

    # Overloading minus "-"
    def __sub__(self, other):
        if self.prime != other.prime:
            raise TypeError("Cant subtract from object not of the same Field.")
        diff = (self.num - other.num) % self.prime
        return self.__class__(diff, self.prime)
    
    # Overloading " * "
    def __mul__(self, other):
        if self.prime != other.prime:
            raise TypeError("Cant multiply objects not of the same Field.")
        product = (self.num * other.num) % self.prime
        return self.__class__(product, self.prime)

    # Overloading the print() function for objects of class FieldElement.
    def __repr__(self):
        return 'FieldElement {}({})'.format(self.num,self.prime)

     # Overloading the "x == y" logical operation for objects of class FieldElement.
    def __eq__(self, other):
        if other.num == None or other.prime == None:
            return False
        else:
            return self.num == other.num and self.prime == other.prime

    def __pow__(self, exponent):
        n = exponent % (self.prime - 1)
        num = pow(self.num, n, self.prime)
        return self.__class__(num, self.prime)

    #1/26/2020 Haroon - TrueDiv pasted from "programming bitcoin" book's ecc.py
    def __truediv__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot divide two numbers in different Fields')
        # self.num and other.num are the actual values
        # self.prime is what we need to mod against
        # use fermat's little theorem:
        # self.num**(p-1) % p == 1
        # this means:
        # 1/n == pow(n, p-2, p)
        num = (self.num * pow(other.num, self.prime - 2, self.prime)) % self.prime
        # We return an element of the same class
        return self.__class__(num, self.prime)

    def __rmul__(self, coefficient):
        num = (self.num * coefficient) % self.prime
        return self.__class__(num=num, prime=self.prime)

    def __ne__(self,other):
        if self.num != other.num or self.prime != other.prime:
            return True
######################################################################################################################
# 2/7/2020 | HAROON IMRAN | haroon.imran@gmail.com
# 1. The class "Point" defines an object representing a point on an elliptic curve in terms of:
# x, x coordinate
# y, y coordinate
# a, the coeffiecient of x
# b, the constant
# in an elliptic curve of the form y^2 = x^3 + ax + b
# When performing modulo arithmentic, over a Finite Field of order "p", the equation would be:
# y^2 mod p = (x^3 + ax + b) mod p
# 
# This class provides methods to 
#   >> add, multiply and divide "Point" objects on an elliptic curve
#   >> scalar multiply an integer with a "Point" object
#   >> 
#######################################################################################################################   

#------------------------------------
# 2. Point.
#------------------------------------
class Point:

    def __init__(self, x, y, a, b):
        self.x = x
        self.y = y
        self.a = a
        self.b = b

        # Allow the object to be a point at infinity (Additive Identity)
        # Check whether the points lie on the curve.
     
        if (isinstance(self.x, FieldElement) and isinstance(self.y,FieldElement)):
            if self.x.num == None or self.y.num == None:
                return
        else:
            if self.x == None or self.y == None:
                return
        
        
    def onCurve(self):    
        try:
            if ((self.y ** 2) != (self.x ** 3) + (self.a * self.x) + self.b):
                raise ValueError("Point {} does not lie on the elliptic curve y**2 = x**3 + {}x + {}"\
                    .format(self,self.a,self.b))
            else:
                if isinstance(self.x,FieldElement):
                    print("YES! The point {} lies on the curve elliptic curve y**2 = x**3 + {}x + {}"\
                        .format(self,self.a.num,self.b.num))
                    return True
                else:
                    print("YES! The point {} lies on the curve elliptic curve y**2 = x**3 + {}x + {}"\
                        .format(self,self.a,self.b))
                    return True
        except ValueError:
                print("No! The point {} does NOT lie on the curve elliptic curve y**2 = x**3 + {}x + {}"\
                    .format(self,self.a,self.b))
                return False

                                                ########
    
    def __add__(self, other):
        #Test that the points are on the same curve.
        if self.a != other.a or self.b != other.b:
            raise ValueError("The points are not on the same curve.")
    
            #Add1 - Define point addition to the additive identity (point at "infinity" on the elliptic curve)
            # Adding the additive identity (None,None) to x1,y1
        if (isinstance(self.x, FieldElement) and isinstance(self.y,FieldElement)):
            if self.x.num == None and self.y.num == None:
                return self.__class__(other.x.num, other.y.num,other.a.num,other.b.num)
            if other.x.num == None and other.y.num == None:
                return self.__class__(self.x.num, self.y.num,self.a.num,self.b.num)
        else:
            if self.x == None and self.y == None:
                return self.__class__(other.x, other.y,other.a,other.b)
            if other.x == None and other.y == None:
                return self.__class__(self.x,self.y,self.a,self.b)

        
                #Add2 - Define point addition with the additive inverse. The result is the additive identity.
                # x1 = x2 & y1 = -y2
        if self.x == other.x and self.y != other.y:
            return self.__class__(None,None,self.a,self.b) 
    

            #Add3 - x1 != x2 /  Refer to equation on page 36 of the book Programming Bitcoin, First Edition.
        if self.x != other.x:
            s = (other.y - self.y)/(other.x - self.x)
            x_sum = s**2 - self.x - other.x
            y_sum = s*(self.x - x_sum) - self.y
            return self.__class__(x_sum,y_sum,self.a, self.b)
    

            #Add4 - when x1,y1 = x2,y2 (i.e., the line across the curve is a tangent)
            # Refer to equations f on pages 36-36 of the book Programming Bitcoin, First Edition.
        if self == other:
            s = (3*self.x**2 + self.a)/(2*self.y)
            x_sum = s**2 - 2*self.x
            y_sum = s*(self.x - x_sum) - self.y
            return self.__class__(x_sum,y_sum,self.a, self.b)
    
            #Add5 - when x1,y1 = x2,y2 and y = 0, return the point at infinity.
        if self == other and self.y == 0:
            return self.__class__(None,None,self.a, self.b)

    
    def __eq__(self,other):
        if other == None:
            return False
 
        if self.a == other.a and self.b == other.b and self.x == other.x and self.y == other.y:
            return True

    def __ne__(self,other):
        if other.x == None and other.y == None:
            return False

        if self.a != other.a or self.b != other.b or self.x != other.x or self.y != other.y:
            return True

    def __repr__(self):
        if self == None:
            raise TypeError("Cant print an undefined object.")
        else:    
            if isinstance(self.x,FieldElement):
                return "Point({},{})_{}_{} FieldElement({})".format(self.x.num,self.y.num,self.a.num,self.b.num,self.x.prime)
            else:
                return "Point({},{})_{}_{}".format(self.x,self.y,self.a,self.b)

    def __rmul__(self,coefficient):
        product = self
        for _ in range(coefficient-1):
            product = product + self
        return product