import requests
from utils import utilsFunctions
import json

headers = utilsFunctions.token_dysrup()

excel_data = utilsFunctions.read_excel()
users_ids = (excel_data['user_id'])
users_pass = (excel_data['Senha'])
stores = (list(zip(users_ids, users_pass)))

for (user_id, password) in stores:
    change_password = {
      "user_id": user_id,
      "password": password,
      "confirm_password": password
    }
    url = 'https://app.dysrup.com.br/api/v1/change_password'
    response = requests.post(url, headers=headers, json=change_password)
