from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.fakemail.net")

sleep(1)

eposta = driver.find_element_by_id('email')
rasgele_posta = eposta.text

driver.close()