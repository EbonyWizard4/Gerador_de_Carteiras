# import
import pandas as pd

def Model_01():
    tabela = pd.read_csv('data_base.csv')

    # construção da carteira
    # - filtro de valores magic formula
    liq_esperada = 1000000
    min_esperado = 0
    tabela = tabela[tabela['Liq.2meses'] > liq_esperada]
    tabela = tabela[tabela['EV/EBIT'] > min_esperado]
    tabela = tabela[tabela['ROIC'] > min_esperado]

    # criando coluna lucro sobre preço
    yield_minimo = 0.15
    yield_maximo = yield_minimo * 2

    tabela['Lucro' ] = tabela['Cotação' ] * tabela['Div.Yield' ] 
    tabela['Cot.Máxima'] = tabela['Lucro'] / yield_minimo

    # - filtro de valores aprimorados
    tabela = tabela[tabela['Cot.Máxima'] > tabela['Cotação']]

    # - rankear indices
    tabela['ranking_ev_ebit' ] = tabela['EV/EBIT'].rank(ascending = True)
    tabela['ranking_ev_roic' ] = tabela['ROIC'].rank(ascending = False)
    tabela['ranking_final' ] = tabela['ranking_ev_roic' ] + tabela['ranking_ev_ebit' ] 

    # - ordenar valores mais relevantes
    tabela = tabela.sort_values('ranking_final')

    # tratamento do Div.Yieald
    tabela = tabela[tabela['Div.Yield'] > yield_minimo]
    tabela = tabela[tabela['Div.Yield'] < yield_maximo]

    porcem = 100
    tabela['Div.Yield'] = tabela['Div.Yield'] * porcem

    # gerar carteira
    tabela = tabela[['Papel', 'Cotação', 'Cot.Máxima',  'Div.Yield' ]]

    # exibe tabela
    print(tabela)

    # salvando carteira em csv
    tabela.to_csv('modelo_01.csv', index=False)

# Model_01()