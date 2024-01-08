import requests
from utils import utilsFunctions
import pandas as pd

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIyIiwianRpIjoiNTgyOWVhNzU0YTAyMjNiMjdkYTRiMzJhOTgxMjQzOTM2MzI5NTFhYTBjNWUxNzRkY2YxNmQyMDgxN2NiMzRkMjllMjI4NTc3MjM4OTNjZjUiLCJpYXQiOjE3MDQ2NTc0MjQuNzg2MjQ5LCJuYmYiOjE3MDQ2NTc0MjQuNzg2MjUxLCJleHAiOjE3MTI0MzM0MjQuNzc5ODU0LCJzdWIiOiI0NjQiLCJzY29wZXMiOltdfQ.c5At6NZKT3zQrote9luA_0G2T20yzDUvrlQShYtU8CoD8cUgiBPVLQNPykjT0YF1Ax4wPNnw6twyx0vD24FCYhxt3IklhwY2UM13M7ixXyguwi7VsQ2j21OxY6sUfit6t2Rr1TCklrDWgpi5e6G80p6qjxuDWox-yblJyw66TB-nH911phnf0uiQ9MCCvfVZIxPzSSmxovLHmnvyVtWAq0BNkF3rosNd-EwswXV61-kM5I2c9IRBhBLfrFtQ7xHX5ttuHPkB50dJBBX1vsCUFXmeEdH6Dn0jb4IuF4OPAvWNf_H_OP4cb-ncdH3aZuFXZE8yQNaLzT3lrOIhxbcvej8kQQlBsr32Buui2oLBHzajzIM8yK8QDtoxOyfT0-L5LKnjmy4o3rWkQRWzjWzBzKWjgaTYLlYVE2XMMsRhccvRY2CPFrg0NFUNEvCvsdDz2p_iAAg9r6pyj190kVmi0zsrAK0RkL8TLBVZLSvwBDa5SbaWvn31SFUpFUwFpeWnvbQmqcuQWe0dvc3d_ddxluCQvoiAp6K2-vNhYNV3GR8bcV6tNC9h6Uw2hkJc6o3QAocfr9y73xAIX402Mrw9MLJny8EXUbDQZmri7oi4fzL_brZKAQhKNDPXCrfxCa6pHdWjLsq4mX1In_-4l4_M4wlVkvBz7zVS5Nhc7veYioQ"
headers = {'Authorization': f'Bearer {token}'}

# print("Criação de contrato")
# print("Insira o número, referente ao cliente: ")


contract_data_excel = utilsFunctions.read_excel()
# products_group_data_excel = utilsFunctions.read_excel()
# requests_group_data_excel = utilsFunctions.read_excel()

contract_data = []
# products_group_data = []
# requests_group_data = []

for index, row in contract_data_excel.iterrows():
    service_type_excel = row['Tipo de serviço']
    status_excel = row['Status']
    flag_excel = row['Bandeira']
    client_excel = row['Cliente']

    service_type = ''
    status = ''
    flag = ''
    client = ''

    if service_type_excel == 'Exclusivo':
        service_type = 'exclusive'
    elif service_type_excel == 'Compartilhado':
        service_type = 'shared'
    else:
        print('Tipo de serviço inválido')

    if status_excel == 'Ativo':
        status = 'active'
    elif status_excel == 'Inativo':
        status = 'inactive'
    else:
        print('Status inválido')

    contract = {
        "service_type": service_type,
        'status': status,
        'flag_id': flag,
        'clients_id': client,
        'products_group': [],
        'requests_group': []
    }
    print(contract)
