import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def Scraping():
    # configurar o chrome
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # webscrapping da tabela
    driver.get("https://www.fundamentus.com.br/resultado.php")
    localTabela = "/html/body/div[1]/div[2]/table"
    tabela = driver.find_element("xpath", localTabela)
    # tratamento da tabela
    html_tabela = tabela.get_attribute("outerHTML")
    tabela = pd.read_html(str(html_tabela), thousands=".", decimal=",")[0]
    # filtrar colunas
    tabela = tabela[["Papel", "Cotação", "EV/EBIT", "ROIC", "Liq.2meses", "Div.Yield"]]

    # tratamento de dados das colunas
    tabela["ROIC"] = tabela["ROIC"].str.replace("%", "")
    tabela["ROIC"] = tabela["ROIC"].str.replace(".", "")
    tabela["ROIC"] = tabela["ROIC"].str.replace(",", ".")
    tabela["ROIC"] = tabela["ROIC"].astype(float)
    tabela["Div.Yield"] = tabela["Div.Yield"].str.replace("%", "")
    tabela["Div.Yield"] = tabela["Div.Yield"].str.replace(".", "")
    tabela["Div.Yield"] = tabela["Div.Yield"].str.replace(",", ".")
    tabela["Div.Yield"] = tabela["Div.Yield"].astype(float)
    tabela["Div.Yield"] = tabela["Div.Yield"] / 100

    print(tabela)
    tabela.to_csv("data_base.csv", index=False)


# scraping()
