from bs4 import BeautifulSoup
from utils import utilsFunctions
import pandas as pd

store_list = []

with open('Lojas atacadao.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    soup = BeautifulSoup(content, 'html.parser')
    card_list = soup.find_all(class_='StoresList_card__NvxZ_')
    for card in card_list:
        name = card.find(class_='StoresList_name__milVs').text
        address = card.find_all(class_='_JuwhE _noMHa')[1].text
        city = card.find_all(class_='_JuwhE _noMHa')[2].text
        store_info = {
            'Loja': name,
            'Endereço': address,
            'Cidade/Estado': city
        }
        store_list.append(store_info)
print(store_list)

store_list_data = pd.DataFrame(store_list)
utilsFunctions.save_excel(store_list_data)