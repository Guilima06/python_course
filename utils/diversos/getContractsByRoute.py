import requests
from utils import utilsFunctions
import pandas as pd

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIyIiwianRpIjoiNDY5YjI3ODQzMjhmYzExZmI0NjYyZDY1MDliYzY3MzdjZjkyMGRiNmY0ODMxMThlYmY0MmVjNzVhYzFkYjdmMGZjMTA2ZjQyNTcwZDY0MGQiLCJpYXQiOjE2OTU3NjE0NTUuNDc2MDA4LCJuYmYiOjE2OTU3NjE0NTUuNDc2MDEsImV4cCI6MTcwMzUzNzQ1NS40NzAwMDIsInN1YiI6IjEwNjkiLCJzY29wZXMiOltdfQ.GHe78gPaJM736Laty_mfHhojohcaA3kc6upOm8eFOp3z2UDA_b8qfwZ1ymkHGrpRYdSspKmooKQaFfs3X_uVczkkO1yIvG3IdZRfA7yiMdRMnw2rv2s1E3QmRLLgxga37mhWDbHlCxbuWapOQ9cckcoIB7innAWYoGTBte9nWKQ8iiQxecXHYBUYoGMNWQWlJRVFG24wIJpnaFDMOnq8vygRum6sERq94W_V5cVWixUf3ZDyz1Q8bdtoD01jP6hficixBq0JGAK0aA6JWAd7VXB9Vw1gkTNwBvyCyrQW0oRZD-1JKQGOi5yq-npf0FDv_suuksgXOeStJRdS9toEGwsScon031lqKaG-BO1uYwRMfX2JunDkza77guSnAx0alt82TwXZb8hGmqdYt8EaPYWU6mPFUSIjIKf1ORBOd5hghhVmMUeEMQQGzR9SvcnOruSUexxTbtLHMmmzivGy2TbqrrnEBjJoIIzNSVCXhZaTMf6tn2WCJVzizZwFD0Yh8ZXindTejLEr1oW-Sp7TQyY_rLTrY3BqJIHY2s8GHoDdIAXSxrXV3i_9Lg6iAGgeQO2l7OlUyGkkxLd_9HM5Xg05kxCI5JLoP8ikTl97yWd6ysMJaT-rYw6TWvFojjElUz8UVRnCto8rHVwmdbHWK9pkHhqYQfLMui0fiYa2BLo"
headers = {'Authorization': f'Bearer {token}'}


def relatorio():
    clients = get_clients()
    stores = get_stores()
    users = get_users()

    ids_clients = list(map(lambda x: x.get('clients_id'), clients))
    contracts_param = {
        'clients_id': ids_clients,
        'status': 'active'
    }
    contracts = get_contracts(contracts_param)
    # contracts_per_client = clients_conctracts(clients, contracts)

    analyze_routes(contracts, stores, users)
    # print(itf)
    # get_contracts_by_store_id()



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


#
def get_contracts(contracts_json):
    url = 'https://app.dysrup.com.br/api/v1/web/contract/filter'
    response = requests.post(url, headers=headers, json=contracts_json)
    contracts_response = response.json()
    # print(contracts_response)
    return contracts_response


def get_stores():
    url = 'https://app.dysrup.com.br/api/v1/web/store/filter'
    response = requests.post(url, headers=headers)

    stores_response = response.json()
    stores_json = []

    for store in stores_response['data']:
        store_id = store['store_id']
        store_name = store['store_name']
        store_data = {
            'store_id': store_id,
            'store_name': store_name
        }
        stores_json.append(store_data)
    return stores_json


def get_users():
    url = 'https://app.dysrup.com.br/api/v1/web/repositor/filter'
    response = requests.post(url, headers=headers)

    users_response = response.json()
    users_json = []

    for user in users_response['data']:
        user_id = user['user_id']
        user_name = user['name']
        user_data = {
            'user_id': user_id,
            'user_name': user_name
        }
        users_json.append(user_data)
    return users_json



def clients_conctracts(clients, contracts):
    contracts_per_client =[]
    for client in clients:
        contracts_ids = []
        client_name = client['client_name']
        # print(client_name)
        for contract in contracts['data']:
            client_name_contract = contract['client_name']
            contract_id = contract['contract_id']
            if client_name == client_name_contract:
                contracts_ids.append(contract_id)
                # print(f'Esse é o nome do cliente {client_name_contract}')
        client_contract_list = {
            'client_name': client_name,
            'contracts': contracts_ids
        }
        contracts_per_client.append(client_contract_list)
    # print(contracts_per_client)
    return contracts_per_client




def get_list_itineraries():
    itinerary_params = {
        'status': 'active'
    }
    url = 'https://app.dysrup.com.br/api/v1/web/itinerary/filter'
    response = requests.post(url, headers=headers, json=itinerary_params)

    itinerary_response = response.json()
    # print(itinerary_response)
    return itinerary_response


def get_itineraries_informations(itinerary_id):
    itinerary_params = {
        'itinerary_id': itinerary_id
    }
    url = 'https://app.dysrup.com.br/api/v1/web/itinerary/get'
    response = requests.post(url, headers=headers, json=itinerary_params)
    itinerary_informations_response = response.json()
    # print(itinerary_informations_response)
    return itinerary_informations_response


