class ReverseComplement(object):  #declares an object class.  We capitalize the first letter (unlike variables that should start with lowercase) to avoid potential collisions with variable names
    
    def __init__(self, sequence, reverse = True):  #this is a special function (within an object, a function is usually called a method) that must be present in (almost) every object class.  It is implicitly called when the object is instantiated.  For more on instantiation, see the main() running code.
        if reverse:  #we defined an optional argument "reverse" to be true.  We did this because we assume people will often want the reverse complement.  They have to specify reverse = False if they don't.
            self.inputSeq = sequence[::-1]  #Neat trick in Python to reverse the order of an iterable (string, list, etc).  Indexing goes [inclusive start:non-inclusive end:step].  A step of -1 tells it to start from the end and step backwards 1 element at a time.  This seems to run slightly more efficiently than iterating in reverse.
        else: #if the user wants a non-reverse complement
            self.inputSeq = sequence  #we store the value without reversing.  The self.[name] means that this value will be variable that can be called from anywhere within this instance of the object AND from outside the object by calling [instance].[name].  A variable that is tied to a function like this one is called an attribute. 
        self.inputSeq = self.inputSeq.upper()  #for convenience, we are working entirely with uppercase letters.  If the user supplies lowercase, we raise them.  If we did not, we would get an exception when we look through our complement dictionary.  A possible improvement to this would be letting the users choose to have the return in lowercase or even preserve their original case.  How might we do that?
        self.complementTable = self.createComplementTable()  #this is defining an attribute of the object (complementTable) by calling the createComplementTable method.  Of interest, since the table is just returned by the function, a program could call the table for its own use by calling [instance].createComplementTable()
        self.complementLists = self.createComplementLists()  #same as above, but this one gets back all non-degenerate possibilities
        self.checkInput() #always good to validate inputs.  This will handle any invalid letters entered.  It will still raise an exception, but will be more specific in the error reporting.
        self.outputSeqString = self.createOutputString()  #Creates the outputString (the reverse complement).  Because this is called in the __init__ initializer method, we automatically calculate the reverse complement (why this is convenient will be covered in the __str__ overload method)
        self.outputList = False  #this initializes an attribute to False.  Why we want to do this will be covered as part of a later method.
        
    def __str__(self):  #this is overloading the existing str(object) method.  Normally, if I tried to print(thisObject), I would either get an exception or a bunch of rubbish back.
        return self.outputSeqString  #Instead, this says that if I try to print the entire object or turn it to a string, what I REALLY want to get back is the outputSeqString I created in the initialization function
        
    def createComplementTable(self):  #Simple method that returns a fixed dictionary.  Because it is a built-in method of the class, it can be called from within as self.createComplementTable or from outside the object as [instance].createComplementaryTable.
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
    
    def createComplementLists(self):  #Same concept as the previous method.  I should note that these could have both been stuck inside the initializer method, but this makes for much cleaner code.
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
    
    def checkInput(self):  #Input validation
        for letter in self.inputSeq:   #iterate over the input letters
            if letter not in list(self.complementTable.keys()):  #get a list of keys from the complement table, and if a letter is in the input sequence that is not a key in the table
                raise ValueError(letter + " in " + self.inputSeq + " is not a valid DNA base.")  #Raise an exception that explicitly lists what the problem was and where.  Help the user help themselves.
            
    def createOutputString(self):  #This simple function creates our most basic output: a reverse complement string containing any degeneracy that may have been in the original
        output = ""  #intiialize an empty string
        for letter in self.inputSeq:  #iterate over our input string (which, if appropriate was reversed in the initializer)
            output += self.complementTable[letter]  #add on the proper complementary base to the growing output string
        return output  #return the output
    
    def permutations(self):  #turn a sequence containing degenerate bases into a list of all possible non-degenerate sequences
        import itertools  #this library contains the code we need to create all possible permutations and probably does so more efficiently than our own code would
        if self.outputList:  #if we already have the value we are trying to create here (and we can tell because it is no longer the False value we initialized it to)
            return self.outputList  #we avoid repeating previous work and just output what we already have stored.  As will be shown in the test code below, the work required for this function can grow exponentially.  We only want to run it if it is requested AND we only ever want to run it the one time.
        letterList = []  #initialize an empty list to store a list of lists, where the outer list will correspond to the letters of the sequence and each inner list will represent all possibilities for that letter
        for letter in self.inputSeq:  #iterate over the input sequence
            letterList.append(self.complementLists[letter])  #add a list of possible bases to a growing list of possible bases at each position
        self.outputList = [''.join(letter) for letter in itertools.product(*letterList)]  #use the itertools module's product function to create the permutations (if this line seems strange to you, try looking up list comprehension in python and positional arguments, commonly called *args)
        return self.outputList #return the (potentially quite large) list
    
