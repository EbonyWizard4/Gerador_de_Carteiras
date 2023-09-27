"""
Modul principal
"""
from telas import Tela
from scraping import Scraping

if __name__ == "__main__":
    scraping = Scraping()
    if scraping:
        root = Tela()
        # root.carregar()
        root.root_gen("dark", "Stock Portfolio")
        root.mainloop()
    else:
        print('Deu ruim no scraping')
