import pandas as pd
import utilsFunctions

products = pd.read_excel(utilsFunctions.open_file(), header=1)
products_list = []
print(products.columns)

for row in products.iterrows():
    id_product = products['ID']
    description = products['Descrição']
    status = 'Ativo'
    marca = products['Marca']
    code = products['Código referência da indústria']
    categoria = products['Categoria']
    data_products = {
        'ID': id_product,
        'Descrição': description,
        'Status': status,
        'Marca': marca,
        'Código referência da indústria': code,
        'Categoria': categoria
    }
    products_list.append(data_products)
print(products_list)
utilsFunctions.write_excel(products_list)