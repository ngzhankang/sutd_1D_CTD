# importing libs
import tkinter as tk
from tkinter import ttk

# import helper classes
from helpers._Cards import Cards
from helpers._LoadData import LoadData

# make root a global var since we need the window to appear!
global root
root = tk.Tk()

# grouper class
# https://stackoverflow.com/a/17470842/12347869
class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = root
        self.root.title("GPA Calculator")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # setting the position where the window will init first
        # https://www.geeksforgeeks.org/how-to-center-a-window-on-the-screen-in-tkinter/
        self.screen_width, self.screen_height = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.x, self.y = (self.screen_width - self.root.winfo_reqwidth()) // 2, (self.screen_height - self.root.winfo_reqheight()) // 2
        self.root.geometry(f"+{self.x}+{self.y}")
        
        # define other stuff if you have here...


if __name__ == '__main__':
    # call the grouper class
    # https://stackoverflow.com/a/75706167/12347869
    MainApplication(root).grid(column=0, row=0, sticky=('NESW'))

    # run the main application over here
    root.mainloop() #event function to run the entire programme in IDLE