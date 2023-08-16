import utils.utilsFunctions
import requests


def consulta_produtos(product_data):
headers = utils.utilsFunctions.token_dysrup()
product_json = product_data
url = 'https://app.dysrup.com.br/api/v1/web/product/get'
response = requests.get(url,headers=headers,json=product_json)
print(response.content)