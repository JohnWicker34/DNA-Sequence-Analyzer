from seq import DNASequence as seq
from seq import makeNewDNA
from seq import findSeq
from seq import findId
from seq import getGCpercentage
from seq import reverseComplement
from seq import findPattern





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
    print("10. Display instructions.")
    print("11. Exit.")
def get_choice():
    while True:
        try:
            choice = int(input("Enter your choice: "))
            return choice
        except ValueError:
            print("Invalid choice. Try again.")
printInstructions()

while True:

    choice = get_choice()

    match choice:
        case 1:
            makeNewDNA()
        case 2:
         SEQ = input("Enter seq to find ids for: ").upper()
         all_ids = findId(SEQ)
         if all_ids:
           for i in range(len(all_ids)):
             print(f"ID {i+1}: {all_ids[i]}")
         else:
           print(f"No ids were found that match the seq: {SEQ}")
        case 3:
         id = input("Enter id to find seq for: ")
         sequence = findSeq(id)
         if sequence:
            print(f"SEQ: {sequence}")
         else:
           print(f"No sequence found for id: {id}")
        case 4:
         ids = input("Enter id(s) to find GC percentage for: ").split()

         for id in ids:
           result = getGCpercentage(id)
         if result is not None:
            print(f"GC percentage of {id}: {result:.2f}%")
         else:
            print(f"ID {id} not found.") 
        case 5:
           id = input("Enter DNA ID: ")
           result = reverseComplement(id)
           if result is not None:
              print("Reverse complement:", result)
           else:
              print("ID not found.")
        case 6:
           id = input("Enter DNA ID: ")
           pattern = input("Enter pattern: ")
           positions = findPattern(id, pattern)
           if positions is None:
              print("ID not found.")
           elif positions == []:
                print("Pattern not found.")
           else:
             print("Pattern positions:", positions)
        case 7:
           for id, sequence in seq.DNA_SEQUENCES.items():
                print(f"ID: {id}, SEQ: {sequence}")
        case 8:
            for i in range(len(seq.ids)):
                print(f"ID {i+1}: {seq.ids[i]}")
        case 9:
            for i in range(len(seq.seqs)):
                print(f"SEQ {i+1}: {seq.seqs[i]}")
        case 10:
           printInstructions()
        case 11:
          print("Goodbye!")
          break
        case _:
          print("Invalid choice. Try again.")



