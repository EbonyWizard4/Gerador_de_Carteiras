from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.fundamentus.com.br/resultado.php')
localTabela = '/html/body/div[1]/div[2]/table'
tabela = driver.find_element('xpath', localTabela)
html_tabela = tabela.get_attribute('outerHTML')
tabela = pd.read_html(str(html_tabela), thousands='.', decimal=',')[0]
tabela = tabela.set_index(['Papel'])

tabela = tabela[['Cotação', 'EV/EBIT', 'ROIC', 'Liq.2meses']]
print(tabela)