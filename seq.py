class DNASequence:

    countBases = {"A": 0, "C": 0, "G": 0, "T": 0}
    seqs = []
    ids  = []
    DNA_SEQUENCES = {}

    with open("data.csv", 'r') as file:
        for line in file:
            if line in ["\n"]:
                break
            ids.append(line.split(", ")[0])
            seqs.append(line.split(", ")[1])


    def __init__(self):
        self.__seq = "" 
        self.__id = ""

    def __str__(self):
        return f"seq: {self.__seq}, id: {self.__id})"

    def getId(self):
        return self.__id

    def setId(self, id):
        if len(id) == 0:
            raise ValueError("ID cant be empty!")
        DNASequence._settingID(self, id)

    def _settingID(self, id):
        if id not in DNASequence.ids:
            DNASequence.ids.append(id)
            self.__id = id

    def getSeq(self):
        return self.__seq

    def setSeq(self, seq):
        validChars = ["A", "C", "G", "T"]
        if len(seq) == 0:
            raise ValueError("Seq cant be empty!")
        for char in seq:
            if char.upper() not in validChars:
                raise ValueError("SEQ MUST BE: A, C, G, T")
                
        DNASequence.__settingSeq(self, seq)

    #dont change ever
    def __settingSeq(self, seq):
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
        

def makeNewDNA():
    dna = DNASequence()
    id = input("Enter your ID: ")
    DNASequence.setId(dna, id)
    seq = input("Enter your DNA sequence: ")
    DNASequence.setSeq(dna, seq)

    return dna


def getGCpercentage(id):
    if len(id) == 0:
        raise ValueError("The length of the id can't be 0")
    GC = DNASequence.countBases["G"] + DNASequence.countBases["C"]
    return 100 * (GC / len(DNASequence.DNA_SEQUENCES[id]))


def reverseComplement(id):
    complement = ""

    for char in DNASequence.DNA_SEQUENCES[id]:
        match char:
            case 'A':
                complement += "T"
            case 'T':
                complement += "A"
            case 'G':
                complement += "C"
            case 'C':
                complement += "G"
            case _:
                ...
    return complement[::-1]


def promptChoice(prompt, err):
    while True:
        try:
            choice = int(input((prompt)))
        except ValueError:
            print(err)
        else:
            return choice

def findId(sequence):
    all_ids = []
    for id, seq in DNASequence.DNA_SEQUENCES.items():
        if sequence == seq:
            all_ids.append(id)
    return all_ids

def findSeq(identification):
    return DNASequence.DNA_SEQUENCES[identification] 

def findPattern(id, pattern):
    print("findPattern is in progress")
    ...
