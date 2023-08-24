# import
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
# configurar o chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# webscrapping da tabela
driver.get('https://www.fundamentus.com.br/resultado.php')
localTabela = '/html/body/div[1]/div[2]/table'
tabela = driver.find_element('xpath', localTabela)
# tratamento da tabela
html_tabela = tabela.get_attribute('outerHTML')
tabela = pd.read_html(str(html_tabela), thousands='.', decimal=',')[0]
tabela = tabela.set_index(['Papel'])
# filtrar colunas
tabela = tabela[['Cotação', 'EV/EBIT', 'ROIC', 'Liq.2meses']]
# tratamento de dados das colunas
tabela['ROIC'] = tabela['ROIC'].str.replace("%", "")
tabela['ROIC'] = tabela['ROIC'].str.replace(".", "")
tabela['ROIC'] = tabela['ROIC'].str.replace(",", ".")
tabela['ROIC'] = tabela['ROIC'].astype(float)
# construção da carteira
# - filtro de valores
tabela = tabela[tabela['Liq.2meses'] > 1000000]
tabela = tabela[tabela['EV/EBIT'] > 0]
tabela = tabela[tabela['ROIC'] > 0]
# rankear indices
tabela['ranking_ev_ebit' ] = tabela['EV/EBIT'].rank(ascending = True)
tabela['ranking_ev_roic' ] = tabela['ROIC'].rank(ascending = False)
tabela['ranking_final' ] = tabela['ranking_ev_roic' ] + tabela['ranking_ev_ebit' ] 
# - ordenar valores mais relevantes
tabela = tabela.sort_values('ranking_final')
# exibe tabela
print(tabela.head(10)[['Cotação', 'EV/EBIT', 'ROIC', 'Liq.2meses', 'ranking_final' ]])