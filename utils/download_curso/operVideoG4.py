import json
import os
import pickle
from selenium import webdriver
from utils import  utilsFunctions

def get_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--auto-open-devtools-for-tabs')
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)

    url = 'https://online.g4educacao.com/'
    driver.get(url)

    driver.delete_all_cookies()

    cookies = pickle.load(open("cookie", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)

    # visit again and you shall see your account logged in
    url = 'https://online.g4educacao.com/bundle/g4-pass'
    driver.get(url)
    return driver


def facilitate(json_path):
    driver = get_driver()
    original_json_filename = json_path.split('.json')[0]
    with open(json_path) as f:
        data = json.load(f)
        modules = data.get('modulos')
        if modules is not None:
            for module in modules:
                for key, value in module.items():
                    if key != 'lista_videos':
                        print(f'{key}: {value}')
                    else:
                        for video in value:
                            for k, v in video.items():
                                print(f'\t{k}: {v}')
                            driver.get(video['url_video'])
                            vimeo_url = input('\tINSIRA A URL DO VIMEO: ')
                            video['url_video_vimeo'] = vimeo_url
                            with open(f'{original_json_filename}_copy.json', 'w') as copy_json:
                                json.dump(data, copy_json, indent=4)
                            print('-=' * 20)

    with open(f'{original_json_filename}_copy.json') as f:
        data = json.load(f)

        with open(json_path, 'w') as final_json:
            json.dump(data, final_json, indent=4)

    os.remove(f'{original_json_filename}_copy.json')
    driver.close()



from selenium import webdriver

def save_cookie(driver, path):
    with open(path, 'wb') as filehandler:
        pickle.dump(driver.get_cookies(), filehandler)


# driver = webdriver.Chrome()
# driver.get('https://online.g4educacao.com/')
# foo = input()
# save_cookie(driver, os.path.join(os.getcwd(), 'cookie'))


facilitate(utilsFunctions.open_file())
