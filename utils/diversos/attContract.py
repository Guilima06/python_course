from utils import utilsFunctions

excel = utilsFunctions.read_excel()
contratantes = []
for index, contratante in excel.iterrows():
    tenant_id = ['']
    cnpj = excel['CNPJ']
    