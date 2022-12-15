# -*- coding: utf-8 -*-
import requests
import json
import urllib.request
import api_config
import get_auth


SECRET_KEY = api_config.API_KEY['COUPANG_SECRET_KEY']
ACCESS_KEY = api_config.API_KEY['COUPANG_ACCESS_KEY']
keyword = '건전지'
METHOD = 'GET'
limit = 10
URL = "/v2/providers/affiliate_open_api/apis/openapi/products/search?keyword=" + urllib.parse.quote(keyword) + "&limit=" + str(limit)
authorization = get_auth.coupang.generate_hmac(METHOD, URL, SECRET_KEY, ACCESS_KEY)  # HMAC 생성
aaa = get_auth.coupang()
# todo: class를 초기화해야하는 이유?
# todo: 초기화는 뭐하는거?
product_data = aaa.get_product(METHOD, URL, authorization)

# FIXME: API 호출을 하지 않기 위해 text to json 하였으나, json 변환이 잘 되지않아 포기함.. - 20221205
# product_data_sample1 = open('./json_sample_data.txt', 'r', encoding='utf-8').readlines()
# product_data_sample2 = json.load(product_data_sample1)
# print(product_data_sample2)
# product_data_sample3 = product_data_sample2['data']

for i in range(limit):
    print(product_data[i]['productName'])