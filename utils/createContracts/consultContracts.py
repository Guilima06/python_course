import requests
from utils import utilsFunctions
import pandas as pd

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIyIiwianRpIjoiNWEwZmRiZjhkNzBmOGVmNzM3ZGRlNDk3MjZiNDJkYjQ4NTg2YmEwNGI1YWY1MzIxZWM1ZDM0MDI1NjYwODkzMWFkM2Q5ZTk3NjM1MWYwYTQiLCJpYXQiOjE3MDQ2Nzg0ODcuNTU0NDIyLCJuYmYiOjE3MDQ2Nzg0ODcuNTU0NDI0LCJleHAiOjE3MTI0NTQ0ODcuNTQ5NzczLCJzdWIiOiIxNiIsInNjb3BlcyI6W119.QXF5eiWo9-ZxotU1KnF7iqi71EP4t4qchYFEg3FOMTRawdMeOjPf-NQCWmCPgcANkHFsYtFbPXIvsJFks_oeV1juykFv1Jh40Cv_DGe-10CJuGzpjyVzrlhqbukQc8m5eWffumW9Zlxbu8iF8GBl0zUceKAQDuxEEZQuOIFuokAyzSh4-Uu6ZTKkAP9n40qfE6-0dDq2P11FKG-uF2U3-kNIkJrNReOK-qX5X1pYXMg0gGyLqm6nVQDYN-cUjl34SUcUimaz7x1bMM4BeZHbxUuK33mb5Spbjy0JXHver5gacvwF-mRhe23Y4WixK_DTH69FAGeOlPYbjJcQ0dvV1DOxDVPIjJ8rjwx_zVmcOgTJVm9hH78P2mRAAa4eZirwOCZu_mTsOXtcpWLGyvAt9nHj43bV1tvOAr25L5K8YXOMqh2jmYjpMPdnd2iDX3qCWjA6QiKfhdiYHh09lRhL8FFXqoJAWwVvGrBCL2b3Gg0iw3WBmNGMMFTHFvpyKtCn0IrHjSaC7E_hvPZMUJ2xNC9j--348yepEmXXN82ddMaMlMcHFM1G1glzYUhRaC6VVSOSaJij-gp36-wTzWv7w6J2MDJXsnSvaN5q2cDvm6uPX8BbqKTr1BI-2WBDnBP19Ut2slOdlZj1EQaK4Zt4VEFxFLxKP0EGEOjdQyTeRjk"
headers = {'Authorization': f'Bearer {token}'}


def consult_contracts():
    client = escolher_client()

    contracts_param = {
        'clients_id': client,
        'status': 'active'
    }

    contract = escolher_contrato(contracts_param)
    # print(contract)

    get_contract_param = {
        'contract_id': contract,
        'isFromGrid': False
    }

    contract_data = get_contract_data(get_contract_param)

    new_contract = format_new_contract(contract_data)
    print(new_contract)
    create_new_contract(new_contract)




def get_clients():
    url = 'https://app.dysrup.com.br/api/v1/web/client/filter'
    response = requests.post(url, headers=headers)

    clients_response = response.json()
    clients_json = []

    for client in clients_response['data']:
        client_id = client['client_id']
        client_name = client['client_name']
        client_data = {
            'clients_id': client_id,
            'client_name': client_name
        }
        clients_json.append(client_data)
    return clients_json


def get_list_contracts(contracts_json):
    url = 'https://app.dysrup.com.br/api/v1/web/contract/filter'
    response = requests.post(url, headers=headers, json=contracts_json)
    contracts_response = response.json()
    print(contracts_response)
    return contracts_response


def escolher_client():
    clients = get_clients()

    print('-=' * 20)
    print('Escolha um cliente abaixo')
    print('-=' * 20)

    for indice, client in enumerate(clients):
        # client_id = client['clients_id']
        client_name = client['client_name']
        print(f'{indice + 1} - Nome:{client_name}')

    client_desejado = clients[int(input('\nInsira o número do cliente que deseja: ')) - 1]
    ids_clients = [client_desejado['clients_id']]
    return ids_clients


def escolher_contrato(contracts_param):
    contracts = get_list_contracts(contracts_param)

    print('-=' * 20)
    print('Escolha o contrato desejado')
    print('-=' * 20)

    for indice, contract in enumerate(contracts['data']):
        client_name = contract['client_name']
        network_name = contract['network_name']
        flag_name = contract['flag_name']
        service_type = contract['service_type']
        status = contract['status']

        print(f'{indice + 1} - Nome:{client_name}\n Rede: {network_name}\n Bandeira: {flag_name}\n '
              f'Tipo de serviço: {service_type}\n Status: {status}\n')

    contrato_desejado = contracts['data'][int(input('Insira o número do contrato que deseja: ')) - 1]
    contract_id = contrato_desejado['contract_id']
    return contract_id


def get_contract_data(contract_json):
    url = 'https://app.dysrup.com.br/api/v1/web/contract/get'
    response = requests.post(url, headers=headers, json=contract_json)
    contracts_response = response.json()
    return contracts_response


def format_new_contract(contract_data):
    contract_product_group = contract_data['data']['products_group']
    new_product_group = create_product_group(contract_product_group)

    contract_requests_group = contract_data['data']['requests_group']
    new_requests_group = create_requests_group(contract_requests_group)

    new_contract = {
        "service_type": "exclusive",
        "status": "active",
        "flag_id": contract_data['data']['basic_data']['flag_id'],
        'client_id': contract_data['data']['basic_data']['client_id'],
        'products_group': new_product_group,
        'requests_group': new_requests_group
    }
    return new_contract


def create_product_group(product_group):
    products_group = []

    for group in product_group:
        new_group = {
            'control': 'new',
            'product': group['product'],
            'store': group['store']
        }
        products_group.append(new_group)
    return products_group


def create_requests_group(contract_requests_group):
    requests_groups = []

    for group in contract_requests_group:
        product = format_request_products(group['product'])
        new_group = {
            'control': 'new',
            'request_description': group['description'],
            'network_client_code': group['client_code'],
            'store': group['store'],
            'product': product
        }
        requests_groups.append(new_group)
    return requests_groups


def format_request_products(product):
    request_products = []

    for information in product:
        new_products = {
            'control': 'new',
            'product_id': information['id'],
            'product_code': information['product_code'],
            'product_order': information['order']
        }
        request_products.append(new_products)
    return request_products

def create_new_contract(new_contract):
    url = 'https://app.dysrup.com.br/api/v1/web/contract/create'
    response = requests.post(url, headers=headers, json=new_contract)
    status_create = response.json()
    print(status_create)


while True:
    consult_contracts()
    user = str(input('Continuar? '))
    if 'Nn' in user:
        break