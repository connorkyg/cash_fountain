import hmac
import hashlib
import os
import time
import requests
import json
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import secrets
import api_config

# todo: DOMAIN을 get_product() 내에 선언하면, self.DOMAIN 인식을 못함. 왜?
class coupang:
    DOMAIN = "https://api-gateway.coupang.com"

    def generate_hmac(method, url, secret_key, access_key):
        path, *query = url.split("?")
        os.environ["TZ"] = "GMT+0"
        datetime = time.strftime('%y%m%d') + 'T' + time.strftime('%H%M%S') + 'Z'
        message = datetime + method + path + (query[0] if query else "")
        signature = hmac.new(bytes(secret_key, "utf-8"),
                             message.encode("utf-8"),
                             hashlib.sha256).hexdigest()

        return f"CEA algorithm=HmacSHA256, access-key={access_key}, signed-date={datetime}, signature={signature}"

    def get_product(self, request_method, URL, authorization):
        full_url = "{}{}".format(self.DOMAIN, URL)
        response = requests.request(method=request_method, url=full_url, headers={"Authorization": authorization, "Content-Type": "application/json;charset=UTF-8"})
        print('API 차감 -1회')
        retdata = json.dumps(response.json(), indent=4).encode('utf-8')
        jsondata = json.loads(retdata)
        data = jsondata['data']
        productdata = data['productData']

        return productdata