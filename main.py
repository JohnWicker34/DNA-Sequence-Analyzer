from seq import DNASequence as seq
from seq import makeNewDNA
from seq import findSeq
from seq import findId
from seq import getGCpercentage
from seq import reverseComplement





def printInstructions():
    print("1. Add DNA.")
    print("2. Find DNA names.")
    print("3. Find DNA seq.")
    print("4. Get GC percentage.")
    print("5. Reverse Compliment.")
    print("6. Find Pattern")
    print("7. Print all ids and seqs.")
    print("8. Print all ids.")
    print("9. Print all seqs.")

printInstructions()

while True:

    choice = int(input())

    match choice:
        case 1:
            makeNewDNA()
        case 2:
            SEQ = input("Enter seq to find ids for: ")
            all_ids = findSeq(SEQ)
            if all_ids:
                for i in range(len(all_ids)):
                    print(f"ID {i+1}: {all_ids[i]}") 
            else:
                print(f"No ids were found that match the seq: {seq}")
        case 3:
            id = input("Enter id to find seqs for: ")
            all_seqs = findId(id)
            if all_seqs:
                for i in range(len(all_seqs)):
                    print(f"ID {i+1}: {all_seqs[i]}") 
            else:
                print(f"No seqs were found that match the id: {id}")
        case 4:
            ids = input("Enter id(s) to find GC percentage for: ").split()
            for i in range(len(ids)):
                print(f"GC percentage of id {i+1} ({seq.ids[i]}) is:", getGCpercentage(ids[i])) 
        case 5:
            ...
        case 6:
            ...
        case 7:
            for id, seq in seq.DNA_SEQUENCES.items():
                print(f"ID: {id}, SEQ: {seq}")
        case 8:
            for i in range(len(seq.ids)):
                print(f"ID {i+1}: {seq.ids[i]}")
        case 9:
            for i in range(len(seq.seqs)):
                print(f"SEQ {i+1}: {seq.seqs[i]}")
        case _:
            ...



