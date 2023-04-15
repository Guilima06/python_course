import requests
import utilsFunctions
import json


login = 'https://app.dysrup.com.br/api/v1/login'
response= requests.post(login, json={
  "username": "administrador@dysrup.com.br",
  "password": "Dysrup@BH2023",
  "type": "web",
  "employer_code": "SMBH",
})
binario_get = response.content.decode('utf-8')

# converter em objeto dicionário
dicionario = json.loads(binario_get)

token = dicionario['data']['token']['access_token']
# print(token)

headers = {'Authorization': f'Bearer {token}'}


excel_data = utilsFunctions.read_excel()
print(excel_data.columns)
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

# print(response.content)