#Record Percentage Calculator

#Imports 
from tkinter import *

#Constants
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 400
WINDOW_BORDER = 10

#Global Variables
record = None
players = []

record_input = None
player_name_input = None
player_score_input = None


def float_check(num):
    try:
        float(num)
        return True
    except:
        return False
#A function to decide if 'num' can be converted to a float


def update_leaderboard():
    for player in players:
        if record:
            player[2] = str(round((player[1]/record)*100,2))+"%"
        print(*player)
#Updates the leaderboard and prints it into the output

def create_entry(window,placex,placey,width,height):
    entry = Entry(window)
    entry.place(x=placex+WINDOW_BORDER,y=placey+WINDOW_BORDER,width=width,height=height)
    return entry
#Basic function for creating an entry.      

def create_button(window,placex,placey,width,height,text,command):
    button = Button(window,text=text,command=command)
    button.place(x=placex+WINDOW_BORDER,y=placey+WINDOW_BORDER,width=width,height=height)
    return button
#Basic function for creating a button and connecting it to a function.

def create_label(window,placex,placey,width,height,text,wraplength):
    label = Label(window,text=text,wraplength=wraplength)
    label.place(x=placex+WINDOW_BORDER,y=placey+WINDOW_BORDER,width=width,height=height)
    return label
#Basic function for creating a label

#BUTTON RECEIVER FUNCTIONS
def on_submit_button_pressed():
    global player_name_input
    global player_score_input
    global record
    
    player = player_name_input.get()
    score = player_score_input.get()
    #Fetches the player's name and score
    
    if float_check(score):
        score = float(score)
        if record:
            players.append([player,score,(score/record)*100])
        else:
            players.append([player,score,"N/A"])
        update_leaderboard()
        #Adds the player to the list of players
        
        player_name_input.delete(0,END)
        player_score_input.delete(0,END)
        #Clears the input fields
    else:
        print("Unable to read score input.")


def on_record_button_pressed():
    global record_input
    global record
    
    if float_check(record_input.get()):
        record = float(record_input.get())
    else:
        record = None
    
    update_leaderboard()

def main():
    global record
    global players
    
    global record_input
    global player_name_input
    global player_score_input
    #Global Declerations
    
    window = Tk()
    window.geometry(str(WINDOW_WIDTH+(WINDOW_BORDER*2))+"x"+str(WINDOW_HEIGHT+(WINDOW_BORDER*2)))
    
    record_input = create_entry(window,0,0,50,20)
    record_input_label = create_label(window,0,20,50,20,"Record",50)
    record_submit_button = create_button(window,60,0,20,20,"<",on_record_button_pressed)
    #Record Fetching Field
    
    player_name_input = create_entry(window,50,50,180,20)
    player_name_label = create_label(window,50,70,180,20,"Player Name",100)
    
    player_score_input = create_entry(window,240,50,100,20)
    player_score_label = create_label(window,240,70,100,20,"Player Score",100)
    
    submit_button = create_button(window,WINDOW_WIDTH-20,50,20,20,"+",on_submit_button_pressed)
    #Player input fields
    
    window.mainloop()
    
main()