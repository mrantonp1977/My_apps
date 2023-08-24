import random
import tkinter as tk


def generate_numbers():
    history_1 = {}


    for i in range(6):
        numbers_1 = random.sample(range(1, 50), 6)


        for number in numbers_1:
            if number in history_1:
                history_1[number] += 1
            else:
                history_1[number] = 1



        textbox_numbers[i].delete("1.0", tk.END)
        textbox_numbers[i].insert(tk.END, ", ".join(map(str, numbers_1)))




        textbox_history.delete("1.0", tk.END)
        textbox_history.insert(tk.END, f"{history_1}\n"

                                   f"" f"")


# Create the main window
window = tk.Tk()
window.title("Random Number Generator")
window.geometry("800x800")
window.configure(bg="#EEE9D1")

# Create a label for the title
title_label = tk.Label(window, text="Lotto Random Number Generator", font=("Arial black", 20),borderwidth=20,relief="ridge", bg="blue", fg="yellow")
title_label.pack(pady=25)

# Create a button to generate numbers
generate_button = tk.Button(window, text="Υπολογισμός Τυχαίων Αριθμών\nClick Here !!!", font=("Arial black", 14),bd=10, bg="yellow",
                            fg="#DE15F0", command=generate_numbers)
generate_button.pack(pady=25)

# Create text boxes for displaying numbers
textbox_numbers = []
for i in range(6):
    frame = tk.Frame(window, bg="#7FCBC4")
    frame.pack(pady=5)

    label_numbers = tk.Label(frame, text="Οι 6 τυχαίοι αριθμοί είναι:", font=("Arial black", 12), bg="#7FCBC4",
                             fg="blue")
    label_numbers.pack(side=tk.LEFT)

    textbox_numbers.append(tk.Text(frame, height=1, width=22, font=("Arial black", 12), bg="#FFFFFF", fg="#DF10B4"))
    textbox_numbers[i].pack(side=tk.LEFT)





# Create a text box for displaying history
label_history = tk.Label(window, text="    Ιστορικό Εμφανήσεων    ", font=("Arial black", 14),borderwidth=10, relief="ridge", bg="yellow", fg="#DE15F0")
label_history.pack(pady=10)

textbox_history = tk.Text(window, height=7, width=40, font=("Arial black", 12), bg="#FFFFFF", fg="green")
textbox_history.pack()

# Start the main loop
window.mainloop()