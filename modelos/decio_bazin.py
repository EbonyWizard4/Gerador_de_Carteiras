"""
gera carteira segundo metodo bazin
"""
import pandas as pd


class ModelBazin:
    """
    Cria a carteira segundo Modelo Bazin
    """
    def model_bazin(self):
        """
        Faz o filtro no data base e monta a carterira
        """
        #Ler database
        try:
            tabela = pd.read_csv("CSV/data_base.csv")

            # tratamento de dados das colunas principais
            tabela["Div.Yield"] = tabela["Div.Yield"].str.replace("%", "")
            tabela["Div.Yield"] = tabela["Div.Yield"].str.replace(".", "")
            tabela["Div.Yield"] = tabela["Div.Yield"].str.replace(",", ".")
            tabela["Div.Yield"] = tabela["Div.Yield"].astype(float)
            tabela["Div.Yield"] = round(tabela["Div.Yield"] / 100, 2)

            # definições de valores para filtros
            liq_esperada = 1000000
            dy_esperado = 0.06
            tabela["3xEBIT"] = 3 * (tabela["Cotação"] / tabela["P/EBIT"])
            tabela["Lucro"] = tabela["Cotação"] * tabela["Div.Yield"]
            tabela["Preço.Justo"] = round(tabela["Lucro"] / dy_esperado, 2)

            # - filtro de valores segundo Décio Bazin
            tabela = tabela[tabela["Liq.2meses"] > liq_esperada] #Liquidez
            tabela = tabela[tabela["Div.Yield"] > dy_esperado] #Cash Yield
            tabela = tabela[tabela["Dív.Brut/ Patrim."] < tabela["3xEBIT"]] #Endividamento
            tabela = tabela[tabela["Preço.Justo"]>tabela["Cotação"]] #Preço Justo

            # - filtro adicional
            tabela = tabela[tabela["P/L"] > 0] #Lucro positivo

            # Tratamento do "Div.Yield"
            por_cem = 100
            tabela["Div.Yield"] = round(tabela["Div.Yield"] * por_cem, 2)

            # - ordenar valores mais relevantes
            tabela = tabela.sort_values("Preço.Justo")


            # gerar carteira
            tabela = tabela.head(10)[["Papel", "Cotação", "Preço.Justo", "Div.Yield"]]


            # salvando carteira em csv
            tabela.to_csv("CSV/decio_bazin.csv", index=False)

            # Confirmação de funcionamento
            print("\nMODEL BAZIN\n")
            return True
        except RuntimeError:
            return

if __name__=="__main__":
    ModelBazin().model_bazin()
