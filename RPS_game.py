from tkinter import *
import random

#variables and dictionary
player_score = 0
computer_score = 0
possible_outcomes = {
    "rock":{"rock":1, "paper":0, "scissors":2},
    "paper":{"rock":2, "paper":1, "scissors":0},
    "scissors":{"rock":0, "paper":2, "scissors":1}
}
#Functions
def outcome_handler(user_choice):
    global computer_score,player_score
    outcomes = ["rock","paper","scissors"]
    ran_num = random.randint(0,2)
    computer_choice = outcomes[ran_num]
    result = possible_outcomes[user_choice][computer_choice]
    
    player_choice_label.config(fg="pink", text=f"Player choice : {user_choice}")
    computer_choice_label.config(fg="pink", text=f"Computer choice : {computer_choice}")
    #if_conditions
    if result == 2:
        player_score += 1
        player_score_label.config(text=f"Player : {player_score}")
        computer_score_label.config(text=f"Computer : {computer_score}")
        outcome_label.config(fg="gold", text="Player won",font=("Calibri",14))
    elif result == 1:
        player_score_label.config(text=f"Player : {player_score}")
        computer_score_label.config(text=f"Computer : {computer_score}")
        outcome_label.config(fg="silver", text="Draw",font=("Calibri",14))
    elif result == 0:
        computer_score += 1
        player_score_label.config(text=f"Player : {player_score}")
        computer_score_label.config(text=f"Computer : {computer_score}")
        outcome_label.config(fg="red", text="Computer won",font=("Calibri",14))

#Main_screen
x = Tk()
x.title("RPS game")

#Labels
Label(x,text="Rock, Paper, Scissors",font=("Calibri",14)).grid(row=0,sticky=N,pady=10,padx=200)
Label(x,text="Please select an option",font=("Calibri",12)).grid(row=1,sticky=N)
player_score_label = Label(x,text="Player : 0",font=("Calibri",12))
computer_score_label = Label(x,text="Computer : 0",font=("Calibri",12))
player_choice_label = Label(x,font=("Calibri",12))
computer_choice_label = Label(x,font=("Calibri",12))
outcome_label = Label(x,font=("Calibri",12))

player_score_label.grid(row=2,sticky=W)
computer_score_label.grid(row=2,sticky=E)
player_choice_label.grid(row=3,sticky=W)
computer_choice_label.grid(row=3,sticky=E)
outcome_label.grid(row=3,sticky=N)
Label(x).grid(row=5)

#Buttons
Button(x, text="Rock", width=15,command=lambda:outcome_handler("rock")).grid(row=4,sticky=W,pady=5,padx=5)
Button(x, text="Paper", width=15,command=lambda:outcome_handler("paper")).grid(row=4,sticky=N,pady=5,padx=5)
Button(x, text="Scissors", width=15,command=lambda:outcome_handler("scissors")).grid(row=4,sticky=E,pady=5,padx=5)
x.mainloop()