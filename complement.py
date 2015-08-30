class ReverseComplement(object):
    
    def __init__(self, sequence, reverse = True):
        if reverse:
            self.inputSeq = sequence[::-1]
        else:
            self.inputSeq = sequence
        self.inputSeq = self.inputSeq.upper()
        self.complementTable = self.createComplementTable()
        self.complementLists = self.createComplementLists()
        self.checkInput()
        self.outputSeqString = self.createOutputString()
        self.outputList = False
        
    def __str__(self):
        return self.outputSeqString
        
    def createComplementTable(self):
        complementTable =  {"A":"T",
                            "T":"A",
                            "G":"C",
                            "C":"G",
                            "Y":"R",
                            "R":"Y",
                            "S":"S",
                            "W":"W",
                            "K":"M",
                            "M":"K",
                            "B":"V",
                            "D":"H",
                            "H":"D",
                            "V":"B",
                            "N":"N"}
        return complementTable
    
    def createComplementLists(self):
        complementLists =  {"A":["T"],
                            "T":["A"],
                            "G":["C"],
                            "C":["G"],
                            "Y":["G","A"],
                            "R":["T","C"],
                            "S":["C","G"],
                            "W":["T","A"],
                            "K":["A","C"],
                            "M":["T","G"],
                            "B":["G","C","A"],
                            "D":["T","C","A"],
                            "H":["T","G","A"],
                            "V":["T","G","C"],
                            "N":["T","G","C","A"]}
        return complementLists
    
    def checkInput(self):
        for letter in self.inputSeq:
            if letter not in list(self.complementTable.keys()):
                raise ValueError(letter + " in " + self.inputSeq + " is not a valid DNA base.")
            
    def createOutputString(self):
        output = ""
        for letter in self.inputSeq:
            output += self.complementTable[letter]
        return output
    
    def permutations(self):
        import itertools
        if self.outputList:
            return self.outputList
        letterList = []
        for letter in self.inputSeq:
            letterList.append(self.complementLists[letter])
        self.outputList = [''.join(letter) for letter in itertools.product(*letterList)]
        return self.outputList
    
class RNAReverseComplement(ReverseComplement):
    
    def createComplementTable(self):
        complementTable =  {"A":"U",
                            "T":"A",
                            "U":"A",
                            "G":"C",
                            "C":"G",
                            "Y":"R",
                            "R":"Y",
                            "S":"S",
                            "W":"W",
                            "K":"M",
                            "M":"K",
                            "B":"V",
                            "D":"H",
                            "H":"D",
                            "V":"B",
                            "N":"N"}
        return complementTable
    
    def createComplementLists(self):
        complementLists =  {"A":["U"],
                            "T":["A"],
                            "U":["A"],
                            "G":["C"],
                            "C":["G"],
                            "Y":["G","A"],
                            "R":["U","C"],
                            "S":["C","G"],
                            "W":["U","A"],
                            "K":["A","C"],
                            "M":["U","G"],
                            "B":["G","C","A"],
                            "D":["U","C","A"],
                            "H":["U","G","A"],
                            "V":["U","G","C"],
                            "N":["U","G","C","A"]}
        return complementLists
    
    
    
    
import datetime
test = ReverseComplement("atgcnyag")
rnatest = RNAReverseComplement("atgcnyag")
print(test)
print(rnatest)
start = datetime.datetime.now()
dna = test.permutations()
runTime = str(datetime.datetime.now()-start)
print("Shorter template took: " + runTime)
rna = rnatest.permutations()
for i in range(0,5):
    print(dna[i])
print(str(len(dna)) + " elements")
for i in range(0,5):
    print(rna[i])
test = ReverseComplement("atgnnnnkwsrycgtvhdnn")
rnatest = RNAReverseComplement("atgnnnnkwsrycgtvhdnn")
print(test)
print(rnatest)
start = datetime.datetime.now()
dna = test.permutations()
runTime = str(datetime.datetime.now()-start)
print("Longer template took: " + runTime)
rna = rnatest.permutations()
for i in range(0,5):
    print(dna[i])
print(str(len(dna)) + " elements")
for i in range(0,5):
    print(rna[i])
