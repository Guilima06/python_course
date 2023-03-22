from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time


browser = webdriver.Chrome()
site = str('https://sejasocio.samsclub.com.br/#encontre-um-clube')
browser.get(site)
elem = browser.find_element(By.CLASS_NAME, 'units__filter')
print(elem)
time.sleep(5)