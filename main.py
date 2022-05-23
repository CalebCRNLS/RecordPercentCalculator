#Record Percentage Calculator

#Imports 
from tkinter import *

#Constants
WINDOW_WIDTH = 375
WINDOW_HEIGHT = 350
WINDOW_BORDER = 10

PLAYERS_PER_PAGE = 10

COLOUR_RED = "#f52929"
COLOUR_GREEN = "#73f547"

#Global Variables
record = None
players = []

record_input = None
player_name_input = None
player_score_input = None

leaderboard_places = []
current_page = 0
page_label = None

score_high_to_low = None

def float_check(num):
    try:
        float(num)
        return True
    except:
        return False
#A function to decide if 'num' can be converted to a float

def sorter(value):
    return value[1]
    
def delete_player(position):
    global players
    global current_page
    global PLAYERS_PER_PAGE
    
    
    players.pop((PLAYERS_PER_PAGE*current_page)+position)
    update_leaderboard()


def update_leaderboard():
    global current_page
    global players
    global score_high_to_low
    
    players.sort(reverse=not score_high_to_low.get(),key=sorter)
    
    place = 0
    for count in range(current_page*10,(current_page*10)+10):
        
        if count > len(players)-1:
            break
        #Breaks out of the loop if it runs out of players
        
        if record:
            players[count][2] = str(round((players[count][1]/record)*100,2))+"%"
        else:
            players[count][2] = "-"
        #Checks to see what the record is and if it needs updating.
        
        leaderboard_places[place][0].config(text="#"+str(count+1))
        leaderboard_places[place][1].config(text=players[count][0])
        leaderboard_places[place][2].config(text=str(players[count][1]))
        leaderboard_places[place][3].config(text=players[count][2])
        #Updates each spot on the leaderboard
        
        place += 1
        #Update place variable (used to track which leaderboard slot to place each player in)
    
    if place < PLAYERS_PER_PAGE:
        for count in range(place,PLAYERS_PER_PAGE):
            leaderboard_places[count][0].config(text="-")
            leaderboard_places[count][1].config(text="-")
            leaderboard_places[count][2].config(text="-")
            leaderboard_places[count][3].config(text="-")       
    
    page_label.config(text = str(current_page+1)+"/"+str(count_pages()))
    #Refreshes the page counter
    
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

def create_checkbutton(window,placex,placey,text,variable,command,onvalue,offvalue):
    checkbutton = Checkbutton(window,text=text,variable=variable,command=command,onvalue=onvalue,offvalue=offvalue)
    checkbutton.place(x=placex,y=placey)
    return checkbutton

#BUTTON RECEIVER FUNCTIONS
def on_submit_button_pressed():
    global player_name_input
    global player_score_input
    global record
    
    player = player_name_input.get()
    score = player_score_input.get()
    #Fetches the player's name and score
    
    if float_check(score) and player:
        score = float(score)
        if record:
            players.append([player,score,(score/record)*100])
        else:
            players.append([player,score,"-"])
        update_leaderboard()
        #Adds the player to the list of players
        
        player_name_input.delete(0,END)
        player_score_input.delete(0,END)
        #Clears the input fields
    


def on_record_button_pressed():
    global record_input
    global record
    
    if float_check(record_input.get()):
        record = float(record_input.get())
    
    update_leaderboard()

def on_clear_button_pressed():
    players.clear()
    update_leaderboard()
    #Clears and refreshes the leaderboard.

def count_pages():
    global players
    global PLAYERS_PER_PAGE
    
    pages = round(len(players)/PLAYERS_PER_PAGE)
    if pages < len(players)/PLAYERS_PER_PAGE:
        pages += 1
    #This chunk of code will round upwards.
    
    if pages == 0:
        pages = 1
    return pages

def on_page_change(direction):
    global current_page
    global players
    global PLAYERS_PER_PAGE
    global page_label
    
    
    pages = count_pages()
    
    if pages == 0:
        pages = 1    
    #This code will set the number of pages to 1 if the number of pages is 0 (as 0 simply means nothing has been inputted yet)
    
    
    current_page += direction
    if current_page < 0:
        current_page = pages - 1
    elif current_page >= pages:
        current_page = 0
    
    
    page_label.config(text = str(current_page+1)+"/"+str(pages))
    #Moves the current page in the direction specified. If the current page is out of range it will wrap.
    
    update_leaderboard()
    #Refreshes the leaderboard.

def main():
    global record
    global players
    
    global record_input
    global player_name_input
    global player_score_input
    
    global page_label
    global score_high_to_low
    
    global COLOUR_RED
    #Global Declerations
    
    window = Tk()
    
    window.geometry(str(WINDOW_WIDTH+(WINDOW_BORDER*2))+"x"+str(WINDOW_HEIGHT+(WINDOW_BORDER*2)))
    window.title("Athlete Scoreboard")
    window.resizable(0,0)
    
    record_input = create_entry(window,0,0,50,20)
    record_input_label = create_label(window,0,20,50,20,"Record",50)
    record_submit_button = create_button(window,60,0,20,20,"+",on_record_button_pressed)
    record_submit_button.config(bg = COLOUR_GREEN)
    #Record Fetching Field
    
    score_high_to_low = BooleanVar()
    sort_checkbutton = create_checkbutton(window,250,40,"Reverse Order",score_high_to_low,update_leaderboard,True,False)
    
    #Radio buttons to decide if the list should be sorted high-to-low or low-to-high
    
    player_name_input = create_entry(window,50,50,180,20)
    player_name_label = create_label(window,50,70,180,20,"Athlete Name",100)
    
    player_score_input = create_entry(window,240,50,100,20)
    player_score_label = create_label(window,240,70,100,20,"Athlete Score",100)
    
    submit_button = create_button(window,350,50,20,20,"+",on_submit_button_pressed)
    submit_button.config(bg = COLOUR_GREEN)
    #Player input fields
    
    height = 20
    offset_y = 100
    
    for place in range(1,PLAYERS_PER_PAGE+1):
        delete_button = create_button(window,0,offset_y+(height*place),20,height,"X",lambda place=place :delete_player(place-1))
        delete_button.config(bg = COLOUR_RED)
        #Button for deleting individual players
        
        rank_label = create_label(window,25,offset_y+(height*place),25,height,"-",0)
        name_label = create_label(window,50,offset_y+(height*place),180,height,"-",0)
        score_label = create_label(window,230,offset_y+(height*place),70,height,"-",0)
        percent_label = create_label(window,300,offset_y+(height*place),50,height,"-",0)
        leaderboard_places.append([rank_label,name_label,score_label,percent_label])
    #Creates the leaderboard based on the number of players each page should have
    
    clear_leaderboard_button = create_button(window,25,325,150,20,"Clear Leaderboard",on_clear_button_pressed)
    clear_leaderboard_button.config(bg = COLOUR_RED)
    
    prev_page_button = create_button(window,200,325,20,20,"<",lambda:on_page_change(-1))
    page_label = create_label(window,225,325,40,20,"1/1",40)
    next_page_button = create_button(window,270,325,20,20,">",lambda:on_page_change(1))
    #Page navigation buttons
    
    window.mainloop()
    
main()