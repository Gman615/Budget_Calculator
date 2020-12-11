import os, sys, time
from tkinter import *
import tkinter as tk
from tkinter import messagebox


import budget_calc
import budget_calc_gui


def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        self.master.destroy()
        os._exit(0)

def monthly_income(self):
    income = self.txt_income.get()
    income = float(income)
    if type(income) is str:
        return messagebox.showerror("Ooooops", "Numbers only please")    
    housing = self.txt_housing.get()
    housing = float(housing)
    if type(income) is str:
        return messagebox.showerror("Ooooops", "Numbers only please")
    loan = self.txt_loan.get()
    loan = float(loan)
    if type(income) is str:
        return messagebox.showerror("Ooooops", "Numbers only please")
    credit = self.txt_credit.get()
    credit = float(loan)
    if type(income) is str:
        return messagebox.showerror("Ooooops", "Numbers only please")
    bills = self.txt_bills.get()
    bills = float(bills)
    if type(income) is str:
        return messagebox.showerror("Ooooops", "Numbers only please")
    remainder = income-housing-loan-credit-bills
    self.txt_remain.insert(END, remainder)
    
    
    




    
if __name__ == "__main__":
    pass
