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
             
     def add(self, other):
         if self.unit==other.unit:
             return Quantity(self.number+other.number, self.unit)
         else:
             return TypeError("You can't add things with different units!")  
             
class Expression(object):
     def __init__(self, terms):
         self.terms=terms
                 
first=Quantity(1,'gram')
second=Quantity(2,'gram')
third=first.add(second)
print third.number