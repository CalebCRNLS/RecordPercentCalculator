#Record Percentage Calculator

#Imports 


#Global Variables
record = None
players = []

def float_check(num):
    try:
        float(num)
        return True
    except:
        return False


def main():
    global record
    global players
    #Global Declerations
    
    while True:
        record_input = input("What is the record for this event? ")
        if float_check(record_input):
            record = float(record_input)
            break
        else:
            print("Unable to read input.")
            
    print(record)
    
main()