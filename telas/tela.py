"""
Teste de Tela
"""

import tkinter.filedialog as tkfd
from tkinter import PhotoImage, END
import pandas as pd
from customtkinter import CTk, CTkLabel, CTkButton, CTkTabview, CTkFrame, CTkEntry
from docx import Document
from do_pdf import do_pdf

class Tela(CTk):
    """
    Classe para criar Tela
    Args:
        ctk (lib): Usado para criar tela
    """

    def root_gen(self, mode: str, title: str):
        """
        Definições da Tela
        Args:
            mode (str): Dark ou Light
            title (tsr): Titulo da Tela
        """

        # - Propriedades da tela
        self._set_appearance_mode(mode)
        self.geometry("900x650")
        self.resizable(False, False)
        self.title(title)

        # - Elementos da tela
        bg_image = PhotoImage(file="img/fg_900x650.png")
        beck_grownd = CTkLabel(self, image=bg_image, text="")
        beck_grownd.place(x=0, y=0)
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
        button.place(x=42, y=585)

        self.tab_gen()

    def tab_gen(self):
        """
        Gera Tabela na tela
        """
        # lista de tabelas para criar
        tab_list = {
            "Magic Form": "CSV/magicForm.csv",
            "Benjamin Graham": "CSV/ben_grahan.csv",
            "Décio Bazin": "CSV/decio_bazin.csv",
        }

        # criação do tabview
        tab_view = CTkTabview(
            self,
            width=869,
            height=445,
        )
        tab_view.place(x=14, y=99)

        # inserção dos tabs no tabview de acordo com os valores da tab_list
        for tab_item, caminho in tab_list.items():
            # - adicionando tab's
            tab_view.add(tab_item)
            tab_view.tab(tab_item).grid_columnconfigure(0, weight=1)

            # - elementos dos tabs
            # -- descrição
            discribe = CTkFrame(tab_view.tab(tab_item))
            discribe.place(x=0, y=0)

            titulo = CTkLabel(
                discribe,
                text=tab_item,
                font=("Arial", 32, "bold"),
                justify="center",
                width=237,
                height=50
                )
            titulo.pack()

            doc = Document(f"documents/{tab_item}.docx")
            read = [p.text for p in doc.paragraphs]

            texto = CTkLabel(
                discribe,
                text=read[0],
                font=("Arial", 20,),
                wraplength= 220,
                width=238,
                height=325,
                pady=20,
                justify="center"

                )
            texto.pack(padx=20)

            # -- tabela
            tabela = CTkFrame(tab_view.tab(tab_item))
            tabela.place(x=287, y=30)

            # le as informções no arquivo csv
            table_data = pd.read_csv(caminho)
            table_data = table_data.applymap(str)
            columns = [list(table_data)]
            rows = table_data.values.tolist()
            data = columns + rows

            # cria a tabela de acordo com os valores do arquivo csv
            for row_indice in range(len(rows)):
                for col_indice in range(4):
                    entry_item = CTkEntry(
                        tabela,
                        font=("Arial", 16, "bold"),
                        justify="center",
                    )

                    # Posiciona cada elemento da tabela de acordo com o csv
                    entry_item.grid(row=row_indice, column=col_indice)
                    # Insere o valor do arquivo csv em cada elemento da tabela
                    entry_item.insert(END, data[row_indice][col_indice])
                    entry_item.configure(state="disabled")


    def criar(self):
        """
        Cria o Relatório em pdf
        """
        destino = tkfd.askdirectory(title="Escolha onde salvar o relatório")
        do_pdf(destino)
        # root.destroy()
