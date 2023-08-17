import requests
from utils import utilsFunctions

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIyIiwianRpIjoiNmVlMWVjNzkzNWY2NzJjMWQzODRiMzU2ODllY2Y3ZmMxNWY4NzljZDIyMDc5NDFjOGRjZWU2YTg2OGM3NTIwNzI2NWI5ZGM5ZmIyMTM0NjAiLCJpYXQiOjE2OTIyODMzOTUuMTkwMTgsIm5iZiI6MTY5MjI4MzM5NS4xOTAxODIsImV4cCI6MTcwMDA1OTM5NS4xODEzNDEsInN1YiI6IjIxMjUiLCJzY29wZXMiOltdfQ.pgaPYlCgmu6bS-kUlqkOFguc62vWlmEsVOYJGfx261cphM5CAfw7uVIhbm_dgRqvqHfaST2u7yFf57DuHpFreveXwkICi7GYR_EG0AQgvHWbyDYmjB_QM3Tx1QeVDt9_IvplRQ-H5Anp2Zj2mQksgz6sizLcxx7GyEYEPzk4cCXZ5yeC6U4vtN_9TEbzOU3LFO7H6XBj2gAFN2RiwRvCx3_9hO9pakCnnbMFUtDIHCPN8UEr6M7Di82Gz9JNrR_epzbOXTR1k_eZVKX79kdnYUXqEy7mjtZ4Cj3UqK4TJ4E8Tykh0C1xDNOb8MvJ309BLBWaXo6vB43FldY6TSzcyLV2o6lUwMxUvx_WZYszD8r5R-PS4d4DX-XuXLBFVgptM5v4LGihAVLkPedmcjMJSrA6Q3T8q3IJEzOMGc4khglEZFV1SUS90XyKsBLPSNBWTWFXx7XDyPW7oQ1g08xsv1Q086MK_Zwluh327XyREuV6784ZH6uPv84ceSd2zS1zQmnjtJTZwevW0riTNDPHTgGFtyYgTUSsPlA4P6LEFRMEhZiP2T85ESh1lDGlDQz2RtmbQ6W5MR_LS9gqKdXT-ptu-I4oiON7mijxUlBowpFWldoeHLC9jmHILixMO6MeZ8DviYzENN72H5JR53xI1Ps8FpkQ0mp2MxzK8X7D7X8"
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

    analyze_routes(contracts_per_client)
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



def analyze_routes(contracts_per_client):
    itineraries = get_list_itineraries()
    ids_itineraries = list(map(lambda x: x.get('itinerary_id'), itineraries['data']))
    for itinerary in ids_itineraries:
        itinerary_informations = get_itineraries_informations(itinerary)
        contracts_in_itinerary = get_contracts_in_itinerary(itinerary_informations)
        # contracts_in_itinerary_per_client = get_contracts_in_itinerary_per_client(itinerary, contracts_per_client)
        route_list = []
        for route in itinerary_informations['data']['routes']:
            route_information = route
            route_list.append(route_information)

        for row in route_list:
            repositor_id = row['repositor_id']
            row_number = row['row']
            route_number = str(row_number)
            # print(route_number)
            route_days = row['days']
            for day, ids in route_days.items():
                day = day
                for id in ids:
                    store_id = id
                    params = {
                        'store_id': store_id,
                        'contract_ids': contracts_in_itinerary
                    }
                    contracts_by_store = get_contracts_by_store_id(params)
                    params_selecteds = {
                        'day': day,
                        'route_number': route_number,
                        'store_id': store_id,
                        'contracts_id': contracts_by_store,
                        'itinerary_id': itinerary
                    }
                    print(params_selecteds)
                    selected_contracts = get_selected_contracts_by_route(params_selecteds)
                    # print(selected_contracts)







def get_contracts_by_store_id(store_params):
    url = 'https://app.dysrup.com.br/api/v1/web/itinerary/get_contracts_by_store_id'
    response = requests.post(url, headers=headers, json=store_params)
    contracts_by_store = response.json()
    print(contracts_by_store)
    contracts_id = []
    for contract in contracts_by_store['data']['store_contracts']:
        contract_id = contract['id']
        contracts_id.append(contract_id)
    print(contracts_id)
    return contracts_id


def get_selected_contracts_by_route(params):
    url = 'https://app.dysrup.com.br/api/v1/web/itinerary/get_selected_contracts_by_route'
    response = requests.post(url, headers=headers, json=params)
    selected_contracts_by_route = response.json()
    print(selected_contracts_by_route)



relatorio()
