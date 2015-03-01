from collections import Counter
from os.path import join, dirname
from yaml import load

Ex = load(open(join(dirname(__file__), 'examples.yml')))

class Quantity(object):
     def __init__(self, number, units, powers):
         
         self.number=number
         self.units=units
         self.powers=powers
         self.dictunits={symbol: exponent for symbol,exponent
                 in zip(units, powers)}
         
         if type(number)==int:
             pass
         elif type(number)==float:
             pass
         else: 
             raise TypeError("You need to use a number!")

     def __mul__(self, other):
         return self.multiply(other)
         
     def __rmul__(self, other):
         return self.multiply(other)
         
     def __add__(self, other):
         return self.add(other)
         
     def __radd__(self, other):
         return self.add(other)
         
     def __eq__(self, other):
         if self.number==other.number:
            if self.dictunits==other.dictunits:
                return True
         else:
             return False

     def add(self, other):
         if self.dictunits==other.dictunits:
             return Quantity(self.number+other.number, self.units, self.powers)
         else:
             raise TypeError("You can't add things with different units!")  

     def multiply(self, other):
         if type(other)==float:
             return Quantity(self.number*other, self.units, self.powers)
         elif type(other)==int:
             return Quantity(self.number*other, self.units, self.powers)
             
         else:
             Units1=Counter(self.dictunits)
             Units2=Counter(other.dictunits)
             newunits=Units1+Units2
             return Quantity(self.number*other.number, newunits.keys(), newunits.values())
         
     def convert(self, oldunit, newunit, scale):
         if oldunit in self.units:
            self.dictunits[newunit]=self.dictunits.pop(oldunit)
            return Quantity(scale*self.number, self.dictunits.keys(), self.dictunits.values())
         else: 
            raise LookupError("I can't change a unit if it isn't in this quantity!")
            
