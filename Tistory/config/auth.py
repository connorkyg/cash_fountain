import requests
from Tistory.config import secrets
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import os
import random

path_auth_code = f'./authorization_code_{secrets.BLOG_INFO["BLOG_NAME"]}.txt'
path_access_token = f'./access_token_{secrets.BLOG_INFO["BLOG_NAME"]}.txt'

def random_sleep():
    return time.sleep(random.sample(range(2, 5), 1)[0])


def get_access_token():
    if not os.path.isfile(path_auth_code):
        with open(path_auth_code, 'w', encoding='utf-8') as f:
            USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
            # Authentication code 발급
            # authentication code 허가하기 페이지 접속 -> 허가하기 -> authentication code 저장
            get_auth_domain = 'https://www.tistory.com/oauth/authorize'
            url_login = 'https://www.tistory.com/auth/login'
            get_auth_url = get_auth_domain + '?client_id=' + secrets.API_KEY[
                'TISTORY_APP_ID'] + '&redirect_uri=' + secrets.BLOG_INFO['redirect_uri'] + '&response_type=code'

            options = webdriver.ChromeOptions()
            options.add_argument(f'user-agent={USER_AGENT}')
            options.add_argument("lang=ko_KR")
            path = r"D:/Development/Python/Coupang Partners/utils/chromedriver.exe"
            # driver = webdriver.Chrome(service=Service(path), options=options)
            with webdriver.Chrome(service=Service(path), options=options) as driver:
                driver.get(url_login)
                driver.find_element(By.CLASS_NAME, 'txt_login').click()
                driver.find_element(By.XPATH, '//*[@id="input-loginKey"]').send_keys(secrets.LOGIN_INFO['ID'])
                driver.find_element(By.XPATH, '//*[@id="input-password"]').send_keys(secrets.LOGIN_INFO['PW'])
                random_sleep()
                driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/div/form/div[4]/button[1]').click()
                random_sleep()
                driver.get(get_auth_url)
                random_sleep()
                driver.find_element(By.XPATH, '//*[@id="contents"]/div[4]/button[1]').click()
                random_sleep()

                auth_code = driver.current_url.split('=')[1].split('&')[0]
                print(f'Authorization code: {auth_code}')
                f.write(auth_code)
    else:
        print("Auth code exists")
        with open(path_auth_code, 'r', encoding='utf-8') as f:
            auth_code = f.read()
    # todo: 마지막 실행일시로부터 1시간 경과 시 auth_code 재발급 코드 작성

    if not os.path.isfile(path_access_token):
        access_token_url = 'https://www.tistory.com/oauth/access_token'
        get_access_token_params = {
            'client_id': secrets.API_KEY['TISTORY_APP_ID'],
            'client_secret': secrets.API_KEY['TISTORY_SECRET_KEY'],
            'redirect_uri': secrets.BLOG_INFO['redirect_uri'],
            'code': f'{auth_code}',
            'grant_type': 'authorization_code'
        }

        # Access-Token 발급
        req_access_token = requests.get(access_token_url, params=get_access_token_params,
                                        headers={'Accept': 'application/xml; charset=utf-8', 'User-Agent': USER_AGENT})
        token_tmp = req_access_token.text
        access_token = token_tmp.split('=')[1]
        print(f'Access-Token: {access_token}')
    else:
        print("Access code exists")
        with open(path_access_token, 'r', encoding='utf-8') as f:
            access_token = f.read()
            
    return access_token
