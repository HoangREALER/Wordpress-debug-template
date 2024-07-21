import requests
import urllib3
from urllib.parse import urlencode

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


url = "http://127.0.0.1:8181"
HTTP_CONFIG = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080",
}

session = requests.Session()
session.verify = False
session.proxies = HTTP_CONFIG
session.allow_redirects = True

def pushs():
    api = "/wp-json/instawp-connect/v3/push"
    query = ""
    body = ""
    if query:
        api += "?" + urlencode(query)

    r = request."post"(url + api, data=body)
