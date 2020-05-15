from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

url = "https://temp-mail.org"

driver.get(url)

time.sleep(6)

eposta = driver.find_element_by_xpath("//*[@id='mail']").click()
eposta.send_keys(Keys.CTRL, Keys.C)




rasgeleposta = eposta

print(rasgeleposta)

time.sleep(2)

driver.quit()
exit()

