import time

import requests
from utils import utilsFunctions
import pandas as pd

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIyIiwianRpIjoiM2U2YjI2MTRjOTJmYTcyYzZmMmZiNDlhMjhmNmQwZDExY2IyZWRhMjQzMWM2ZWFiNDgyYjExNjcwM2M4MTJhYzgwOTk4YjFmYjEyZGUzOWUiLCJpYXQiOjE3MDQ3NjgxMjguMTIwNjM5LCJuYmYiOjE3MDQ3NjgxMjguMTIwNjQyLCJleHAiOjE3MTI1NDQxMjguMTE1MDgyLCJzdWIiOiIxNiIsInNjb3BlcyI6W119.Epf9h8Vhcp3LZIEYyDUdMjmX5aZjOQgU8m8vegQzGCjv1l1k-lGQFd0_WiiOsyXHXW9VTq__eaK1dEhRogRMu9TkCkc3iSKzP1EeGZxUbGFx4Te2POKSm2_iQPDJ2um-puuVm44GIn4MhKA-bVilv_b8O9CNWFTITZcBKZCyB3pd8Sm9PzbEL0lpagi-Bes2ixdQZkZU_-Wu-HvXoAdG3CpUjKO-0PCg5IKczkwrrz8E066F9jLopsx00zQw63vN1_0N8r_D-7Ii5NiJsX-2T0d-rVGYFAqcD_3kOaLRDgA9ugRAbW8vysPzpejManjehhn50JycRa7MOj8gYU0EMCxsvdA_D1KJzl-ojN2nR22bD7xz6KAN4acnpInaxRUGjLL0kjcEKIEaabXQ2vTSAvaSi0dp7131th4XFeC-lRdjGPlU7Wq7YykK0BEir0csjtZemI7IP4mcDZhKFco7voL0UaMZU5E9EMf8G8XfQ_yKwfjBKfGkD-BxV_8EDoArM_W2yr74DJq5vp1HI7FjxVaRqbfx0GlzkF-5fRNJLTpBvzoVUVfQyBt_UL6y4l_9heLILZpB9VjRtOnd9fNX5QCezZJVSrwGlHKSdrhZv8-b72ymJDv7lua_pzxomq1gUhUfKijktdSuPF-gccqOzHtO7L5RdMUusPBYXdvJMlA"
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
    edited_product_group = delete_product_group(contract_product_group)
    print(edited_product_group)

    request_group = contract_destiny_data['data']['requests_group']
    delete_requests_group = []

    if len(request_group) != 0:
        for group in request_group:
            requests_group_data = {
                'id': group['id'],
                'control': 'del',
                'product': []
            }
            delete_requests_group.append(requests_group_data)

        edit_contract = {
            "service_type": "exclusive",
            "status": "active",
            'client_id': contract_destiny_data['data']['basic_data']['client_id'],
            'contract_id': contract_destiny,
            "flag_id": contract_destiny_data['data']['basic_data']['flag_id'],
            'products_group': edited_product_group,
            'requests_group': delete_requests_group
        }
        print(f'Edição do contrato removendo mix e pedidos\n{edit_contract}\n')
        create_contract(edit_contract)
        # time.sleep(5)
    else:
        print('A lista de formulários estava vazia')

    base_product_group = contract_base_data['data']['products_group']
    new_products_group = create_product_group(base_product_group)

    base_requests_group = contract_base_data['data']['requests_group']
    new_requests_group = create_requests_group(base_requests_group)

    edit_contract = {
        "service_type": "exclusive",
        "status": "active",
        'client_id': contract_destiny_data['data']['basic_data']['client_id'],
        'contract_id': contract_destiny,
        "flag_id": contract_destiny_data['data']['basic_data']['flag_id'],
        'products_group': new_products_group,
        'requests_group': new_requests_group
    }
    print(f'Este json vai atualizar o contrato e inserir o mix e os formulários de pedido.\n{edit_contract}\n')
    create_contract(edit_contract)

    return edit_contract


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


def delete_product_group(product_group):
    products_group = []

    for group in product_group:
        new_group = {
            'id': group['id'],
            'control': 'del',
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
