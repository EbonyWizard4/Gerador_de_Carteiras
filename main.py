import customtkinter as ctk

from tkinter import *
from tkinter import filedialog

from scraping import Scraping
from modelo_01 import Model_01
from do_pdf.do_pdf import Do_pdf


"""Executa os modulos do programa"""


def Criar():
    """Coletar dados da internet"""
    # Scraping()

    """Criar carteira através do modelo"""
    # Model_01()

    """Salva o relatório em diretório especificado"""
    destino = Seletor()
    Do_pdf(destino)
    root.destroy()


"""Criar Janela Principal"""
root = ctk.CTk()
root._set_appearance_mode("dark-blue")
root.title("Ebw Invest")
root.geometry("400x200")
root.resizable(width=False, height=False)

"""Criando seletor"""


def Seletor():
    destino = ctk.filedialog.askdirectory(title="Escolha onde salvar o relatório")
    return destino


"""Criar Frame para exibir elementos Titulo da Tela"""
frame = ctk.CTkFrame(master=root, width=390, height=190).place(x=5, y=5)

text = ctk.CTkLabel(
    frame, text="Criador Automático de\nCarteiras de Investimento", font=("arial", 20)
)
text.pack(pady=25)

btn = ctk.CTkButton(frame, text="Gerar", font=("arial", 20), command=Criar).pack(
    pady=10
)
# ttk.Button(frm, text="Criar", command=Criar).grid(column=0, row=1)
root.mainloop()
