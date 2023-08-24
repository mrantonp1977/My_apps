import customtkinter
import subprocess


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")
root.title("Login Window")



def login():
    username = entry1.get()
    password = entry2.get()

    # Check if the username and password are correct
    if username == "mrantonp" and password == "1977":
        root.destroy()  # Close the login window
        open_second_window()
    else:
        error_label.configure(text="Invalid username or password !!")

def open_second_window():
    subprocess.Popen("Antonis Passwords Database.exe")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login System", font=("arial", 24))
label.pack(pady=18, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)



error_label = customtkinter.CTkLabel(master=frame, text="")
error_label.pack()


root.mainloop()