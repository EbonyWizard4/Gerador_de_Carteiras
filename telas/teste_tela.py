"""Teste de Tela
"""


import tkinter.filedialog as tkfd
from tkinter import PhotoImage, Entry, END
import pandas as pd
from customtkinter import CTk, CTkLabel, CTkButton, CTkTabview


class Tela(CTk):
    """Classe para criar Tela

    Args:
        ctk (lib): Usado para criar tela
    """

    def criar(self):
        """Executa o programa em ordem"""
        destino = self.seletor()
        # Do_pdf(destino)
        # root.destroy()
        print(destino)

    def seletor(self):
        """
        Define diretório de saída
        Returns:
            str: caminho para diretório de saída
        """
        destino = tkfd.askdirectory(title="Escolha onde salvar o relatório")
        return destino

    def root_gen(self, mode: str, title: str):
        """Definições da Tela

        Args:
            mode (str): Dark ou Light
            title (tsr): Titulo da Tela
        """

        self._set_appearance_mode(mode)
        self.geometry("900x600")
        self.resizable(False, False)
        self.title(title)
        bg_image = PhotoImage(file="img/fg_2.png")
        lable1 = CTkLabel(self, image=bg_image, text="")
        lable1.place(x=0, y=0)
        button = CTkButton(
            self,
            width=181,
            height=49,
            corner_radius=50,
            bg_color="#7F859E",
            text="Salvar",
            font=("arial", 20),
            command=self.criar,
        )
        button.place(x=42, y=517)

        self.tab_gen()

    def tab_gen(self):
        """Gera Tabela"""
        # lista de tabelas para criar
        list_tabs = {
            "Magic Form": "CSV/magicForm.csv",
            "Modelo 01": "CSV/modelo_01.csv",
        }

        # criação do tabview
        tab_view = CTkTabview(
            self,
            width=580,
            height=430,
        )
        tab_view.place(x=290, y=130)

        # inserção dos tabs pelos valores da lista
        for tab_item, caminho in list_tabs.items():
            tab_view.add(tab_item)
            tab_view.tab(tab_item).grid_columnconfigure(0, weight=1)

            table_data = pd.read_csv(caminho)
            table_data = table_data.applymap(str)
            columns = [list(table_data)]
            rows = table_data.values.tolist()
            data = columns + rows

            for row_indice in range(len(rows)):
                for col_indice in range(2):
                    entry_item = Entry(
                        tab_view.tab(tab_item),
                        width=22,
                        fg="blue",
                        font=("Arial", 16, "bold"),
                        justify="center",
                    )

                    entry_item.grid(row=row_indice, column=col_indice, padx=10)
                    entry_item.insert(END, data[row_indice][col_indice])


# if __name__=="__main__":
#     root = Tela()
#     root.root_gen("dark","Stock Portfolio")
#     root.mainloop()
