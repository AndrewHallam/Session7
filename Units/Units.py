class Quantity(object):
     def __init__(self, number, unit):
         self.number=number
         self.unit=unit
         
         if type(number)==int:
             pass
         elif type(number)==float:
             pass
         else: 
             raise TypeError("You need to use a number!")
             
class Expression(object):
     def __init__(self, terms):
         self.terms=terms
                 
first=Quantity('a','meter')
print type(first.number)
print first.unit