def get_contracts_in_itinerary_per_client(ids_itineraries, contracts_per_client):
    itinerary_information = get_itineraries_informations(ids_itineraries)
    # print(contracts_per_client)
    client_and_contract_list = []
    for client in contracts_per_client:
        list_contracts = []
        client_name = client['client_name']
        contract_list = client['contracts']
        for contract in contract_list:
            for contract_itinerary in itinerary_information['data']['contracts']:
                if contract == contract_itinerary:
                    list_contracts.append(contract)
        clients_contracts_in_itinerary = {
            'client_name': client_name,
            'contracts_ids': list_contracts
        }
        client_and_contract_list.append(clients_contracts_in_itinerary)
    return client_and_contract_list


def get_contracts_in_itinerary(itinerary_informations):
    contracts_in_itinerary = []
    for contract_itinerary in itinerary_informations['data']['contracts']:
        # print(contract_itinerary)
        contracts_in_itinerary.append(contract_itinerary)
    return contracts_in_itinerary


def analyze_routes(contracts, stores, users):
    itinerary_details = []
    itineraries = get_list_itineraries()
    ids_itineraries = list(map(lambda x: x.get('itinerary_id'), itineraries['data']))
    for itinerary in ids_itineraries:
        itinerary_informations = get_itineraries_informations(itinerary)
        roteiro = itinerary_informations['data']['description']
        print(f'Analisando roteiro {roteiro}')
        contracts_in_itinerary = get_contracts_in_itinerary(itinerary_informations)
        # contracts_in_itinerary_per_client = get_contracts_in_itinerary_per_client(itinerary, contracts_per_client)
        route_list = []
        for route in itinerary_informations['data']['routes']:
            route_information = route
            route_list.append(route_information)

        for row in route_list:
            repositor_id = row['repositor_id']
            user_information = get_user_information(repositor_id, users)
            row_number = row['row']
            route_number = str(row_number)
            print(f'Analisando rota {row_number}')
            route_days = row['days']
            for day, ids in route_days.items():
                print(f'Analisando o dia {day}')
                for id in ids:
                    store_id = id
                    store_information = get_store_information(store_id, stores)
                    print(f'Analisando a loja {store_information}')
                    params = {
                        'store_id': id,
                        'contract_ids': contracts_in_itinerary
                    }
                    contracts_by_store = get_contracts_by_store_id(params)
                    contracts_information = format_contracts_by_store(contracts_by_store, contracts)
                    params_selecteds = {
                        'day': day,
                        'route_number': route_number,
                        'store_id': store_id,
                        'contracts_id': contracts_information,
                        'itinerary_id': itinerary
                    }
                    selected_contracts = get_selected_contracts_by_route(params_selecteds)

                    if len(selected_contracts['data']) == 0:
                        selected_contracts_data = format_contracts_by_store(contracts_by_store, contracts)
                        selected_contracts_name = get_contracts_name(selected_contracts_data, contracts)
                        details = {
                            'Roteiro': roteiro,
                            'Loja': store_information,
                            'dia da semana': day,
                            'Promotor': user_information,
                            'Contratos selecionados': selected_contracts_name
                        }
                        itinerary_details.append(details)
                        print(details)
                    else:
                        selected_contracts_data = format_contracts_by_store(selected_contracts['data'], contracts)
                        selected_contracts_name = get_contracts_name(selected_contracts_data, contracts)
                        details = {
                            'Roteiro': roteiro,
                            'Loja': store_information,
                            'dia da semana': day,
                            'Promotor': user_information,
                            'Contratos selecionados': selected_contracts_name
                        }
                        print(details)
                        itinerary_details.append(details)
    relatorio_contratos = pd.DataFrame(itinerary_details)
    relatorio_contratos.to_excel('Relatório contratos.xlsx')









def get_contracts_by_store_id(store_params):
    url = 'https://app.dysrup.com.br/api/v1/web/itinerary/get_contracts_by_store_id'
    response = requests.post(url, headers=headers, json=store_params)
    contracts_by_store = response.json()
    # print(contracts_by_store)
    contracts_id = []
    for contract in contracts_by_store['data']['store_contracts']:
        contract_id = contract['id']
        contracts_id.append(contract_id)
    # print(contracts_id)
    return contracts_id


def get_selected_contracts_by_route(params):
    url = 'https://app.dysrup.com.br/api/v1/web/itinerary/get_selected_contracts_by_route'
    response = requests.post(url, headers=headers, json=params)
    selected_contracts_by_route = response.json()
    return selected_contracts_by_route


def get_user_information(user_id, users):
    for user in users:
        if user['user_id'] == user_id:
            return user['user_name']


def get_store_information(store_id, stores):
    for store in stores:
        if store['store_id'] == store_id:
            return store['store_name']


def get_client_information(search_client):
    url = 'https://app.dysrup.com.br/api/v1/web/client/get'
    response = requests.post(url, headers=headers, json=search_client)
    client_information = response.json()
    # print(client_information)
    return client_information


def format_contracts_by_store(contracts_by_store, contracts):
    contracts_id = []
    contract_name = ''
    for contract in contracts_by_store:
        for contract_data in contracts['data']:
            if contract == contract_data['contract_id']:
                client_name = contract_data['client_name']
                flag_name = contract_data['flag_name']
                service_type = contract_data['service_type']
                if service_type == 'shared':
                    contract_name = client_name + ' - ' + flag_name + ' - ' + 'Compartilhado'
                elif service_type == 'exclusive':
                    contract_name = client_name + ' - ' + flag_name + ' - ' + 'Exclusivo'
                contract_id = {
                    'id': contract,
                    'name': contract_name
                }
                contracts_id.append(contract_id)
    return contracts_id


def get_contracts_name(contracts_information, contracts):
    list_contracts_name = []
    for contract in contracts_information:
        name = contract['name']
        list_contracts_name.append(name)
    return list_contracts_name



relatorio()
