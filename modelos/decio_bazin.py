"""
gera carteira segundo metodo bazin
"""
import pandas as pd


def model_bazin():
    """
    Faz o filtro no data base e monta a carterira
    """
    #Ler database
    tabela = pd.read_csv("CSV/data_base.csv")

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

    # exibe tabela
    print(tabela)

    # salvando carteira em csv
    tabela.to_csv("CSV/decio_bazin.csv", index=False)


model_bazin()
