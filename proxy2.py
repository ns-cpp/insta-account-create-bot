from selenium import webdriver

PROXY = "128.199.179.225:3128" # IP:PORT or HOST:PORT

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://httpbin.org/ip")

"""
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType

prox = Proxy()
prox.proxy_type = ProxyType.MANUAL
prox.http_proxy = "185.25.116.69:8080"
prox.socks_proxy = "170.238.160.7:4145"
prox.ssl_proxy = "185.25.116.69:8080"

capabilities = webdriver.DesiredCapabilities.CHROME
prox.add_to_capabilities(capabilities)

driver = webdriver.Chrome(desired_capabilities=capabilities)
"""

"""
from selenium import webdriver
browser = webdriver.Chrome(executable_path='ChromeDriverPath', chrome_options=options)
options.add_argument('--proxy-server=46.102.106.37:13228')
options = Options()
"""
