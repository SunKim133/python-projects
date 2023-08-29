from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_WORD = ("Arial", 60, "bold")
FONT_LANG = ("Arial", 40, "italic")
current_word = {}

try:
    word_data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    word_data = pd.read_csv('data/french_words.csv')
finally:
    data = word_data.to_dict(orient='records')

#----------------------------MARK THE WORD AS MEMORIZED----------------------------#
def is_memorized():
    global current_word
    data.remove(current_word)
    dataframe = pd.DataFrame(data)
    dataframe.to_csv('data/words_to_learn.csv', index=False)

    next_word()
#----------------------------SHOW NEXT WORD----------------------------#
def next_word():
    global current_word, flip_timer
    current_word = random.choice(data)
    canvas.itemconfig(card_img, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill='black')
    canvas.itemconfig(card_word, text=current_word['French'], fill='black')

    flip_timer = window.after(3000, flip_card)

#----------------------------FLIP THE CARD----------------------------#
def flip_card():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_word['English'], fill='white')
    canvas.itemconfig(card_img, image=card_back_img)

#----------------------------UI SETUP----------------------------#
window = Tk()
window.title('Flash Card')
window.config(padx=50, pady=50, bg = BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

# Card Image
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file='images/card_back.png')
card_img = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=FONT_LANG)
card_word = canvas.create_text(400, 263, text="", font=FONT_WORD)
canvas.grid(column=0, row=0, columnspan=2)

# Button Border
btn_border = Frame(window, highlightbackground=BACKGROUND_COLOR, highlightthickness=0, bd=0)

# Wrong Button
wrong_image = PhotoImage(file='images/wrong.png')
wrong_btn = Button(image=wrong_image, highlightbackground=BACKGROUND_COLOR, highlightthickness=0, command=next_word)
wrong_btn.grid(column=0, row=1)

# Check Button
check_image = PhotoImage(file='images/right.png')
check_btn = Button(image=check_image, highlightbackground=BACKGROUND_COLOR, highlightthickness=0, command=is_memorized)
check_btn.grid(column=1, row=1)

next_word()


window.mainloop()