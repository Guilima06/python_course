import requests
from utils import utilsFunctions
import json
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIyIiwianRpIjoiYzk0YWI5MDI0NmZjNzFiNTY5MmVlZWE0MmZjN2U2OWIyODQwZDg1MmFiOTBhNzFiMGViMWU3MDVjMzdhNmQ2NzhhMzVjNjg4OWI5NzI5NTAiLCJpYXQiOjE2OTIxOTQxNzcuMjQ0NjE2LCJuYmYiOjE2OTIxOTQxNzcuMjQ0NjE5LCJleHAiOjE2OTk5NzAxNzcuMjM4NTI3LCJzdWIiOiIxMDY5Iiwic2NvcGVzIjpbXX0.GzFTisCHMxTfe_r3jURrLRH6FnL6FdmLhbkdd7NdJK3xVg_UbBDNv4jmbi4x9s61XR1eKArlo5QrB4aIrCtrtNtc0tmCbP2HP-bNGh9IaQipAY5DWiAK0HGeqwxerHUFaJ_4cYr7SFVv8_Ps8AVIRB76DotZcyrdqmrBzShoGbajpJLq9P7pVxzbBI0N3rPbZTOakyUD0vP8nNk27dxe72bmN9XTUhFPG_c-pxrqsPJKLBcw9wq3_ySUUS8Q8jh7KLuGSIYDq_UTeOOXXTYakW9VfN9kHgCZehrHfbZmUXiljDxXmlbaz8Zj9zTHJ5G64WbHo0Kl2H1AeGBytVEJZ2B21Cor6FEnOAGsIwT9eHfXCKH51pkQJyhFfVfRHLGwkj7mHu2ZUjZQr4An_NX89n8Vwjh9vfVfsmvaOhNZQcGdmdb0p7qDFTTxBqallt0ue0U25yYAFJ3tyHUZrufI5mhSKHR0XsV1JEy7HEG2Df_UzrMAB3_tWmXXeLw5IPauR9M2jJGDIpVYbS4HjjC8ak3ArURSPEi61d9CGpdHH5U0lPAcS13xnlbLehuP-VVEghxhXu9ZZVKGEFadoUTVE7K0AXjV4Y8Vz0TKJW6B2cReMADnppgMIkeZIOvqTPDOO1tOSmkwoDUXV_8FsaqfVZODWS5LpFLofD-qVj7ViM4"
headers = {'Authorization': f'Bearer {token}'}

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
