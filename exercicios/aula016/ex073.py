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
print('-='*20)
print(f'Lista de times {times}')
print('-='*20)
print(f'Os 5 primeiros colocados são: {times[0:4]}.')
print('-='*20)
print(f'Os 4 últimos colocados são: {times[-4:]}.')
print('-='*20)
print(f'A ordem alfabetica dos times é {sorted(times)}')
print('-='*20)
print(f'O Cruzeiro está na {times.index("Cruzeiro")+1}ª posição. ')
print('-='*20)