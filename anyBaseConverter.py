class baseConverter():
    """
        Multipurpose class that is able to
        convert a decimal number to the highest allowed base,
        and the ability to convert it from that to decimal.
        
        Other subclasses are built-in that focus mainly
        on the conversion of a decimal number to
        binary, octal, and hexadecimal.
        
        
        ---HIGHEST ALLOWED BASE 62---
        
        NAME.baseConverter()
        
        NAME.decimalToAny(DECIMAL NUMBER, BASE)     	- Convert any positive integer
                                                       to any base.
                                                       
        NAME.anyToDecimal(NUMBER IN ANY BASE, BASE) 	- Convert any positive integer
                                                       in any base to a decimal number.
    
        NAME.setOfItems()                           	- Set of elements in the list,
                                                       determines highest base.
                                                       
        NAME.baseToBase(NUMBER, BASE, BASE)         	- Changes a decimal number from
                                                       a given base into another.
        
        
        NAME.binary(NUMBER)                         	- Automatically changes a decimal
        NAME.octal(NUMBER)                             number into their respective base.
        NAME.hexadecimal(NUMBER)
        
    """
    
    
    def __init__(self):
        #Number set that can is used for determination on
        #the highest base that can be used.
        #
        #Every element added adds +1 to the highest base
        #that can be calculated.
        
        self.__numSet = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f','g','h'
                         ,'i','j','k','l','m','n','o','p','q','r','s','t','u'
                         ,'v','w','x','y','z','A','B','C','D','E','F','G','H'
                         ,'I','J','K','L','M','N','O','P','Q','R','S','T','U',
                         'V','W','W','Y','Z']
        
        
    def setOfItems(self):
        #Accessor function for the entire number set.
        print("{0}".format(self.__numSet))
                
    
    def decimalToAny(self,decimal,base=2):
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
            #Special case if the input is in the ones place.
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
            #If the power is greater than or equal to zero, then it
            #evaluates what number would go in its place.
        if power>=0:
            if newDecNumber>=0:
                    #WHILE function determines the number of
                    #times that power goes into the decimal.
                    #Power is then reduced and ran back through
                    #recursively. 
                while newDecNumber>=base**power:
                    amount+=1
                    newDecNumber = newDecNumber-(base**power)
                power-=1
                    #numSet is made where it allows for
                    #higher bases than 2-10.
                return str(self.__numSet[amount])+self.anyNumFinder(newDecNumber,power,base)
            else:
                    #If the number cannot go into the tested value,
                    #then a 0 is put in its place.
                power-=1
                return "0"+self.anyNumFinder(decimal,power,base)
        else:
                #ELSE that acts as the ending for the recursive function.
            return ""
        
       
    def anyToDecimal(self,number,base):
        #Function that takes a binary number,
        #and finds its decimal counterpart.
        
            #String splitting for development later,
            #initializes the decimal output at 0.
        number = str(number).split('b')
        number = number[-1]
        powerNum = len(number)-1
        decimalNum = 0
        
            #Breaks up the inputted number into it's pieces
            #for individual calculations dependant on
            #its place value.
        for char in number:
            
                #If it's 0, power is reduced and moves on to the next place.
            if char == '0':
                powerNum-=1
        
                #If it isn't 0, then the examined item
                #is tried to changed into int,
                #and if it fails then it individually
                #looks through the numSet for its position.
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
                    #Decimal number decided on the place value
                    #to that power with determined base.
                decimalNum += charMultiplier*(base**powerNum)
                powerNum-=1
        return decimalNum
        
        
    def baseToBase(self,number,baseOne,baseTwo):
        #Function that uses the two previous functions to
        #easily change between two given bases, and what
        #base that number is originally from.
        decNum = self.anyToDecimal(number,baseOne)
        return self.decimalToAny(decNum,baseTwo)
        
    def binary(self,number):
        return "0b"+self.decimalToAny(number,2)
    
    def octal(self,number):
        return "0o"+self.decimalToAny(number,8)
    
    def hexadecimal(self,number):
        return "0x"+self.decimalToAny(number,16)
        
        
        
testval = 120
baseTestval = 11
a = baseConverter()

def anyTEST():
    b = a.decimalToAny(testval,baseTestval)
    print(testval)
    print(a.anyToDecimal(b,baseTestval))
    print("\n{0}\n{1}\n".format(a.binary(testval),
                                bin(testval)))
    
    print("{0}\n{1}\n".format(a.octal(testval),
                              oct(testval)))
    
    print("{0}\n{1}\n".format(a.hexadecimal(testval),
                              hex(testval)))
    print(b)
anyTEST()
    
    


