import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.geometry('340x440')
window.title("Hello World")
window.config(bg="#333333")

def login_func():
    username = "Mohamed"
    password = "12345"
    if username_entry.get()== username and password_entry.get()== password:
        messagebox.showinfo(title="Login success",message="You have logged in successfully")
    else:
        messagebox.showerror(title="Login Failed",message="Wrong username or password")

# Creating the widgets
frame = tk.Frame(window,bg="#333333")
login_label = tk.Label(frame, text="Login", bg="#333333",fg="#ffffff",font=("Arial",30))
username_label = tk.Label(frame, text="Username",bg="#333333",fg="#ffffff",font=("Arial",16))
username_entry = tk.Entry(frame,font=("Arial",16))
password_label = tk.Label(frame, text="Password",bg="#333333",fg="#ffffff",font=("Arial",16))
password_entry = tk.Entry(frame, show="*",font=("Arial",16))
login_button = tk.Button(frame, text="Login",bg="#393030",fg="#ffffff",font=("Arial",16), command=login_func)

# Placing widgets on the screen
login_label.grid(row=0,column=0,columnspan=2,sticky="news", pady=40)
username_label.grid(row=1,column=0)
username_entry.grid(row=1,column=1, pady=20)
password_label.grid(row=2,column=0)
password_entry.grid(row=2,column=1, pady=20)
login_button.grid(row=3,column=0,columnspan=2,pady=30)
frame.pack()

window.mainloop()
