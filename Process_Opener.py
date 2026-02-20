import tkinter as tk
from tkinter import messagebox
import subprocess
import webbrowser
import time
import random
import winsound
import pyautogui
def gpu_glitch(flashes=10):
    glitch = tk.Toplevel()
    glitch.attributes("-topmost", True)
    glitch.attributes("-fullscreen", True)

    colors = ["red", "black", "green", "blue", "white", "cyan"]
    try:
        for _ in range(flashes):
            if not glitch.winfo_exists():
                break
            glitch.config(bg=random.choice(colors))
            glitch.update()
            time.sleep(0.05)
        glitch.destroy()
    except tk.TclError:
        pass
root = tk.Tk()
root.withdraw()
period = random.randrange(1, 6)
with open("message.txt", "w") as f:
    f.write("Hello! How are you doing today?" + "\n")
    f.write("I am stalking you. Can I prove it?" + "\n")
    f.write("You are on a Windows Operating System." + "\n")
    f.write("You are doing schoolwork but you're bored." + "\n")
    f.write("I see you.... \n")
messagebox.showwarning("Unstable System Alert", "Your PC is doing weird stuff. You may be infected with malware. Who knows?")
time.sleep(period)
subprocess.Popen(["notepad.exe",
                  "message.txt"])
time.sleep(period)
webbrowser.open("https://www.google.com/search?q=pls+help+my+pc+is+doing+weird+stuff")
time.sleep(period)
webbrowser.open("https://rickroll.it/rickroll.mp4")
time.sleep(period)
winsound.Beep(670, 1000)
time.sleep(round(period / 2))
winsound.Beep(770, 1000)
time.sleep(round(period / 2))
winsound.Beep(870, 1000)
time.sleep(round(period / 2))
winsound.Beep(970, 1000)
time.sleep(round(period / 2))
winsound.Beep(1000, 1000)
time.sleep(round(period / 2))
winsound.Beep(2000, 4000)
time.sleep(period)
gpu_glitch(15)
time.sleep(3)
webbrowser.open("https://www.google.com/search?q=job+application")
time.sleep(3)
messagebox.askyesno("Job?", "Want to get a job?")
subprocess.Popen(["notepad.exe"])
time.sleep(3)
pyautogui.hotkey('alt', 'tab')
time.sleep(period)
pyautogui.typewrite("Congrats! You survived the payload, but remember:\n I'm watching.", interval=0.15)
print("Goodbye!")
