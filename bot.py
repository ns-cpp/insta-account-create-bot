from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from isimler import rasgelead, rasgelesoyad
import random
#import proxy

#PROXY = "96.44.183.149:55225" 

#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--proxy-server=%s' % PROXY)

#driver = webdriver.Chrome(options=chrome_options)
#driver.get("http://httpbin.org/ip")
#time.sleep(2)

driver = webdriver.Chrome()




driver.get("https://www.fakemail.net")

time.sleep(1)

eposta = driver.find_element_by_id('email')

rasgeleposta = eposta.text

driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')


url = "https://www.instagram.com/accounts/emailsignup/"

driver.get(url)

time.sleep(4)

email = driver.find_element_by_name("emailOrPhone")
adsoyad = driver.find_element_by_name("fullName")
kullaniciadi = driver.find_element_by_name("username")
sifre = driver.find_element_by_name("password")


#time.sleep(2)

email.send_keys(rasgeleposta)


rastgelead = rasgelead
satgelesoyad = rasgelesoyad
adsoyad.send_keys(rastgelead , " ",rasgelesoyad)


alfabe = ["a","b","c","d","e","f","g","h","i","j","k","l","n","m","o","p","r","s","t","y","z"]
sayi = random.randint(0,1000)
rastgeleid = str(alfabe[random.randint(0,20)]) + str(alfabe[random.randint(0,20)]) + str(alfabe[random.randint(0,20)]) + str(alfabe[random.randint(0,20)]) + str(alfabe[random.randint(0,20)]) + str(alfabe[random.randint(0,20)]) + str(alfabe[random.randint(0,20)]) + str(alfabe[random.randint(0,20)]) + str(alfabe[random.randint(0,20)]) + str(alfabe[random.randint(0,20)]) + str(sayi)
kullaniciadi.send_keys(rastgeleid)



sifresonu = random.randint(0,1000)
sifresonuyazi = str(sifresonu)
rasgelesifre = rastgelead + rasgelesoyad + sifresonuyazi
sifre.send_keys(rasgelesifre)
sifre.send_keys(Keys.ENTER)



with open("hesaplar.txt", "a", encoding="utf-8") as f:
    
    f.write("[")
    f.write(rasgeleposta)
    f.write("]")
    f.write(" ")
    f.write("[")
    f.write(rasgelesifre)
    f.write("]")
    f.write("\n")
    f.close()

time.sleep(3)
driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[22]").click()
driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/div[5]/div[2]/button").click()