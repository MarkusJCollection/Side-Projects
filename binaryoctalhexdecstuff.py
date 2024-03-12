from math import log2,floor
class baseConverter():
    def __init__(self):
        self.__binarySet = [0,1]
        self.__octalSet = [0,1,2,3,4,5,6,7]
        self.__hexSet = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
        self.__output = ""
        
    def sets(self):
        print("{0} \n{1} \n{2}".format(self.__binarySet,self.__octalSet,self.__hexSet))
        
        
    def decimalToBinary(self,decimal):
        number='0'
        if decimal == 0:
            number += self.__output
            self.output = ""
            return print(number)
        else:  
            num = ''
            power = floor(log2(decimal))
            print(power)

a = baseConverter()
a.decimalToBinary(0)

"""
c = []
for i in range(7):
    c.append(0)
    
print(c)
"""

