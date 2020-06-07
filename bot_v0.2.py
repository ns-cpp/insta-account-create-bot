from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
#from isimler import rasgele_ad_soyad
from random import randint
#import proxy3
import requests
from bs4 import BeautifulSoup
#from fakemail import rasgele_posta
#import proxy


def isimler():
    adlar = ["Enes" , "Hasan" , "Hüseyin" , "Mete", "Mehmet","Mustafa",
    "Ahmet","Ali","Hüseyin","Hasan","İbrahim","İsmail","Osman","Yusuf","Murat",
    "Ömer","Ramazan","Halil","Süleyman","Abdullah","Mahmut","Recep","Salih","Fatih",
    "Fatma","Ayşe","Emine","Hatice","Zeynep","Elif",
    "Meryem","Şerife","Sultan","Zehra","Hanife","Merve",
    "Havva","Zeliha","Fadime","Esra","Özlem","Hacer","Yasemin","Hülya"]

    rasgelead = adlar[randint(0,43)]

    soyadlar = ["YILMAZ","KAYA","DEMİR","ÇELİK","ŞAHİN","YILDIZ","YILDIRIM","ÖZTÜRK",
    "AYDIN","ÖZDEMİR","ARSLAN","DOĞAN","KILIÇ","ASLAN","ÇETİN", 
    "KARA","KOÇ","KURT","ÖZKAN","ŞİMŞEK","POLAT","ÖZCAN","KORKMAZ","ÇAKIR","ERDOĞAN","YAVUZ",
    "CAN","ACAR","ŞEN","AKTAŞ","GÜLER","YALÇIN","GÜNEŞ","BOZKURT",
    "BULUT","KESKİN","ÜNAL","TURAN","GÜL","ÖZER","IŞIK","KAPLAN",
    "AVCI","SARI","TEKİN""TAŞ","KÖSE","YÜKSEL","ATEŞ","AKSOY"]

    rasgelesoyad = soyadlar[randint(0,48)]  


    rasgele_ad_soyad = rasgelead + " " + rasgelesoyad
    return rasgele_ad_soyad
    

isimlerson = isimler()
print("Seçilen İsim : ", isimlerson)

def proxy33():
    r = requests.get("https://free-proxy-list.net")
    soup = BeautifulSoup(r.content,"html.parser")
    solmenu = soup.find_all("textarea",attrs={"class":"form-control"})

    for game in solmenu:
        #print(game.text)
        with open("ip_ve_portlar.txt", "w") as f:
            f.write(game.text)
            f.close()
    f = open("ip_ve_portlar.txt","r")
    proxylist = f.readlines()
    i = randint(4,300)
    rasgeleproxy = proxylist[i]

    return rasgeleproxy
    






driver1 = webdriver.Chrome()
driver1.get("https://www.fakemail.net")
eposta = driver1.find_element_by_id('email').text




#driver.execute_script("window.open('https://www.fakemail.net');")


#print(ipvemailacma())

def kullidolustur():
    alfabe = ["a","b","c","d","e","f","g","h","i","j","k","l","n","m","o","p","r","s","t","y","z"]
    sayi = randint(0,1000)
    rastgeleid = str(alfabe[randint(0,20)]) + str(alfabe[randint(0,20)]) + str(alfabe[randint(0,20)]) + str(alfabe[randint(0,20)]) + str(alfabe[randint(0,20)]) + str(alfabe[randint(0,20)]) + str(alfabe[randint(0,20)]) + str(alfabe[randint(0,20)]) + str(alfabe[randint(0,20)]) + str(alfabe[randint(0,20)]) + str(sayi)
    return rastgeleid


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % proxy33())

driver2 = webdriver.Chrome(options=chrome_options)
#driver2 = webdriver.Chrome()
driver2.get("http://httpbin.org/ip")
sleep(2)

#driver2 = webdriver.Chrome()
driver2.get("https://www.instagram.com/accounts/emailsignup/")
sleep(4)
email = driver2.find_element_by_name("emailOrPhone")
email.send_keys(eposta)


adsoyad = driver2.find_element_by_name("fullName")
adsoyad.send_keys(isimlerson)

kullid = driver2.find_element_by_name("username")
kullid.send_keys(kullidolustur())

sifre = driver2.find_element_by_name("password")
sifreson = kullidolustur()
sifre.send_keys(sifreson)

driver2.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[7]/div/button').click()

with open("hesaplar.txt", "a", encoding="utf-8") as f:
    
    f.write("[")
    f.write('"')
    f.write(eposta)
    f.write('"')
    f.write(",")
    f.write('"')
    f.write(sifreson)
    f.write('"')
    f.write("]")
    f.write("\n")
    f.close()

sleep(3)
driver2.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[30]').click()


#driver.execute_script("window.open('https://www.instagram.com/accounts/emailsignup/');")






print('Made by "1948boys" co-founder "ns.cpp".')


