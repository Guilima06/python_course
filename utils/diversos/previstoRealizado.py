from utils import utilsFunctions

# rel_atendimento = utilsFunctions.read_excel()
# rel_visitas = utilsFunctions.read_excel(header=3)
# lojas = utilsFunctions.read_excel()
# lista_atendimentos = []
# lista_visitas = []
# lista_lojas = []
visita_controle = ''
relatorio = []


def atendimentos_gestao():
    lista_atendimentos = []
    rel_atendimento = utilsFunctions.read_excel()
    for index, row in rel_atendimento.iterrows():
        loja_atendimento = row['Loja']
        roteiro = row['Roteiro']
        cargo_func_atendimento = row['Cargo']
        funcionario_atendimento = row['Funcionário']
        data_atendimento = row['Data']
        status_atendimento = row['Status']
        check_in = row['Check-in']
        check_out = row['Check-out']
        adc_manual = row['Adicionado manualmente']
        atendimento = {
            'Loja': loja_atendimento,
            'Roteiro': roteiro,
            'Cargo': cargo_func_atendimento,
            'Funcionário': funcionario_atendimento,
            'Data': data_atendimento,
            'Status': status_atendimento,
            'Check-in': check_in,
            'Check-out': check_out,
            'Adicionado manualmente': adc_manual
        }
        lista_atendimentos.append(atendimento)
    return lista_atendimentos


def visitas_controle():
    lista_visitas = []
    rel_visitas = utilsFunctions.read_excel(header=3)
    for index, row in rel_visitas.iterrows():
        nome_loja = row['Loja']
        cargo = row['Cargo']
        funcionario = row['Funcionário']
        data_visita = row['Data da visita']
        tipo_autent = row['Tipo de autenticação']
        visita = {
            'Loja': nome_loja,
            'Cargo': cargo,
            'Funcionário': funcionario,
            'Data da visita': data_visita,
            'Tipo de autenticação': tipo_autent
        }
        lista_visitas.append(visita)
    return lista_visitas


def lojas():
    lista_lojas = []
    lojas = utilsFunctions.read_excel()
    for index, row in lojas.iterrows():
        nome_loja = row['Nome da loja']
        status_loja = row['Status']
        cidade_loja = row['Cidade - UF']
        regional_loja = row['Regional']
        dados_loja = {
            'Nome da loja': nome_loja,
            'Status': status_loja,
            'Cidade - UF': cidade_loja,
            'Regional': regional_loja
        }
        lista_lojas.append(dados_loja)
    return lista_lojas


lista_lojas = lojas()
lista_atend_gest = atendimentos_gestao()
lista_visit_control = visitas_controle()
contador = 0



for atendimento in lista_atend_gest:
    verificacao = ''
    if atendimento['Status'] != 'Pendente':
        for visita in lista_visit_control:
            if visita['Loja'] == atendimento['Loja'] and visita['Funcionário'] == atendimento['Funcionário'] and \
                    visita['Data da visita'] == atendimento['Data']:
                visita_controle = 'Visita Registrada'
                loja = utilsFunctions.find_loja(lista_lojas, 'Nome da loja', atendimento['Loja'])
                analise = {
                    'Loja': atendimento['Loja'],
                    'Cidade': loja['Cidade - UF'],
                    'Regional': loja['Regional'],
                    'Roteiro': atendimento['Roteiro'],
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
                'Roteiro': atendimento['Roteiro'],
                'Cargo': atendimento['Cargo'],
                'Funcionário': atendimento['Funcionário'],
                'Data': atendimento['Data'],
                'Status': atendimento['Status'],
                'Check-in': atendimento['Check-in'],
                'Check-out': atendimento['Check-out'],
                'Adicionado manualmente': atendimento['Adicionado manualmente'],
                'Visita controle': visita_controle,
                'Data da visita': '',
                'Tipo de autenticação': ''
            }
            relatorio.append(analise)

for loja in lista_lojas:
    store = loja['Nome da loja']
    atendimento_encontrado = False
    for visita in lista_visit_control:
        if visita['Loja'] == store:
            atendimento_encontrado = True
            break
    if not atendimento_encontrado:
        analise = {
            'Loja': store,
            'Cidade': loja['Cidade - UF'],
            'Regional': loja['Regional'],
            'Roteiro': '',
            'Cargo': '',
            'Funcionário': '',
            'Data': '',
            'Status': '',
            'Check-in': '',
            'Check-out': '',
            'Adicionado manualmente': '',
            'Visita controle': 'Loja sem nenhuma visita validada',
            'Data da visita': '',
            'Tipo de autenticação': ''
        }
        relatorio.append(analise)


relatorio_ordenado = sorted(relatorio, key=lambda relatorio: relatorio['Loja'])
utilsFunctions.save_excel(relatorio_ordenado)
