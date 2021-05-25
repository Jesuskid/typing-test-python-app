import random
from tkinter import *
from tkinter import ttk
from random import choice
import csv
import math

Minute = 1
reps = 0
timer = None
sample_texts = ''


root = Tk()
root.geometry('830x500')
root.title('Typing speed test')

def reset_timer():
    global SCORE
    root.after_cancel(timer)
    top_w.config(text="Time remaining: 00:00")
    entry.config(state='disabled')
    label.config(state='normal')
    label.delete('1.0', END)
    label.insert(INSERT, f'Timeout: You typed {SCORE} words in per minute')
    label.config(state='disabled')
    btn.config(text='Try Again')
    SCORE = 0

def start_timer():
    global sample_texts
    sample_texts = [random.choice(words).strip("\n") for i in range(200)]
    label.config(state='normal')
    label.delete('1.0', END)
    label.insert(INSERT, sample_texts)
    label.config(state='disabled')

    entry.config(state='normal')
    work_sec = Minute * 60
    count_down(work_sec)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    top_w.config(text=f"Time remaining: {count_min}:{count_sec}")
    print(f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = root.after(1000, count_down, count - 1)
    else:
        reset_timer()



SCORE = 0
with open('1-1000.txt',) as file:
    words = file.readlines()





top_l = Label(root, text=f'Words typed: 0 ', font=('Arial', 14),)
top_l.grid(row=0, column=0)

top_w = Label(root, text='', font=('Arial', 14),)
top_w.grid(row=3, column=0)

btn = ttk.Button(root, text='Start', command=start_timer)
btn.grid(row=1, column=0)


label = Text(root, height=10, width=70, font=('Arial', 14), spacing2=2)
label.insert(INSERT, 'Welcome to the typing test, click the start button to begin!')
label.config(state='disabled')
label.grid(row=2, column=0, pady=20, padx=20)


entry = Entry(root, width=60, font=('Arial', 16), state='disabled')
entry.grid(row=4, column=0, pady=100)

def check_word(event):
    global SCORE
    global sample_texts
    data = sample_texts
    word = entry.get()
    new_word = word.strip(" ")
    if new_word  in data:
        SCORE += 1
        data.remove(new_word)
        top_l.config(text=f'Words typed: {SCORE}')
        label.config(state='normal')
        label.delete('1.0', END)
        label.insert(INSERT, data)
        label.config(state='disabled')
    entry.delete(0, END)




if __name__ == '__main__':
    root.bind('<space>',  check_word)
    root.mainloop()
