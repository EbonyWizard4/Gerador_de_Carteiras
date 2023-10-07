"""
Modul principal
"""
from telas import Tela
from scraping import Scraping
from modelos import MagicForm, ModelBazin, ModelGrahan

if __name__ == "__main__":
    scraping = Scraping().scraping()
    if scraping:
        # cria as carteiras
        MagicForm().magic_form()
        ModelBazin().model_bazin()
        ModelGrahan().model_grahan()

        # Renderiza a Tela
        root = Tela()
        root.root_gen("dark", "Stock Portfolio")
        root.mainloop()
    else:
        print('Deu ruim no scraping')
