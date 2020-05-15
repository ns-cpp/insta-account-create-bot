from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from isimler import rasgele_ad_soyad
from random import randint
#from fakemail import rasgele_posta
#import proxy






driver = webdriver.Chrome()
driver.get("https://www.fakemail.net")

sleep(1)

eposta = driver.find_element_by_id('email')
rasgeleposta = eposta.text


driver = webdriver.Chrome()
driver.get("https://instagram.com")
