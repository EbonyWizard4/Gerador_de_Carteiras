"""Módulo Principal"""

import customtkinter as ctk

from scraping import Scraping
from modelos import Model_01
from do_pdf.do_pdf import Do_pdf


# """Executa os modulos do programa"""


def criar():
    """Executa o Programa em ordem"""
    # """Coletar dados da internet"""
    Scraping()

    # """Criar carteira através do modelo"""
    Model_01()

    # """Salva o relatório em diretório especificado"""
    destino = seletor()
    Do_pdf(destino)
    root.destroy()


# """Criar Janela Principal"""
root = ctk.CTk()
root._set_appearance_mode("dark-blue")
root.title("Ebw Invest")
root.geometry("400x200")
root.resizable(width=False, height=False)

# """Criando seletor"""


def seletor():
    """Escolhe diretório de saída"""
    destino = ctk.filedialog.askdirectory(title="Escolha onde salvar o relatório")
    return destino


# """Criar Frame para exibir elementos Titulo da Tela"""
FRAME = ctk.CTkFrame(master=root, width=390, height=190).place(x=5, y=5)

TEXT = ctk.CTkLabel(
    FRAME, text="Criador Automático de\nCarteiras de Investimento", font=("arial", 20)
)
TEXT.pack(pady=25)

BTN = ctk.CTkButton(FRAME, text="Gerar", font=("arial", 20), command=criar).pack(
    pady=10
)
# ttk.Button(frm, text="Criar", command=Criar).grid(column=0, row=1)
if __name__=="__main__":
    root.mainloop()
