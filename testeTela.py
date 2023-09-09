"""Teste de Tela
"""
from tkinter import PhotoImage
from customtkinter import CTk, CTkLabel, CTkButton

class Tela(CTk):
    """Classe para criar Tela

    Args:
        ctk (lib): Usado para criar tela
    """  
    
    def root_gen(self, mode, title):
        """Definições da Tela

        Args:
            mode (str): Dark ou Light
            title (tsr): Titulo da Tela
        """
        
        self._set_appearance_mode(mode)
        self.geometry("900x600")
        self.resizable(False,False)
        self.title(title)
        bg_image = PhotoImage(file="img/fundoApp2.png")
        lable1 = CTkLabel(self, image=bg_image, text="" )
        lable1.place(x=0, y=0)
        button = CTkButton(
            self,
            width=180,
            height=49,
            corner_radius=0,
            text="Salvar"
        )
        button.place(x=51, y=491)


if __name__=="__main__":
    root = Tela()
    root.root_gen("dark","Stock Portfolio")
    root.mainloop()
