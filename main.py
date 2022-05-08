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
#A function to decide if 'num' can be converted to a float


def update_leaderboard():
    for player in players:
        print(*player)


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
    #Fetches the record of the event.
    
    while True:
        player = input("What is the name of this player? ")
        score = input("What was the player's time/distance/score? ")
        
        if float_check(score):
            score = float(score)
            players.append([player,score,(score/record)*100])
            update_leaderboard()
        else:
            print("Unable to read score input.")
    
main()