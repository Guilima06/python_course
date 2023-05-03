# crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro
# na ordem de colocação. depois mostre: A) Apenas os 5 primeiros colocados.
# B) Os ultimos 4 colocados da tabela.
# C) uma lista com os times em ordem alfabética
# D) em que posição da tabela está o time do Cruzeiro.
from utils import utilsFunctions

times = ('Botafogo', 'Fortaleza', 'Palmeiras', 'Internacional', 'Fluminense', 'Cruzeiro', 'Grêmio', 'São Paulo',
         "Vasco da Gama", 'Atlético-MG', 'Santos', 'Bragantino', 'Flamengo', 'Athletico-PR', 'Bahia', 'Goiás',
         "Corinthians", 'Cuiabá', 'Coritiba', 'América-MG',
)
print(f'Os 5 primeiros colocados são: {times[0]}, {times[1]}, {times[2]}, {times[3]} e {times[4]}.')
print(f'Os 4 últimos colocados são: {times[-4]}, {times[-3]}, {times[-2]} e {times[-1]}.')
print(f'A ordem alfabetica dos times é {sorted(times)}')
contador = 0
for time in times:
    if times[contador] == 'Cruzeiro':
        print(f'O Cruzeiro está na {contador}ª posição. ')
        break
    else:
        contador += 1
