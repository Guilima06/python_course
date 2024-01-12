import time

import requests
from utils import utilsFunctions
import pandas as pd

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIyIiwianRpIjoiMDMxMDY1NTk1OWYyMzE3ZTFiMjEwY2Y5MjlhODZkNTFkMzI5MGE5ZTY2NTk1YjBmNzBiNDg5N2NjODUzNWFmMmUyODIyMzUwOTRlODI0ZjEiLCJpYXQiOjE3MDQ5MDgzMTEuMDE5NjA2LCJuYmYiOjE3MDQ5MDgzMTEuMDE5NjA5LCJleHAiOjE3MTI2ODQzMTEuMDEyNzk0LCJzdWIiOiIxMDY5Iiwic2NvcGVzIjpbXX0.DGkQx42OEAqD7qW2aCdQf5QmT6blQtUqq49Wp4VebDgbLZi3AYNGfhot6vMBcIpunKqdUun_WEYIPt4F8uSIf7EV9fMIeFRYUJha-Kh2sw_rDf7xkEokosSc9cCY8EOaMZi_imKkRSoPDQZFoOp3tDsr9yEB-4gf2ZUBYtQnoq7TCVXBWJW2WixJoNzwpUrvOysaqoMGjlDxmc5s13gX9E8m6OfSYie-OSPDq6TJSV1rclApNmEIWQRZ7ZAtcMrHKYPnCqg8BxF6lR3NwogP0wtidwEM3nGku2mJ_ex1OgyKcZGxwFiPn2KMM7OBQHQZroJ1iI80THQWPuRiEb0oZ96wd2gLcwC1m1huvCXcYoEVnRMPlRJiPfi6gwm5FrlmdWvJbZTkQ6Mz8vRPhAtYrz-4K-ph_sF6qWSv1dSQxn7WHgUjv6jqEVluCM31gWekfb3OUuLkMKVpM5ZrTVeC0_Ux7TPWkwuJh_NX5vumiRB_-c3ZdWOQ8q17BddcgLOPp5naupztw1Wthuk2hq86HmfYNYfRMNqmWuMiKop1XwCDyQJQpV2eUiXenfUilZCWQigUCstlzTkv3sK89q0gpA3hlb62qiOYt-q5uwOEW78UIFxjgiEHD3W5zBhmoW0aMyHg6dzPdYe9ZBQO75R9D--N1YEah-9o20kTnA9qdgY"
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


def generate_rel():
    # client = escolher_client()

    parameters = {
        "report_entity": "scheduled_attendances",
        "client_id": 301,
        "preview": True,
        "per_page": '10',
        'page': 1
    }

    url = 'https://app.dysrup.com.br/api/v1/admin/report/generate'
    response = requests.post(url, headers=headers, json=parameters)
    attendances = response.json()
    print(attendances)



# while True:
#     consult_contracts()
#     user = str(input('Continuar? '))
#     if user in 'Nn':
#         break


generate_rel()
