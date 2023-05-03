from utils import utilsFunctions

rel_atendimento = utilsFunctions.read_excel()
rel_visitas = utilsFunctions.read_excel(header=3)
lojas = utilsFunctions.read_excel()
lista_atendimentos = []
lista_visitas = []
lista_lojas = []
visita_controle = ''
relatorio = []

for index, row in rel_atendimento.iterrows():
    loja_atendimento = row['Loja']
    cargo_func_atendimento = row['Cargo']
    funcionario_atendimento = row['Funcionário']
    data_atendimento = row['Data']
    status_atendimento = row['Status']
    check_in = row['Check-in']
    check_out = row['Check-out']
    adc_manual = row['Adicionado manualmente']
    atendimento = {
        'Loja': loja_atendimento,
        'Cargo': cargo_func_atendimento,
        'Funcionário': funcionario_atendimento,
        'Data': data_atendimento,
        'Status': status_atendimento,
        'Check-in': check_in,
        'Check-out': check_out,
        'Adicionado manualmente': adc_manual
    }
    lista_atendimentos.append(atendimento)

for index, row in rel_visitas.iterrows():
    loja_visita = row['Loja']
    cargo_func_visita = row['Cargo']
    funcionario_visita = row['Funcionário']
    data_visita = row['Data da visita']
    tipo_autent_visit = row['Tipo de autenticação']
    visita = {
        'Loja': loja_visita,
        'Cargo': cargo_func_visita,
        'Funcionário': funcionario_visita,
        'Data da visita': data_visita,
        'Tipo de autenticação': tipo_autent_visit
    }
    lista_visitas.append(visita)

for index, row in lojas.iterrows():
    loja_lista = row['Nome da loja']
    status_loja = row['Status']
    cidade_loja = row['Cidade - UF']
    regional_loja = row['Regional']
    dados_loja = {
        'Nome da loja': loja_lista,
        'Status': status_loja,
        'Cidade - UF': cidade_loja,
        'Regional': regional_loja
    }
    lista_lojas.append(dados_loja)


for atendimento in lista_atendimentos:
    verificacao = ''
    if atendimento['Status'] != 'Pendente':
        for visita in lista_visitas:
            if visita['Loja'] == atendimento['Loja'] and visita['Funcionário'] == atendimento['Funcionário']:
                visita_controle = 'Visita Registrada'
                loja = utilsFunctions.find_loja(lista_lojas, 'Nome da loja', atendimento['Loja'])
                analise = {
                    'Loja': atendimento['Loja'],
                    'Cidade': loja['Cidade - UF'],
                    'Regional': loja['Regional'],
                    'Cargo': atendimento['Cargo'],
                    'Funcionário': atendimento['Funcionário'],
                    'Data': atendimento['Data'],
                    'Status': atendimento['Status'],
                    'Check-in': atendimento['Check-in'],
                    'Check-out': atendimento['Check-out'],
                    'Adicionado manualmente': atendimento['Adicionado manualmente'],
                    'Visita controle': visita_controle,
                    'Data da visita': visita['Data da visita'],
                    'Tipo de autenticação': visita['Tipo de autenticação']
                }
                relatorio.append(analise)
                verificacao = 'Ok'
                break
            else:
                verificacao = "Não encontrado"
        if verificacao == 'Não encontrado':
            visita_controle = 'Visita não registrada'
            loja = utilsFunctions.find_loja(lista_lojas, 'Nome da loja', atendimento['Loja'])
            analise = {
                'Loja': atendimento['Loja'],
                'Cidade': loja['Cidade - UF'],
                'Regional': loja['Regional'],
                'Cargo': atendimento['Cargo'],
                'Funcionário': atendimento['Funcionário'],
                'Data': atendimento['Data'],
                'Status': atendimento['Status'],
                'Check-in': atendimento['Check-in'],
                'Check-out': atendimento['Check-out'],
                'Adicionado manualmente': atendimento['Adicionado manualmente'],
                'Visita controle': visita_controle,
                'Data da visita': visita['Data da visita'],
                'Tipo de autenticação': visita['Tipo de autenticação']
            }
            relatorio.append(analise)


relatorio_ordenado = sorted(relatorio, key=lambda relatorio: relatorio['Loja'])
# print(relatorio_ordenado)
utilsFunctions.save_excel(relatorio_ordenado)
