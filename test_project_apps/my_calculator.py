from tkinter import *
import math

def button_press(num):

    global equation_text

    equation_text = equation_text + str(num)

    equation_label.set(equation_text)

def equals():

    global equation_text

    try:

        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text = total

    except SyntaxError:

        equation_label.set("syntax error")

        equation_text = ""

    except ZeroDivisionError:

        equation_label.set("arithmetic error")

        equation_text = ""

def clear():

    global equation_text

    equation_label.set("")

    equation_text = ""

def backspace():
    global equation_text
    equation_text = equation_text[:-1]  # Remove the last character
    equation_label.set(equation_text)

def modulo():
    global equation_text
    equation_text = equation_text + '%'
    equation_label.set(equation_text)

def square_root():
    global equation_text
    try:
        result = math.sqrt(float(equation_text))
        equation_text = str(result)
        equation_label.set(equation_text)
    except ValueError:
        equation_label.set("Invalid input")
        equation_text = ""


window = Tk()
window.title("Calculator program")
window.geometry("600x750")
window.configure(background="#9650C6")




equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('arial',30), bg="black",fg="#11D106", width=35, height=3)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, height=5, width=13, font=35,fg="white",bg="black",borderwidth=8,relief="ridge",
                 command=lambda: button_press(1))
button1.grid(row=1, column=0)

button2 = Button(frame, text=2, height=5, width=13, font=35,fg="white",bg="black",borderwidth=8,relief="ridge",
                 command=lambda: button_press(2))
button2.grid(row=1, column=1)

button3 = Button(frame, text=3, height=5, width=13, font=35,fg="white",bg="black",borderwidth=8,relief="ridge",
                 command=lambda: button_press(3))
button3.grid(row=1, column=2)

button4 = Button(frame, text=4, height=5, width=13, font=35,fg="white",bg="black",borderwidth=8,relief="ridge",
                 command=lambda: button_press(4))
button4.grid(row=2, column=0)

button5 = Button(frame, text=5, height=5, width=13, font=35,fg="white",bg="black",borderwidth=8,relief="ridge",
                 command=lambda: button_press(5))
button5.grid(row=2, column=1)

button6 = Button(frame, text=6, height=5, width=13, font=35,fg="white",bg="black",borderwidth=8,relief="ridge",
                 command=lambda: button_press(6))
button6.grid(row=2, column=2)

button7 = Button(frame, text=7, height=5, width=13, font=35,fg="white",bg="black",borderwidth=8,relief="ridge",
                 command=lambda: button_press(7))
button7.grid(row=3, column=0)

button8 = Button(frame, text=8, height=5, width=13, font=35,fg="white",bg="black",borderwidth=8,relief="ridge",
                 command=lambda: button_press(8))
button8.grid(row=3, column=1)

button9 = Button(frame, text=9, height=5, width=13, font=35,fg="white",bg="black",borderwidth=8,relief="ridge",
                 command=lambda: button_press(9))
button9.grid(row=3, column=2)

button0 = Button(frame, text=0, height=5, width=13, font=35,fg="white",bg="black",borderwidth=8,relief="ridge",
                 command=lambda: button_press(0))
button0.grid(row=4, column=1)

plus = Button(frame, text='+', height=4, width=11, font=("arial black",11),fg="black",bg="orange",borderwidth=8,relief="ridge",
                 command=lambda: button_press('+'))
plus.grid(row=0, column=3)

minus = Button(frame, text='-', height=4, width=11, font=("arial black",11),fg="black",bg="orange",borderwidth=8,relief="ridge",
                 command=lambda: button_press('-'))
minus.grid(row=1, column=3)

multiply = Button(frame, text='*', height=4, width=11, font=("arial black",11),fg="black",bg="orange",borderwidth=8,relief="ridge",
                 command=lambda: button_press('*'))
multiply.grid(row=2, column=3)

divide = Button(frame, text='/', height=4, width=11, font=("arial black",11),fg="black",bg="orange",borderwidth=8,relief="ridge",
                 command=lambda: button_press('/'))
divide.grid(row=3, column=3)

equal = Button(frame, text='=', height=4, width=11, font=("arial black",11),fg="black",bg="blue",borderwidth=8,relief="ridge",
                 command=equals)
equal.grid(row=4, column=3)

decimal = Button(frame, text='.', height=4, width=11, font=("arial black",11),fg="black",bg="orange",borderwidth=8,relief="ridge",
                 command=lambda: button_press('.'))
decimal.grid(row=4, column=2)


clear = Button(frame, text='clear', height=4, width=11, font=("arial black",11),fg="black",bg="green",borderwidth=8,relief="ridge",
                 command=clear)
clear.grid(row=4, column=0)


backspace = Button(frame, text='backspace', height=4, width=11,font=("arial black",11),fg="black",bg="green",borderwidth=8,relief="ridge",
                 command=backspace)
backspace.grid(row=0,column=0)


modulo = Button(frame, text='%', height=4, width=11, font=("arial black", 11), fg="black", bg="orange",
                   borderwidth=8, relief="ridge", command=modulo)
modulo.grid(row=0,column=2)

sqrt_button = Button(frame, text='√', height=4, width=11, font=("arial black", 11), fg="black", bg="orange", borderwidth=8, relief="ridge",
                    command=square_root)
sqrt_button.grid(row=0, column=1)




window.mainloop()