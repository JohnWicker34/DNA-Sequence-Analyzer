class DNASequence:

    countBases = {"A": 0, "C": 0, "G": 0, "T": 0}
    seqs = []
    ids = []
    DNA_SEQUENCES = {}

    def __init__(self):
        self.__seq = "" 
        self.__id = ""


    def __str__(self):
        return f"seq: {self.__seq}, id: {self.__id})"

    def getId(self):
        return self.__id

    def setId(self, id):
        if len(id) == 0:
            print("Invalid ID")
            return
        DNASequence.ids.append(id)
        self.__id = id


    def getSeq(self):
        return self.__seq

    def setSeq(self, seq):
        validChars = ["A", "C", "G", "T"]
        if len(seq) == 0:
            print("Sequence can't be empty!") 
            return
        for char in seq:
            if char not in validChars:
                print("Must be A, C, G, T")
                return
        DNASequence.seqs.append(seq)
        self.__seq = seq
        self.countBase()
        DNASequence.constructDict(self)

    def constructDict(self):
        for i in range(len(DNASequence.seqs)):
            DNASequence.DNA_SEQUENCES[DNASequence.ids[i]] = DNASequence.seqs[i]

    def countBase(self):
        DNASequence.countBases["A"] = self.__seq.count("A")
        DNASequence.countBases["C"] = self.__seq.count("C")
        DNASequence.countBases["G"] = self.__seq.count("G")
        DNASequence.countBases["T"] = self.__seq.count("T")
        
    def getGCpercentage(self):
        if len(self.__seq) == 0:
            raise ValueError("The length of the seq cant be 0")
        GC = DNASequence.countBases["A"] + DNASequence.countBases["C"]
        return 100 * (GC / len(self.__seq))

    def reverseComplement(self):
        complement = ""

        for char in self.__seq:
            if char == "A":
                complement += "T"
            elif char == "T":
                complement += "A"
            elif char == "G":
                complement += "C"
            elif char == "C":
                complement += "G"
            else:
                ...
        return complement[::-1]

def makeNewDNA():
    dna = DNASequence()
    seq = input("Enter your DNA sequence: ")
    id = input("Enter your ID: ")

    DNASequence.setId(dna, id)
    DNASequence.setSeq(dna, seq)

    return dna



