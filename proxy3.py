import requests
from bs4 import BeautifulSoup
import time

url = "https://hidemy.name/en/proxy-list"
time.sleep(10)
html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

list = soup.find("tbody").find_all()

print(list)
time.sleep(10)