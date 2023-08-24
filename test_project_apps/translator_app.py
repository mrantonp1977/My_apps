from tkinter import *
import googletrans
import textblob
from tkinter import ttk, messagebox


root = Tk()
root.title("Translator")
root.geometry("400x600")
root.config(background="orange")


def translate_it():
    translated_text.delete(1.0, END)
    try:
        for key, value in languages.items():
            if (value == original_combo.get()):
                from_language_key = key


        for key, value in languages.items():
            if (value == translated_combo.get()):
                to_language_key = key

        words = textblob.TextBlob(original_text.get(1.0, END))

        words = words.translate(from_lang=from_language_key, to=to_language_key)
        translated_text.insert(1.0, words)

    except Exception as e:
        messagebox.showerror("Translator", e)




def clear():
    original_text.delete(1.0, END)
    translated_text.delete(1.0, END)

languages = googletrans.LANGUAGES

language_list = list(languages.values())

original_text = Text(root, height=5, width=30, font=("arial", 14))
original_text.grid(row=0, column=0, pady=20, padx=20)

translate_button = Button(root, text="Translate!", font=("arial black", 14), width=10, background="black", foreground="orange",  command=translate_it)
translate_button.grid(row=2, column=0, padx=20, pady=30)


translated_text = Text(root, height=5, width=30, font=("arial", 14))
translated_text.grid(row=3, column=0, pady=20, padx=10)

original_combo = ttk.Combobox(root, width=30, value=language_list, font=("arial black", 9))
original_combo.current(21)
original_combo.grid(row=1, column=0)

translated_combo = ttk.Combobox(root, width=30, value=language_list, font=("arial black", 9))
translated_combo.current(26)
translated_combo.grid(row=4, column=0)

clear_button = Button(root, text="Clear", font=("Helvetica", 14), width=10, background="black", foreground="orange", command=clear)
clear_button.grid(row=5, column=0, pady=20)




root.mainloop()