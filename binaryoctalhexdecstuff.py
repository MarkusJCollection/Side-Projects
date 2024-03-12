from math import log2,floor
class baseConverter():
    def __init__(self):
        self.__numSet = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f','g','h'
                         ,'i','j','k','l','m','n','o','p','q','r','s','t','u'
                         ,'v','w','x','y','z','A','B','C','D','E','F','G','H'
                         ,'I','J','K','L','M','N','O','P','Q','R','S','T','U',
                         'V','W','W','Y','Z']
        
    def sets(self):
        print("{0}".format(self.__numSet))
                
    
    def decimalToAny(self,decimal,base=10):
        #Takes an input of a decimal number that will then
        #be changed into a binary string.
        
            #Sets the starting power to 0.
        powerNum = 0
            #Finds the smallest, largest power that the number can have.
            #Ex. 2^2=4 is the smallest, largest power if the input was 3.
        while base**powerNum<=decimal:
            powerNum+=1
            #Special case if the input was 0.
        if powerNum == 0:
            return "0"
            #Special case if the input was 1.
        elif powerNum < 2:
            return "{0}".format(self.__numSet[decimal])
            #If a special case isn't hit, then a recursive function is ran.
        else:
            powerNum-=1
            return self.anyNumFinder(decimal,powerNum,base)


    def anyNumFinder(self,decimal,power,base=2):
        #Recursive function that takes an input of
        #the number, and what power of 2 is being tested.
        #---- Takes the largest number that can go into it,
        #---- and progressively goes down until 0 is reached.
        
        newDecNumber = decimal-(base**power)
        amount = 1
        if power>=0:
            if newDecNumber>=0:
                while newDecNumber>=base**power:
                    amount+=1
                    newDecNumber = newDecNumber-(base**power)
                power-=1
                return str(self.__numSet[amount])+self.anyNumFinder(newDecNumber,power,base)
            else:
                power-=1
                return "0"+self.anyNumFinder(decimal,power,base)
        else:
            return ""
        
       
       
    def anyToDecimal(self,number,base):
        #Function that takes a binary number,
        #and finds its decimal counterpart.
        
        number = str(number).split('b')
        number = number[-1]
        powerNum = len(number)-1
        decimalNum = 0
        
        for char in number:
            if char == '0':
                powerNum-=1
            else:
                try:
                    charMultiplier = int(char)
                except:
                    position = 0
                    for value in self.__numSet:
                        if value == char:
                            charMultiplier=position
                        else:
                            position+=1
                decimalNum += charMultiplier*(base**powerNum)
                powerNum-=1
        return decimalNum
        
        
        
        
        
testval = 3
baseTestval = 16
a = baseConverter()



def anyTEST():
    b = a.decimalToAny(testval,baseTestval)
    print(testval)
    print(a.anyToDecimal(b,baseTestval))
    print(oct(testval))
    print("  {0}".format(b))
    print(hex(testval))
    print(bin(testval))
#anyTEST()


