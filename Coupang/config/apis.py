# -*- coding: utf-8 -*-
from Coupang.config import secrets
import requests
import json
import os
import hmac
import hashlib
import time

now = time.strftime('%Y%m%d_%H%M%S')

DOMAIN = "https://api-gateway.coupang.com"

def generate_hmac(method, url, secret_key, access_key):
    path, *query = url.split("?")
    dateGMT = time.strftime('%y%m%d', time.gmtime())
    timeGMT = time.strftime('%H%M%S', time.gmtime())
    datetime = dateGMT + 'T' + timeGMT + 'Z'
    message = datetime + method + path + (query[0] if query else "")
    signature = hmac.new(bytes(secret_key, "utf-8"),
                         message.encode("utf-8"),
                         hashlib.sha256).hexdigest()

    return "CEA algorithm=HmacSHA256, access-key={}, signed-date={}, signature={}".format(access_key, datetime, signature)


def get_product(url):
    method = 'GET'
    authorization = generate_hmac(method, url, secrets.API_KEY['COUPANG_SECRET_KEY'], secrets.API_KEY['COUPANG_ACCESS_KEY'])
    coupang_url = '{}{}'.format(DOMAIN, url)
    response = requests.request(method=method, url=coupang_url, headers={"Authorization": authorization, "Content-Type": "application/json"})
    print('API 차감 -1회')
    retdata = json.dumps(response.json(), indent=4).encode('utf-8')
    jsondata = json.loads(retdata)
    data = jsondata['data']
    productdata = data['productData']
    with open(f'./product_data_{now}', 'w+', encoding='utf-8') as f:
        f.write(productdata)

    return productdata
