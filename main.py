"""Módulo Principal"""

import customtkinter as ctk

from scraping import Scraping
from modelos import Model_01
from do_pdf.do_pdf import Do_pdf

def criar():
    """Executa o programa em ordem
    """
    Scraping()
    Model_01()
    destino = seletor()
    Do_pdf(destino)
    root.destroy()

class Root(ctk.CTk):
    """Criador da Tela

    Args:
        ctk (Lib): Usado para criar Telas
    """

    def root_gen(self, mode):
        """Configurações da janela"""
        self._set_appearance_mode(mode)
        self.geometry("400x200")
        self.resizable(width=False, height=False)
        frame = ctk.CTkFrame(master=root, width=390, height=190).place(x=5, y=5)
        ctk.CTkLabel(
            frame, text="Criador Automático de\nCarteiras de Investimento", font=("arial", 20)
        ).pack(pady=25)
        ctk.CTkButton(frame, text="Gerar", font=("arial", 20), command=criar).pack(pady=10)

def seletor():
    """
    Define diretório de saída
    Returns:
        str: caminho para diretório de saída
    """
    destino = ctk.filedialog.askdirectory(title="Escolha onde salvar o relatório")
    return destino

if __name__ == "__main__":
    root = Root()
    root.title("Ebw Invest")
    root.root_gen("dark")
    root.mainloop()
