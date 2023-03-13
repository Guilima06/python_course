from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('http://www.google.com')
assert 'Google' in browser.title

elem = browser.find_element(By.NAME, 'q')  # Find the search box
search = str(input('Insira o endereço: '))
elem.send_keys(search + Keys.RETURN)
address = browser.find_element(By.CLASS_NAME, )