from utils import utilsFunctions
import pandas as pd

rel_dysrup = utilsFunctions.read_excel()
rel_abc = utilsFunctions.read_excel()
erros = []

for index, row_dys in rel_dysrup.iterrows():
    loja_dys = row_dys['Loja']
    funcionario_dys = row_dys['Funcionário']
    programacao_dysrup = {
        # 'Loja': loja_dys,err
        'Segunda-feira': row_dys['Segunda-feira'],
        'Terça-feira': row_dys['Terça-feira'],
        'Quarta-feira': row_dys['Quarta-feira'],
        'Quinta-feira': row_dys['Quinta-feira'],
        'Sexta-feira': row_dys['Sexta-feira'],
        'Sábado': row_dys['Sábado']
    }
    for index, row_abc in rel_abc.iterrows():
        loja_abc = row_abc['Loja']
        funcionario_abc = row_abc['Promotor']
        if loja_dys == loja_abc:
            # print(loja_dys)
            programacao_abc = {
                # 'Loja': loja_abc,
                'Segunda-feira': row_abc['Segunda-feira'],
                'Terça-feira': row_abc['Terça-feira'],
                'Quarta-feira': row_abc['Quarta-feira'],
                'Quinta-feira': row_abc['Quinta-feira'],
                'Sexta-feira': row_abc['Sexta-feira'],
                'Sábado': row_abc['Sábado']
            }
            for day in programacao_dysrup:
                previsto_dys = programacao_dysrup[day]
                if previsto_dys != 'X':
                    previsto_dys = 'Vazio'
                previsto_abc = programacao_abc[day]
                if previsto_abc != 'X':
                    previsto_abc = 'Vazio'
                if previsto_dys != previsto_abc:
                    erro = {
                        'Loja': loja_abc,
                        'Funcionário na dysrup': funcionario_dys,
                        'Funcionário na Abc': funcionario_abc,
                        'Dia da semana': day,
                        'Programado na dysrup': previsto_dys,
                        'Programação da Abc': previsto_abc
                    }
                    erros.append(erro)

errado = pd.DataFrame(erros)

utilsFunctions.save_excel(errado)