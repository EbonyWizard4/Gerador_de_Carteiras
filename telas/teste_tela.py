"""
Teste de Tela
"""


import tkinter.filedialog as tkfd
from tkinter import PhotoImage, Entry, END
import pandas as pd
from customtkinter import CTk, CTkLabel, CTkButton, CTkTabview, CTkFrame
from docx import Document


class Tela(CTk):
    """
    Classe para criar Tela
    Args:
        ctk (lib): Usado para criar tela
    """

    def criar(self):
        """
        Executa o programa em ordem
        """
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
        """
        Definições da Tela
        Args:
            mode (str): Dark ou Light
            title (tsr): Titulo da Tela
        """

        self._set_appearance_mode(mode)
        self.geometry("900x650")
        self.resizable(False, False)
        self.title(title)
        bg_image = PhotoImage(file="img/fg_900x650.png")
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
        button.place(x=42, y=585)

        self.carregar()
        
    def carregar(self):
        """
        Gera tela de carregamento
        """
        self.tab_gen()


    def tab_gen(self):
        """
        Gera Tabela
        """
        # lista de tabelas para criar
        list_tabs = {
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

        # inserção dos tabs de acordo com os valores da list_tabs
        for tab_item, caminho in list_tabs.items():
            tab_view.add(tab_item)
            tab_view.tab(tab_item).grid_columnconfigure(0, weight=1)  

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
            reslt = [p.text for p in doc.paragraphs]

            texto = CTkLabel(
                discribe,
                text=reslt[0],
                font=("Arial", 20,),
                wraplength= 220,
                width=238,
                height=325,
                pady=20,
                justify="center"

                )
            texto.pack(padx=20)
            # texto.insert("1.1",reslt[0])


            tabela = CTkFrame(tab_view.tab(tab_item))
            tabela.place(x=284, y=0)

            # le as informções no arquivo csv
            table_data = pd.read_csv(caminho)
            table_data = table_data.applymap(str)
            columns = [list(table_data)]
            rows = table_data.values.tolist()
            data = columns + rows

            # cria a tabela de acordo com os valores do arquivo csv
            for row_indice in range(len(rows)):
                for col_indice in range(4):
                    entry_item = Entry(
                        tabela,
                        width=11,
                        fg="blue",
                        font=("Arial", 16, "bold"),
                        justify="center",
                    )

                    # Posiciona cada elemento da tabela de acordo com o csv
                    entry_item.grid(row=row_indice, column=col_indice)
                    # Insere o valor do arquivo csv em cada elemento da tabela
                    entry_item.insert(END, data[row_indice][col_indice])
