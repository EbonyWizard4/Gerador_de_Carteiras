import pandas as pd
list_tabs = {"Magic Form":"CSV/magicForm.csv","Modelo 01":"CSV/modelo_01.csv"}

for tab_item, caminho in list_tabs.items():
    table_data = pd.read_csv(caminho)
    table_data = table_data.applymap(str)
    columns = [list(table_data)]
    rows = table_data.values.tolist()
    data = columns + rows

    for row_item in range(len(rows)):
        for j in range(2):
          print(row_item, j)
