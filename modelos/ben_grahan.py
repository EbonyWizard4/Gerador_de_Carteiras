"""
gera carteira segundo metodo Grahan
"""
import pandas as pd


def model_grahan():
    """
    Faz o filtro no data base e monta a carterira
    """
    #Ler database
    tabela = pd.read_csv("CSV/data_base.csv")


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

    # exibe tabela
    print(tabela)

    # salvando carteira em csv
    tabela.to_csv("CSV/ben_grahan.csv", index=False)


model_grahan()
