from scraping import Scraping
from modelo_01 import Model_01
from do_docx import Do_docx
from tkinter import *
from tkinter import ttk

def Criar():
    Scraping()
    Model_01()
    Do_docx()
    root.destroy()


root = Tk()
root.title('Ebw Invest')
root.geometry('250x150')
frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="Criador Automático de\nCarteiras de Investimento", padding=25).grid(column=0, row=0)
ttk.Button(frm, text="Criar", command=Criar).grid(column=0, row=1)
root.mainloop()