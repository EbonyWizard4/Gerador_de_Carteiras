import pandas as pd
import docx

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from docx.shared import Pt
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL

# Salvando em um arquivo
tabela = pd.read_csv('modelo_01.csv')
print(tabela)

# # - abre um documento
# doc = docx.Document()

# # - pega numero de linhas e colunas
# n_linhas = tabela.shape[0] 
# n_colunas = tabela.shape[1]

# print(n_colunas)
# print(n_linhas)

# # - cria uma tabela usando o dataframe
# tab = doc.add_table(rows=n_linhas, cols=n_colunas)

# # - itera os dados
# for col_ins, col_label in enumerate(tabela):
#     print(col_ins, col_label)
#     for row_ins in range(n_linhas):
#         cell_ = tab.cell(row_ins, col_ins)

#         if row_ins == 0:
#             cell_.text = tabela.columns[col_ins]

# for col_ins, col_label in enumerate(tabela):
#     print(col_ins, col_label)
#     for row_ins in range(n_linhas):
#         cell_ = tab.cell(row_ins, col_ins)
#         cell_.text = str(tabela[col_label][row_ins])

# # salva o arquivo
# doc.save('Relatório.docx')