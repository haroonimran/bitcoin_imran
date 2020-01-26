##############################################################################################
# HAROON IMRAN
# haroon.imran@gmail.com
# Setting up a FiniteField of numbers
##############################################################################################

class FieldElement:
    
    # Constructor:
    def __init__(self,num,prime):
        if (num<0 and num>= prime):
            print("{} is not a valid element in the order {}".format(num,prime - 1))
            raise ValueError("error")
        self.num = num
        self.prime = prime

    def __repr__(self):
        return 'FieldElement {}({})'.format(self.prime,self.num)

    def __eq__(self, other):
        if other == None:
            return False
        return self.num == other.num and self.prime == other.prime
    
    def __add__(self, other):
        if self.prime != other.prime:
            raise TypeError("The objects being added are not of the same order.")
        sum = (self.num + other.num) % self.prime
        return self.__class__(sum, self.prime)
    
    def __mul__(self, other):
        if self.prime != other.prime:
            raise TypeError("The objects being added are not of the same order.")
        product = (self.num * other.num) % self.prime
        return self.__class__(product, self.prime)