class RNAReverseComplement(ReverseComplement):  #declare another class called RNAReverseComplement as an extension of the ReverseComplement base class
    
    def createComplementTable(self):  #because the only real change we need is the inclusion of Uracil, we are overriding the table creation methods from the base class to include it.  Otherwise, everything else is the same.
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
    
    def createComplementLists(self):  #as before, this overrides the base class method.  We could also add entirely new methods.
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
    
    
    
def main():    
    import datetime  #This module is just for timing how long it takes for certain things to happen, and is otherwise not necessary for actual data processing.
    test = ReverseComplement("atgcnyag")  #THIS IS INSTANTIATION.  We have defined an object by the name of test with the ReverseComplement class.
    rnatest = RNAReverseComplement("atgcnyag")  #Now we instantiate an object of our extended RNA class
    print(test) #If the overloading of the __str__ worked, we should get back our reverse complement directly from this.  If not, we get an exception or a bunch of rubbish.  Try this again with the overloading method commented out and see how it behaves.
    print(rnatest)  #Inheritance is the concept that an extension of a base class (such as RNAReverseComplement) inherits the base attributes and methods, so long as they were not overridden (as the table creation methods were).
    start = datetime.datetime.now()  #Simply marks the start time for what we are about to do
    dna = test.permutations()  #creates the list of permutations of non-degenerate bases
    runTime = str(datetime.datetime.now()-start)  #Once the permutations are all made, subtract the start time from the current time to see about how long that took.  This should have been relatively painless
    print("Shorter template took: " + runTime)  #Report back the result
    rna = rnatest.permutations()  #Get the RNA permutations
    for i in range(0,5):  #prints a sample of the results from both the RNA and DNA templates
        print(dna[i])
    print(str(len(dna)) + " elements")
    for i in range(0,5):
        print(rna[i])
    test = ReverseComplement("atgnnnnkwsrycgtvhdnn")  #overwrites the previous instance of the ReverseComplement class stored as test with the new one base off this longer, more degenerate sequence
    rnatest = RNAReverseComplement("atgnnnnkwsrycgtvhdnn")
    print(test)  #and again we show how the overloaded __str__ operator works.  Of note, other operators, such as comparisons and arithmetic can be overloaded as well
    print(rnatest)
    start = datetime.datetime.now()  #initiate a timer as we did above
    dna = test.permutations()  #get all the permutations for this much worse sequence
    runTime = str(datetime.datetime.now()-start)
    print("Longer template took: " + runTime) #report back how long it took (this should have taken over a second to determine)
    rna = rnatest.permutations()
    start = datetime.datetime.now()  #initiate a timer again
    dna = test.permutations()  #get all the permutations for this much worse sequence, but remember how we included a catch before to reuse the previously-calculated value of we had one?
    runTime = str(datetime.datetime.now()-start)
    print("Pre-calculated long template took: " + runTime) #report back how long it took (this should be better, since we just report back what was already calculated).  Now that you have an idea of how much time this can take, and how much memory can be occupied by it, does it make sense that this was left out of the initializer method?  Imagine if this were being run on thousands of sequences or millions where we didn't need all the permutations.  So much wasted time.
    for i in range(0,5):
        print(dna[i])
    print(str(len(dna)) + " elements")  #because this can grow exponentially
    for i in range(0,5):
        print(rna[i])
    print(ReverseComplement("atgcnyag"))  #Something else we can get away with because of overloading
    revComp = RNAReverseComplement("atgcnyag")
    print(revComp)
    otherInstance = ReverseComplement("agaattccttccagaa")  #we can instantiate a completely new object of the ReverseComplement class called, conviently enough, otherInstance
    print(otherInstance)
    print(rnatest)  #note that because these objects are two completely different instances, they are only structured and behave the same... they do not interfere with one another or interact unless we make them
        
main()
