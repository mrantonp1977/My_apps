from tkinter import *
from time import *

window = Tk()
window.geometry("800x300")
window.configure(bg="#D3EED2")


def update():
    time_string = strftime("%H:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000,update)

time_label = Label(window,font=("Arial",70),fg="#00FF00",bg="black")
time_label.pack()

day_label = Label(window,font=("impact",50,"bold"),fg="#A309DA",bg="#D3EED2")
day_label.pack()

date_label = Label(window,font=("impact",50),fg="#A309DA",bg="#D3EED2")
date_label.pack()


update()

window.mainloop()