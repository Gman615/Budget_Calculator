import os, sys, time
from tkinter import *
import tkinter as tk
from tkinter import messagebox


import budget_calc_func
import budget_calc_gui


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)


        self.master = master
        self.master.minsize(375,325)
        self.master.maxsize(375,325)
        self.master.title("Budget Calculator")
        self.master.configure(bg="#18453B")
        self.master.protocol("WM_DELETE_WINDOW", lambda: budget_calc_func.ask_quit(self))
        arg = self.master

        budget_calc_gui.load_gui(self)




if __name__ =="__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

        
