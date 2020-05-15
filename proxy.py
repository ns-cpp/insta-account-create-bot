import requests

proxiler = {
    "https": "185.25.116.69:8080",
    "http": "185.25.116.69:8080"
}

url = "http://httpbin.org/ip"
r = requests.get(url, proxies=proxiler)
r.json()
print(r.json())
