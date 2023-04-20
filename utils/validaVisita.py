import utilsFunctions

controle = utilsFunctions.read_excel(header=3)
gestao = utilsFunctions.read_excel()
print(controle.columns)
print(gestao.columns)

for index, row in gestao.iterrows():
    if row['Cidade'] == 'Belo Horizonte - MG':
        if row['Status'] == 'Concluído' or row['Status'] == 'Em andamento':
            loja_gestão = row['Loja']
            promotor = row['Funcionário']
            for index, row in controle.iterrows():
                if loja_gestão == row['Loja']
#                 if row['Loja'] == loja_gestão:
#                     if row['Funcionário'] == promotor:
#                         print('Visita registrada na loja {} pelo promotor {}'.format(loja_gestão, promotor))
#             else:
#                 print('Loja {} foi atendida pelo promotor {}, mas não registrou a visita com o gerente'.format(loja_gestão,promotor))