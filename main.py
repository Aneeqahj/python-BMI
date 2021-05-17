# BMI Calculator
from tkinter import *
import tkinter as tk

from future.moves.tkinter import messagebox

window = tk.Tk()
window.geometry("600x600")
window.title("BMI Calculator")
window.config(bg="white")
window.resizable("false", "false")

# Labels
label_weight = tk.Label(window, text="Weight(kg):", bg="lightblue")
label_weight.place(x=60, y=20, height=50, width=120)
label_height = tk.Label(window, text="Height(cm):", bg="lightblue")
label_height.place(x=60, y=80, height=50, width=120)
label_gender = tk.Label(window, text="Gender:", bg="lightblue")
label_gender.place(x=60, y=140, height=50, width=120)
label_age = tk.Label(window, text="Age:", bg="lightblue")
label_age.place(x=60, y=200, height=50, width=120)
label_bmi = tk.Label(window, text="BMI:", bg="lightblue")
label_bmi.place(x=60, y=400, height=50, width=120)
label_ideal_bmi = tk.Label(window, text="Ideal BMI:", bg="lightblue")
label_ideal_bmi.place(x=350, y=400, height=50, width=120)

# Entries
weight = tk.Entry(window)
weight.place(x=250, y=20, height=50, width=120)
height = tk.Entry(window)
height.place(x=250, y=80, height=50, width=120)
age = tk.Entry(window, state="readonly")
age.place(x=250, y=200, height=50, width=120)
bmi = tk.Entry(window, state="readonly")
bmi.place(x=200, y=400, height=50, width=100)

# Gender Entry
options = ['Select...', 'Male', "Female"]
variable = StringVar(window)
variable.set(options[0])


def activate(value):
    variable.set(value)
    if value != "Select...":
        age.config(state='normal')
    else:
        age.config(state='readonly')


def clear():
    weight.delete(0, END)
    height.delete(0, END)



gender_menu = OptionMenu(window, variable, *options, command=activate)
gender_menu.place(x=250, y=140, height=50, width=120)

delete = Button(window, text="Clear", command=clear)
delete.place(x=450, y=550)


mainloop()
