import requests
from utils import utilsFunctions

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIyIiwianRpIjoiZTI5MWFmNjExMWUzNzQyNzFlYTliMTVkYmM2ZmVkOTA5MjU0ZmI3YWNlY2E2ZmQ2YTdiNTIwNzkwZjY2MTg3YTc2ZTNhOTVhYjU3ZjEyYzkiLCJpYXQiOjE2OTIyMDc3NTcuNTEwMjI5LCJuYmYiOjE2OTIyMDc3NTcuNTEwMjMxLCJleHAiOjE2OTk5ODM3NTcuNTAyNjY2LCJzdWIiOiIyMTI1Iiwic2NvcGVzIjpbXX0.g-vl3kQ4lz1hw0QJP-XhqQe4i1TIW0ve56JxbvQazVHILNJ-nalj4KF9rIwGimtGm-5FnBAu2tquuetdSo1XuxX8qnHD61ZVDTgctmbLnYp_5NUyl9ODaEEWzcIC_IY7sIqhXztX9yx0HTshvzH7_qFyOKOuERU2XLdhKElHFt_Baa6Ln55LhM7Br-tMRri3CDo3Jv-tvqV8szg30gKlzlClfXOmB-K8qS6KRWkT4sFHDJH0jD8gGhWPr7i5MOWp1hFgGFfTElLr_a8Dr2KX3FoCH91401bpo7jr13Hn_PCSUq3k_vezCkgdcJJVoYXI15lpl_P5fpFBu-kOWnnqqWoHkxj47wwbYDFFvxQDgvIDVyb-tMz1zkpe6pI2RugGqQje79f9iUj70Z2ubmIiszuiTF-FgA9DTex2qeFxFS0u4j9beIfhJKIhLYFETyGN_OAtBDfyt_08jv8sRz3Qfo2ferQBHI7FB4y6Pjb4IUj54trhp2zxaIgxy35rKwypAekhV9sGjBNBxkq4i5j21-b_ZMeR03BvgCsul7EDXo86daIsOospdD18MZwp_KuP_XqqsqOgP3nWtD1w9MeziBJNWZf3crthtKpi44c3I9wF6jPWR7ckOdrlp9zMzvFhLrdyHMMTVDf4xqfnuQ2TowqNsFdLOV3tD7YWglKfzMs"
headers = {'Authorization': f'Bearer {token}'}


def relatorio():
    clients = get_clients()
    # print(clients)
    ids_clients = list(map(lambda x: x.get('clients_id'), clients))
    contracts_param = {
        'clients_id': ids_clients,
        'status': 'active'
    }
    contracts = get_contracts(contracts_param)
    contracts_per_client = clients_conctracts(clients, contracts)

    # analyze_routes(contracts_per_client)
    # print(itf)
    get_contracts_by_store_id()



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


def analyze_routes(contracts_per_client):
    itineraries = get_list_itineraries()
    ids_itineraries = list(map(lambda x: x.get('itinerary_id'), itineraries['data']))
    for itinerary in ids_itineraries:
        itinerary_id = itinerary
        itinerary_informations = get_itineraries_informations(itinerary)
        contracts_in_itinerary = get_contracts_in_itinerary_per_client(itinerary_id, contracts_per_client)
        route_list = []
        for route in itinerary_informations['data']['routes']:
            route_information = route
            route_list.append(route_information)

        for row in route_list:
            repositor_id = row['repositor_id']
            route_number = row['row']
            route_days = row['days']
            for day, ids in route_days.items():
                day = day
                for id in ids:
                    store_id = id
                    # get_contracts_by_store_id(store_id)







def get_contracts_by_store_id():
    store_params = {
        'store_id': 526
    }
    url = 'https://app.dysrup.com.br/api/v1/web/itinerary/get_contracts_by_store_id'
    response = requests.post(url, headers=headers, json=store_params)
    contracts_by_store = response.json()
    print(contracts_by_store)
    # return contracts_by_store





relatorio()
