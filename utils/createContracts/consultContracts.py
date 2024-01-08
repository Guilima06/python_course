import requests
from utils import utilsFunctions
import pandas as pd

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIyIiwianRpIjoiMDVhY2FkYmNkNThkZGNmYzg0ODQyYTZkY2IyMDRmODI5OTI1MWI5ZGVlZjk1NDIyZGNmM2MyYmNkNWVlMzIzMzE0ODI2Yjc2YzJhMmVhMzUiLCJpYXQiOjE3MDQ3MzQzNzUuNzQyODQ1LCJuYmYiOjE3MDQ3MzQzNzUuNzQyODQ4LCJleHAiOjE3MTI1MTAzNzUuNzM3MTMsInN1YiI6IjE2Iiwic2NvcGVzIjpbXX0.jTRpcOG6NK3v3oq0c0HZGzIY2X8cxJQN2f-68PM-sAm3HmwHAkRsQ7YtX9HbvcWLGYBJTN1cbEI4bBGfEZtaL_7DE1NbZKpQyTKd-FkuZb_dRZYzOC8hjP9B-zMVqDaFsxxwdxx6uv0BfohquafvYRwuU41tmxOPUNq__Y4GN5kkcObLfOpl_16uMTgva6BOttwNVp1cf2x4IhqbMijsZ5b4E8a2zq6c1gFyCLIHaLZwvmsrTj2h_X2_MceVKCkUTDAjqdS3GaFshd2urQs6PqkXuunORlmwIfRQ-SNabG5j1idLOpScrCTkv4X6SerOB8Lu2GNGZvWUFar6T-XltYHVToLLALv-QOCvUxtg0mGR1ux1Sw_erIxZD-myABp7VWVMPumyl8Q4lr9t_HHrW8oay8H6iEnEm_nlIXtMCqz8tDYJJSVazf_TH2Y2fq-Cx7bO3QqGWGAcPN2dfBiSEUWvpj6UvgqyC1SoWs5UB5g9FxQ4ZzarxfdbENgat4OCWlh8GDtbSkvjr9TTA9VP5FPNQOP2izwgbnSvzpQrcgF7jwLcBiri2bsqxKL5oIVpybfgpyFeX0jdSQLnbsEMwpnHDUSl8Q6xza5SmwkTxCgJW1M-6o9wo6sNBxzuZzCO1VDNpbAV82xXT9vfCWPBxlUksunrv_xJ7usgzM_BUIM"
headers = {'Authorization': f'Bearer {token}'}


def consult_contracts():
    client = escolher_client()
    contracts_param = {
        'clients_id': client,
        'status': 'active'
    }

    contract_base = escolher_contrato_base(contracts_param)
    get_contract_param = {
        'contract_id': contract_base,
        'isFromGrid': False
    }
    contract_base_data = get_contract_data(get_contract_param)

    contract_destiny = escolher_contrato_destino(contracts_param)
    get_contract_param = {
        'contract_id': contract_destiny,
        'isFromGrid': False
    }
    contract_destiny_data = get_contract_data(get_contract_param)

    contract_data_to_delete = delete_old_requests_and_create_new_requests(contract_base_data, contract_destiny_data, contract_destiny)


    # edit_contract = format_edit_contract(contract_base_data, contract_destiny)
    # print(edit_contract)

    # new_contract = format_new_contract(contract_data)
    # print(new_contract)
    # create_contract(new_contract)




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


def escolher_contrato_base(contracts_param):
    contracts = get_list_contracts(contracts_param)

    print('-=' * 20)
    print('Escolha o contrato base')
    print('-=' * 20)

    for indice, contract in enumerate(contracts['data']):
        client_name = contract['client_name']
        network_name = contract['network_name']
        flag_name = contract['flag_name']
        service_type = contract['service_type']
        status = contract['status']

        print(f'{indice + 1} - Nome:{client_name}\n Rede: {network_name}\n Bandeira: {flag_name}\n '
              f'Tipo de serviço: {service_type}\n Status: {status}\n')

    contrato_desejado = contracts['data'][int(input('Insira o número do contrato que deseja usar como base para duplicar: ')) - 1]
    contract_id = contrato_desejado['contract_id']
    return contract_id


def escolher_contrato_destino(contracts_param):
    contracts = get_list_contracts(contracts_param)

    print('-=' * 20)
    print('Escolha o contrato de destino')
    print('-=' * 20)

    for indice, contract in enumerate(contracts['data']):
        client_name = contract['client_name']
        network_name = contract['network_name']
        flag_name = contract['flag_name']
        service_type = contract['service_type']
        status = contract['status']

        print(f'{indice + 1} - Nome:{client_name}\n Rede: {network_name}\n Bandeira: {flag_name}\n '
              f'Tipo de serviço: {service_type}\n Status: {status}\n')

    contrato_desejado = contracts['data'][int(input('Insira o número do contrato que deseja inserir os dados copiados: ')) - 1]
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


def delete_old_requests_and_create_new_requests(contract_base_data, contract_destiny_data, contract_destiny):

    contract_product_group = contract_destiny_data['data']['products_group']
    edited_product_group = edit_product_group(contract_product_group)

    request_group = contract_destiny_data['data']['requests_group']

    delete_requests_group = []
    try:
        for group in request_group:
            print(f'Grupo encontrado {group['id']}')

            requests_group_data = {
                'id': group['id'],
                'control': 'del',
                'product': []
            }
            print(f'Grupo ajustado {requests_group_data}')
            delete_requests_group.append(requests_group_data)
        print(f'lista criada com grupos de pedidos para apagar {delete_requests_group}')

        edit_contract = {
            "service_type": "exclusive",
            "status": "active",
            'client_id': contract_destiny_data['data']['basic_data']['client_id'],
            'contract_id': contract_destiny,
            "flag_id": contract_destiny_data['data']['basic_data']['flag_id'],
            'products_group': edited_product_group,
            'requests_group': delete_requests_group
        }
        print(f'Este json vai editar o contrato para deletar os formulários de pedido.\n{edit_contract}')

        base_requests_group = contract_base_data['data']['requests_group']
        new_requests_group = create_requests_group(base_requests_group)

        edit_contract = {
            "service_type": "exclusive",
            "status": "active",
            'client_id': contract_destiny_data['data']['basic_data']['client_id'],
            'contract_id': contract_destiny,
            "flag_id": contract_destiny_data['data']['basic_data']['flag_id'],
            'products_group': edited_product_group,
            'requests_group': new_requests_group
        }
        print(f'Este json vai atualizar o contrato e inserir os formulários de pedido.\n{edit_contract}')

        return edit_contract
    except



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


def edit_product_group(product_group):
    products_group = []

    for group in product_group:
        new_group = {
            'id': group['id'],
            'control': 'edit',
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
            'product_id': information['products_id'],
            'product_code': information['product_code'],
            'product_order': information['order']
        }
        request_products.append(new_products)
    return request_products


def create_contract(new_contract):
    url = 'https://app.dysrup.com.br/api/v1/web/contract/create'
    response = requests.post(url, headers=headers, json=new_contract)
    status_create = response.json()
    print(status_create)


while True:
    consult_contracts()
    user = str(input('Continuar? '))
    if user in 'Nn':
        break
