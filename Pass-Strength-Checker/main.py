import tkinter as tk
from tkinter import messagebox
import re

def create_main_window():
    window = tk.Tk()
    window.title("Password Strength Checker")
    window.geometry("400x200")
    background_color = "#f0f0f0"
    window.configure(bg=background_color)
    return window


def check_password_strength(password):
     if len(password) < 8:
         return "Password is too short man, what the heck! You know better than that! Come on! It should be at least 16 characters long!"
     if not re.search("[a-z]", password):
         return "Password must contain at least one lowercase letter! You know that right? Come on!"  
     if not re.search("[A-Z]", password):
         return "Password must contain at least one uppercase letter! Show some respect!"
     if not re.search("[0-9]", password):
         return "Password must contain at least one number! You know math right? We're not asking for much!"
     if not re.search("[_@$]", password):
         return "Password must contain at least one special character! At this point you're just... special right?!"
     return "Password is strong! You're good to go! Here's a cookie 🍪! Now move along." 
 

def on_check_button_click(entry):
    password = entry.get()
    result = check_password_strength(password)
    messagebox.showinfo("Password Strength Result", result)

def main():
    window = create_main_window()
    
    label = tk.Label(window, text="Enter a password:")
    label.pack(pady=15)

    password_entry = tk.Entry(window, show='*')
    password_entry.pack(pady=15)

    check_button = tk.Button(window, text="Check Strength", command=lambda: on_check_button_click(password_entry))
    check_button.pack(pady=20 )
    check_button.configure(bg="#008CBA", fg="white", font=("Roboto", 10))
    

    window.mainloop()

 
if __name__ == "__main__":
    main()
