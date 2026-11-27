from seq import DNASequence as seq
from seq import makeNewDNA
from seq import findSeq
from seq import findId
from seq import getGCpercentage
from seq import reverseComplement
from seq import promptChoice 



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
    print("10. Print instructions again.")
    print("11. Exit")

printInstructions()

while True:

    choice : int = promptChoice("Enter a number (1-11): ", "CHOICE MUST BE A NUMBER!")

    match choice:
        case 1:
            makeNewDNA()
        case 2:
            SEQ = input("Enter seq to find id(s) for: ")
            all_ids = findId(SEQ)

            if all_ids:
                for i in range(len(all_ids)):
                    print(f"ID {i+1}: {seq.ids[i]}") 
            else:
                print(f"No ids were found that match the seq: {SEQ}")
        case 3:
            ID = input("Enter id to find seqs for: ")
            print(findSeq(ID))

        case 4:
            #list of all ids that user wants to get GC for 
            IDS = input("Enter id(s) to find GC percentage for: ").split()
            for i in range(len(IDS)):
                print(f"GC percentage of id {i+1} ({seq.ids[i]}) is:", getGCpercentage(IDS[i])) 

        case 5:
            ID = input("Enter id to find reverse compliment for: ")
            sequence = seq.DNA_SEQUENCES[ID]
            print(f"Reverse comp of seq {{sequence}} is:", reverseComplement(ID)) 
        case 6:
            ...
        case 7:
            for identification, sequence in seq.DNA_SEQUENCES.items():
                print(f"ID: {identification}, SEQ: {sequence}")
        case 8:
            ids = seq.ids
            for i in range(len(seq.ids)):
                print(f"ID {i+1}: {ids[i]}")
        case 9:
            seqs = seq.seqs
            for i in range(len(seq.seqs)):
                print(f"SEQ {i+1}: {seqs[i]}")
        case 10:
            printInstructions()
        case 11:
            with open("data.csv", 'a') as file:
                for identification, sequence in seq.DNA_SEQUENCES.items():
                    file.write(identification)
                    file.write(", ")
                    file.write(sequence)
                    file.write("\n")
            print("goodbye!")
            break
        case _:
            print("You cheeky!")



