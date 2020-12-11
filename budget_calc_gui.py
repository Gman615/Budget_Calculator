import os, sys, time
from tkinter import *
import tkinter as tk
from tkinter import messagebox

import budget_calc
import budget_calc_func

def load_gui(self):

    self.lbl_income = tk.Label(self.master,text='Monthly Income:',bg='#18453B',fg='white')
    self.lbl_income.grid(row=0,column=0,padx=(27,0),pady=(20,0),sticky=N+W)
    self.lbl_housing = tk.Label(self.master,text='Housing Cost:',bg='#18453B',fg='white')
    self.lbl_housing.grid(row=1,column=0,padx=(27,0),pady=(20,0),sticky=N+W)
    self.lbl_loan = tk.Label(self.master,text='Total Loans:',bg='#18453B',fg='white')
    self.lbl_loan.grid(row=2,column=0,padx=(27,0),pady=(20,0),sticky=N+W)
    self.lbl_credit = tk.Label(self.master,text='Credit Cards:',bg='#18453B',fg='white')
    self.lbl_credit.grid(row=3,column=0,padx=(27,0),pady=(20,0),sticky=N+W)
    self.lbl_bills = tk.Label(self.master,text='Other Bills:',bg='#18453B',fg='white')
    self.lbl_bills.grid(row=4,column=0,padx=(27,0),pady=(20,0),sticky=N+W)
    self.lbl_remain = tk.Label(self.master,text='Remaining Amount:',bg='#18453B',fg='white')
    self.lbl_remain.grid(row=5,column=0,padx=(27,0),pady=(20,0),sticky=N+W)

    self.btn_remain = tk.Button(self.master,text='Get Budget',bg='gold',fg='black',command=lambda: budget_calc_func.monthly_income(self))
    self.btn_remain.grid(row=6,column=0,padx=(27,0),pady=(20,0),sticky=N+W)

    self.txt_income = tk.Entry(self.master,text='')
    self.txt_income.grid(row=0,column=1,padx=(27,0),pady=(20,0),sticky=N+W)
    self.txt_housing = tk.Entry(self.master,text='')
    self.txt_housing.grid(row=1,column=1,padx=(27,0),pady=(20,0),sticky=N+W)
    self.txt_loan = tk.Entry(self.master,text='')
    self.txt_loan.grid(row=2,column=1,padx=(27,0),pady=(20,0),sticky=N+W)
    self.txt_credit = tk.Entry(self.master,text='')
    self.txt_credit.grid(row=3,column=1,padx=(27,0),pady=(20,0),sticky=N+W)
    self.txt_bills = tk.Entry(self.master,text='')
    self.txt_bills.grid(row=4,column=1,padx=(27,0),pady=(20,0),sticky=N+W)
    self.txt_remain = tk.Entry(self.master,text='')
    self.txt_remain.grid(row=5,column=1,padx=(27,0),pady=(20,0),sticky=N+W)













if __name__ == "__main__":
    pass
