class baseConverter():
    """
        Multipurpose class that supports the conversions of
            integers and decimals alike. 
        
        
        ---HIGHEST ALLOWED BASE: 62---
        
        CLASS_NAME = baseConverter()
            CLASS_NAME.setOfItems()
            
    Functions take an integer input and can convert from base_10
        to any other supported base. Base to base is integrated
        for conversions such as base_5 to base_7.

        CLASS_NAME.integerToAnyBaseBase(INTEGER_NUMBER, BASE)
        CLASS_NAME.anyBaseToInteger(NUMBER_IN_SAID_BASE, BASE)
        CLASS_NAME.baseToBase(INTEGER, BASE_ONE, BASE_TWO)        
        
        
    Premade functions for conversion of an integer into it's
        binary, octal, and hexadecimal counterparts.
        
        CLASS_NAME.binary(INTEGER)
        CLASS_NAME.octal(INTEGER)                           
        CLASS_NAME.hexadecimal(INTEGER)
        
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
                
    
    
    def integerToAnyBase(self,integer,base=2):
        #Takes an input of an integer number that will then
        #be changed into a binary string.
        
            #Sets the starting power to 0.
        powerNum = 0
        integer = int(integer)
            #Finds the smallest, largest power that the number can have.
            #Ex. 2^2=4 is the smallest, largest power if the input was 3.
        while base**powerNum<=integer:
            powerNum+=1
            #Special case if the input was 0.
        if powerNum == 0:
            return "0"
            #Special case if the input is in the ones place.
        elif powerNum < 2:
            return "{0}".format(self.__numSet[integer])
            #If a special case isn't hit, then a recursive function is ran.
        else:
            powerNum-=1
            return self.integerNumFinder(integer,powerNum,base)


    def integerNumFinder(self,integer,power,base=2):
        #Recursive function that takes an input of
        #the number, and what power of 2 is being tested.
        #---- Takes the largest number that can go into it,
        #---- and progressively goes down until 0 is reached.
        
        newIntNumber = integer-(base**power)
        amount = 1
            #If the power is greater than or equal to zero, then it
            #evaluates what number would go in its place.
        if power>=0:
            if newIntNumber>=0:
                    #WHILE function determines the number of
                    #times that power goes into the decimal.
                    #Power is then reduced and ran back through
                    #recursively. 
                while newIntNumber>=base**power:
                    amount+=1
                    newIntNumber = newIntNumber-(base**power)
                power-=1
                    #numSet is made where it allows for
                    #higher bases than 2-10.
                return str(self.__numSet[amount])+self.integerNumFinder(newIntNumber,power,base)
            else:
                    #If the number cannot go into the tested value,
                    #then a 0 is put in its place.
                power-=1
                return "0"+self.integerNumFinder(integer,power,base)
        else:
                #ELSE that acts as the ending for the recursive function.
            return ""
        
       
    def anyBaseToInteger(self,number,base):
        #Function that takes any whole base number,
        #and finds its integer counterpart.
        
            #String splitting for development later,
            #initializes the decimal output at 0.
        number = str(number).split('b')
        number = number[-1]
        powerNum = len(number)-1
        integerNum = 0
        
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
                    #Integer number decided on the place value
                    #to that power with determined base.
                integerNum += charMultiplier*(base**powerNum)
                powerNum-=1
        return integerNum
        
        
    def baseToBase(self,number,baseOne,baseTwo):
        #Function that uses the two previous functions to
        #easily change between two given bases, and what
        #base that number is originally from.
        
        decNum = self.anyBaseToInteger(number,baseOne)
        return self.integerToAnyBase(decNum,baseTwo)
        
        
        
    def binary(self,number):
        #Preset function for binary conversions.
        return "0b"+self.integerToAnyBase(number,2)
    
    def octal(self,number):
        #Preset function for octal conversions.
        return "0o"+self.integerToAnyBase(number,8)
    
    def hexadecimal(self,number):
        #Preset function for hexadecimal conversions.
        return "0x"+self.integerToAnyBase(number,16)
    
    
    ###############
    ###############
    ###############
    
    
    
    def decimalToBinary(self,number=1,power=0,depth=0):
        #Only takes an input of a 0.[SOMETHING].
        #The left side of a point can be evaluated using
        #the binary function that deals with integers.
        
        
            #Since it's dealing with decimals, there's
            #a preset depth for 25 bits as to not hit
            #the max recursion depth/keep going for infinity
            #in order to represent some values.
        depth+=1
            #Conversion of the number to float allows for
            #easier handling.
        number = float(number)
        if depth == 25:
                #If 25 is reached, the program ends.
            return ""
        else:
                #Automatically reduces the power each time the function is ran.
            power -= 1
                #Calculates the new number for subtraction.
            newNum = number - 2**power
                #Other exit function if the number is found and is equal to zero.
            if number == 0:
                return ""
            else:
                    #If the subtraction is valid and leaves a non-negative number,
                    #then a 1 is appended showing such.
                    #----Otherwise a 0 is added and it moves on to the next power.
                if newNum>=0:
                    return "1"+self.decimalToBinary(newNum,power,depth)
                else:
                    return "0"+self.decimalToBinary(number,power,depth)
                
                
    def binaryToDecimal(self,number=1):
        #Reverses the process and converts the decimal
        #part of a binary string into it's decimal counterpart.
        #Only takes the input of 0.[BINARYSTRING]
        
            #Initializes the power at -1, and the output to 0.
        power = -1
        numOut = 0
            #Converts the number into a string for
            #the ability to iterate through it.
        number = str(number)
        for char in number:
                #If it's not zero then the number is
                #taken to that power of 2.
            if int(char) != 0:
                numOut += 2 ** power
                power-=1
            else:
                power-=1
        return numOut
             
             
    def binaryDecimal(self,decimal=1):
        #Premade function for use of converting
        #decimal numbers to binary.
        
        
            #Splits the conversions between the integer
            #function and the decimalToBinary function.
        wholeNum = decimal//1
        decimal -= wholeNum
        return self.integerToAnyBase(wholeNum,2)+"."+self.decimalToBinary(decimal)
    
                    
        #####################
        #####################
        #####################
                    
                    
                    
                    
    def decimalToAnyBase(self,number=1,base=2,depth=0):
        #Copy of decimal to binary conversion function
        #with it's capabilities extended to suit any
        #valid base.
        
            #Check for if max bit length has been reached.
        if depth == 25:
            return ""
        else:
                #If max length isn't reached, one is added to the depth.
            depth+=1
                #If the number isn't already a float, it is converted to one.
            if type(number) != float:
                number = float(number)
                
                #Method used to figure out what number
                #should be appended at each spot.
            newNum = number * base
                #If the number is 0 then there are no more parts,
                #and the recursive program ends.
            if number == 0:
                return ""
            else:
                    #If the new number is >0, then it's integer counterpart
                    #is appended as a value in the new base, and the rest
                    #of the number is then repeated recursively until the
                    #max depth is reached or the number is 0.
                if newNum>0:
                    wholeNum = int(newNum//1)
                    newNum -= wholeNum
                    return str(self.__numSet[wholeNum])+self.decimalToAnyBase(newNum,base,depth)
                else:
                    return "0"+self.decimalToAnyBase(number,base,depth)
          
        
    def anyBaseToDecimal(self,number=1,base=2):
        #Inverse of the previous function, and takes the decimal counterpart
        #of any base and converts it into the proper one.
        
        
            #Looks for a decimal point in the number, and if there isn't one
            #then the number is converted to float.
        for char in number:
            hasDecimal = False
            if char == '.':
                hasDecimal = True
        if not hasDecimal:
            number = float(number)
    
            #Initializes the power at -1 and the returning number as 0.
        power = -1
        numOut = 0
        
            #Taking the floating number, it is split at the decimal point
            #into a list, and the second half is defined as the new number.
        number = str(number)
        numList = number.split('.')
        number = numList[-1]
            #Iterates through the second half determining
            #the decimal value of that position.
            #----Automatically reduces power.
        for char in number:
            if char == '0':
                power-=1
            else:
                    #Tries to automatically convert it into an integer,
                    #and if that fails then it parses through the number set
                    #to find it's value.
                try:
                    numout+= (base**power)*int(char)
                except:
                    counter = 0
                    for item in self.__numSet:
                        if str(item) == char:
                            numOut += (base**power)*counter
                        else:
                            counter+=1
                power-=1
            #First half is ran through the integer converter
            #and added to whatever was evaluated.
        return int(self.anyBaseToInteger(numList[0],base))+numOut
    
        
        
    def numberToAnyBase(self,number,base):
        #Combines the efforts of the decimal to any base
        #and integer to any base for a complete package of
        #conversion.
        
            #Finds the integer part of the number and makes it the whole number.
            #The decimal number then becomes the rest after having the whole parts
            #subtracted.
        wholeNum = number//1
        decNumber = number-wholeNum
            #Extra try: except: even though no issues were had.
        try:
            if decNumber == 0:
                #If the number was 0 then it was a whole number so only the integer part is ran.
                return self.integerToAnyBase(wholeNum,base)
            else:
                #Anything else is ran through the whole gaunlet.
                return self.integerToAnyBase(wholeNum,base) + "." + self.decimalToAnyBase(decNumber,base)
        except:
            return print("No idea what the error is")
        
        
        ##############
        ##############
        ##############
        
        
        
        #Test values and functions for use of testing the program.
testval = 31251216
baseTestval = 10
a = baseConverter()


def anyFracTest():
    c = a.numberToAnyBase(testval,baseTestval)
    d = a.anyBaseToDecimal(c,baseTestval)
    print(c)
    print(d)
    print(testval)
#anyFracTest()

def binFracTest():
    c = a.binaryDecimal(testval)
   # d = a.binaryToDecimal(c)
    print(c)
   # print(d)
    print(testval)
#binFracTest()


def integerTEST():
    b = a.integerToAnyBase(int(testval),baseTestval)
    
    print(int(testval))
    print(a.anyBaseToInteger(b,baseTestval))
    
    print("\n{0}\n{1}\n".format(a.binary(testval),
                                bin(int(testval))))
    
    print("{0}\n{1}\n".format(a.octal(testval),
                              oct(int(testval))))
    
    print("{0}\n{1}\n".format(a.hexadecimal(testval),
                              hex(int(testval))))
    print(b)
#integerTEST()
    

