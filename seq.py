class DNASequence:
    countBases = {"A": 0, "C": 0, "G": 0, "T": 0}
    DNA_SEQUENCES = {}
    seqs = []
    ids  = []

    def __init__(self):
        self.__seq = "" 
        self.__id = ""

    def __str__(self):
        return f"seq: {self.__seq}, id: {self.__id}"

    def getId(self):
        return self.__id
    def setId(self, id):
     if len(id) == 0:
        raise ValueError("ID cant be empty")

     if id in DNASequence.ids:
        raise ValueError("ID already exists")

     DNASequence._settingID(self, id)

    def _settingID(self, id):
        if id not in DNASequence.ids:
            DNASequence.ids.append(id)
            self.__id = id

    def getSeq(self):
        return self.__seq

    def setSeq(self, seq):
        seq = seq.upper()
        validChars = ["A", "C", "G", "T"]
        if len(seq) == 0:
            raise ValueError("Seq cant be empty!")
        for char in seq:
            if char not in validChars:
                raise ValueError("SEQ MUST BE: A, C, G, T")
                
        DNASequence._settingSeq(self, seq)

    def _settingSeq(self, seq):
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
    try:
        id = input("Enter your ID: ")
        DNASequence.setId(dna, id)
        seq = input("Enter your DNA sequence: ")
        DNASequence.setSeq(dna, seq)
        return dna
    except ValueError as e:
        if dna.getId() != "":
            DNASequence.ids.remove(dna.getId())
        print(e)
def findId(sequence):
    all_ids = []
    for id, seq in DNASequence.DNA_SEQUENCES.items():
        if seq == sequence:
            all_ids.append(id)
    return all_ids

def findSeq(identification):
    for id, seq in DNASequence.DNA_SEQUENCES.items():
        if identification == id:
            return seq

def getGCpercentage(id):
    if id not in DNASequence.DNA_SEQUENCES:
        return None
    seq = DNASequence.DNA_SEQUENCES[id]
    g = seq.count("G")
    c = seq.count("C")

    return (g + c) / len(seq) * 100


def reverseComplement(id):
    if id not in DNASequence.DNA_SEQUENCES:
        return None
    seq = DNASequence.DNA_SEQUENCES[id]
    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
    result = ""
    for char in seq[::-1]:
        result += complement[char]
    return result

def findPattern(id, pattern):
    if id not in DNASequence.DNA_SEQUENCES:
        return None
    seq = DNASequence.DNA_SEQUENCES[id]
    positions = []
    pattern = pattern.upper()
    if pattern == "":
        return positions
    for i in range(len(seq) - len(pattern) + 1):
        if seq[i:i + len(pattern)] == pattern:
            positions.append(i)
    return positions
