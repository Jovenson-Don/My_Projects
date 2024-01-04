from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
else:
    data_dict = data.to_dict(orient="records")


# ---------------------------- SAVE CARD------------------------------- #
def remove():
    data_dict.remove(current_card)
    words_to_learn = pandas.DataFrame(data_dict)
    words_to_learn.to_csv("data/words_to_learn.csv", index=False)
    new_flash_card()


# ---------------------------- FLIP CARD------------------------------- #
def flip_card():
    global current_card
    card_canvas.itemconfig(card_image, image=back_card)
    card_canvas.itemconfig(card_title, text="English", fill="white")
    card_canvas.itemconfig(card_word, text=current_card["English"], fill="white")


# ---------------------------- CREATE NEW FLASH CARDS------------------------------- #
def new_flash_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    card_canvas.itemconfig(card_image, image=front_card)
    card_canvas.itemconfig(card_title, text="French", fill="black")
    card_canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, flip_card)


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

# Canvas
front_card = PhotoImage(file="./images/card_front.png")
card_canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_image = card_canvas.create_image(400, 263, image=front_card)
card_title = card_canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = card_canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
card_canvas.grid(row=0, column=0, columnspan=2)
back_card = PhotoImage(file="./images/card_back.png")

# Button
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, background=BACKGROUND_COLOR, command=new_flash_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, background=BACKGROUND_COLOR, command=remove)
right_button.grid(row=1, column=1)

new_flash_card()

window.mainloop()
