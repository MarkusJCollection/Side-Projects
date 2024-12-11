class arithmeticallyEncode():
    
    def __init__(self,inputValue):
        
        self.input = inputValue
        self.letterIntervals = {}
        self.decodeDict = {}
        self.letterWidths = {}
        self.encoding = 0
        self.decoding = ''
        self.arithmeticallyEncode()
        
    
    def arithmeticallyEncode(self):
        self.createDictionaries()
    
    def createDictionaries(self):
        outputDict = {"stringLength":len(self.input)}
        sortedList = []
        for char in self.input:
            if not (char in outputDict):
                sortedList.append(char)
                outputDict[char] = 1
            else:
                outputDict[char] += 1
        sortedList.sort()
        leftSide = 0
        for entry in sortedList:
            rightSide = leftSide+outputDict[entry]/outputDict["stringLength"]
            self.letterIntervals[entry] = (leftSide, rightSide)
            self.letterWidths[entry] = rightSide-leftSide
            self.decodeDict[leftSide] = entry
            leftSide = rightSide
        self.decodeDict[1] = "###"
        return 1
    
        
    def encode(self):
        currentTuple = (0,1)
        for char in self.input:
            width = currentTuple[1]-currentTuple[0]
            currentTuple = ((currentTuple[0]+(width*self.letterIntervals[char][0]))
                                 ,(currentTuple[0]+(width*self.letterIntervals[char][1])))
        self.encoding = currentTuple[0]
        #print(currentTuple)
        return 1
    
    def decode(self, decodeNum = True):
        outputString = ''
        if decodeNum:
            decodeNum = self.encoding
        for i in range(len(self.input)):
            previousEntry = None
            for entry in self.decodeDict:
                if decodeNum > 1:
                    return print("decode > 1")
                if decodeNum < entry:
                    outputString += self.decodeDict[previousEntry]
                    decodeNum = (decodeNum-previousEntry)/self.letterWidths[self.decodeDict[previousEntry]]
                    break
                else:
                    
                    previousEntry = entry
        print(outputString)
        return 1
    
    
        


    



inputString = "DOWNADOWNBDOWNCDOWN"
inputString2 = "DOWNTONCOW"

a = arithmeticallyEncode(inputString)

a.encode()
a.decode()
