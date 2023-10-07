"""
gera carteira segundo metodo Grahan
"""
import pandas as pd

class ModelGrahan:
    """Cria a carteira segundo modelo Grahan
    """
    def model_grahan(self):
        """
        Faz o filtro no data base e monta a carterira
        """
        try:
            #Ler database
            tabela = pd.read_csv("CSV/data_base.csv")
            # tratamento de dados das colunas principais
            tabela["Div.Yield"] = tabela["Div.Yield"].str.replace("%", "")
            tabela["Div.Yield"] = tabela["Div.Yield"].str.replace(".", "")
            tabela["Div.Yield"] = tabela["Div.Yield"].str.replace(",", ".")
            tabela["Div.Yield"] = tabela["Div.Yield"].astype(float)
            tabela["Div.Yield"] = round(tabela["Div.Yield"] / 100, 2)

            # - filtro adicional
            tabela = tabela[tabela["P/L"] > 0] #Lucro positivo

            # definições de valores para filtros
            constante = 22.5
            liq_esperada = 1000000
            tabela["LPA"] = tabela["Cotação"] / tabela["P/L"]
            tabela["VPA"] = tabela["Cotação"] / tabela["P/VP"]
            tabela["VI"] = round((constante*tabela["LPA"]*tabela["VPA"]) ** (1/2), 2)
            # tabela["VI"] = round(tabela["VI"] ** (1/2), 2)

            # - filtro de valores segundo Benjamim Grahan
            tabela = tabela[tabela["Liq.2meses"] > liq_esperada] #Liquidez
            tabela = tabela[tabela["Cotação"] < tabela["VI"]] #Valor Intrinseco


            # Tratamento do "Div.Yield"
            por_cem = 100
            tabela["Div.Yield"] = round(tabela["Div.Yield"] * por_cem, 2)

            # - ordenar valores mais relevantes
            tabela = tabela.sort_values("VI")


            # gerar carteira
            tabela = tabela.head(10)[["Papel", "Cotação", "VI", "Div.Yield"]]


            # salvando carteira em csv
            tabela.to_csv("CSV/ben_grahan.csv", index=False)

            # Confirmação de funcionamento
            print("\nMODEL GRAHAN\n")
            return True
        
        except RuntimeError:
            return

if __name__=="__main__":
    ModelGrahan().model_grahan()
