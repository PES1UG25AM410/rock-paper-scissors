import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox
import random


user_score = 0
computer_score = 0
rounds_played = 0
total_rounds = 0
options = ['ROCK', 'PAPER', 'SCISSORS']



def start_game():
    
    global total_rounds, rounds_played, user_score, computer_score
    try:
        rounds = int(rounds_entry.get())
        if rounds <= 0:
            messagebox.showerror("Invalid Input", "Number of rounds must be greater than zero.")
            return
        
        total_rounds = rounds
        user_score = 0
        computer_score = 0
        rounds_played = 0
        
        setup_frame.pack_forget()
        game_frame.pack(pady=20, padx=20, fill="both", expand=True)
        update_scoreboard()
        
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the rounds.")

def play_round(user_choice):
    
    global rounds_played, user_score, computer_score

    if rounds_played >= total_rounds:
        return  

    computer_choice = random.choice(options)
    rounds_played += 1
    result_text = ""
    if user_choice == computer_choice:
        result_text = "IT'S A DRAW!"
        result_label.config(fg="#f1c40f")
    elif (user_choice == "ROCK" and computer_choice == "SCISSORS") or \
         (user_choice == "PAPER" and computer_choice == "ROCK") or \
         (user_choice == "SCISSORS" and computer_choice == "PAPER"):
        result_text = "YOU WON THIS ROUND!"
        user_score += 1
        result_label.config(fg="#2ecc71")
    else:
        result_text = "YOU LOST THIS ROUND!"
        computer_score += 1
        result_label.config(fg="#e74c3c")
        
    user_choice_label.config(text=f"Your choice: {user_choice}")
    computer_choice_label.config(text=f"Computer's choice: {computer_choice}")
    result_label.config(text=result_text)
    update_scoreboard()

    if rounds_played == total_rounds:
        end_game()

def update_scoreboard():
    score_label.config(text=f"Score: You {user_score} - {computer_score} Computer")
    round_label.config(text=f"Round: {rounds_played} / {total_rounds}")

def end_game():
    
    if user_score > computer_score:
        final_message = "Congratulations! You won the game!"
    elif computer_score > user_score:
        final_message = "Game Over. The computer won."
    else:
        final_message = "The game ended in a draw!"
        
    messagebox.showinfo("Game Over", final_message)
    play_again_button.pack(pady=20)
    
    
    rock_btn.config(state="disabled")
    paper_btn.config(state="disabled")
    scissors_btn.config(state="disabled")

def reset_game():
    
    user_choice_label.config(text="")
    computer_choice_label.config(text="")
    result_label.config(text="")

    
    play_again_button.pack_forget()
    rock_btn.config(state="normal")
    paper_btn.config(state="normal")
    scissors_btn.config(state="normal")

    
    game_frame.pack_forget()
    setup_frame.pack(pady=50)



root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("800x800")
root.configure(bg="black")


title_font = tkfont.Font(family="Helvetica", size=24, weight="bold")
label_font = tkfont.Font(family="Helvetica", size=14)
button_font = tkfont.Font(family="Helvetica", size=12, weight="bold")
result_font = tkfont.Font(family="Helvetica", size=16, weight="bold")
score_font = tkfont.Font(family="Helvetica", size=14, weight="bold")


setup_frame = tk.Frame(root, bg="black")
game_frame = tk.Frame(root, bg="black")


tk.Label(
    setup_frame,
    text="Welcome to Rock, Paper, Scissors!",
    font=title_font, fg="#ecf0f1", bg="black"
).pack(pady=(0, 20))

tk.Label(
    setup_frame,
    text="Enter the number of rounds you want to play:",
    font=label_font, fg="#ecf0f1", bg="black"
).pack(pady=10)

rounds_entry = tk.Entry(
    setup_frame, font=label_font, width=5, justify='center'
)
rounds_entry.pack(pady=5)
rounds_entry.insert(0, "5")

start_button = tk.Button(
    setup_frame, text="Start Game", font=button_font,
    bg="#2980b9", fg="#ffffff", width=15, command=start_game
)
start_button.pack(pady=20)


tk.Label(
    game_frame, text="Choose your weapon!", font=title_font,
    fg="#ecf0f1", bg="black"
).pack(pady=(0, 20))

score_label = tk.Label(
    game_frame, text="Score: You 0 - 0 Computer", font=score_font,
    fg="#ecf0f1", bg="black"
)
score_label.pack(pady=10)

round_label = tk.Label(
    game_frame, text="Round: 0 / 0", font=label_font,
    fg="#bdc3c7", bg="black"
)
round_label.pack(pady=5)

buttons_frame = tk.Frame(game_frame, bg="black")
buttons_frame.pack(pady=20)

rock_btn = tk.Button(buttons_frame, text="ROCK", font=button_font, bg="#c0392b", fg="white", width=12, height=2, command=lambda: play_round("ROCK"))
paper_btn = tk.Button(buttons_frame, text="PAPER", font=button_font, bg="#27ae60", fg="white", width=12, height=2, command=lambda: play_round("PAPER"))
scissors_btn = tk.Button(buttons_frame, text="SCISSORS", font=button_font, bg="#8e44ad", fg="white", width=12, height=2, command=lambda: play_round("SCISSORS"))

rock_btn.grid(row=0, column=0, padx=10)
paper_btn.grid(row=0, column=1, padx=10)
scissors_btn.grid(row=0, column=2, padx=10)

user_choice_label = tk.Label(game_frame, text="", font=label_font, fg="#ecf0f1", bg="black")
user_choice_label.pack(pady=5)

computer_choice_label = tk.Label(game_frame, text="", font=label_font, fg="#ecf0f1", bg="black")
computer_choice_label.pack(pady=5)

result_label = tk.Label(game_frame, text="", font=result_font, fg="#f1c40f", bg="black")
result_label.pack(pady=20)

play_again_button = tk.Button(
    game_frame, text="Play Again", font=button_font,
    bg="#16a085", fg="#ffffff", width=15, command=reset_game
)


setup_frame.pack(pady=50)
root.mainloop()

