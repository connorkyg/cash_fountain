import os
import time
import requests
import random
from selenium.webdriver.common.by import By

from Tistory.config import chrome
from Tistory.config import secrets


def random_sleep(num1, num2):
    return time.sleep(random.sample(range(num1, num2), 1)[0])


class tistory(chrome.browser):
    driver = chrome.browser().driver

    def login(self):
        url = 'https://www.tistory.com/auth/login'
        self.driver.get(url)
        if self.driver.find_element(By.CLASS_NAME, 'txt_login'):
            self.driver.find_element(By.CLASS_NAME, 'txt_login').click()
            self.driver.find_element(By.XPATH, '//*[@id="input-loginKey"]').send_keys(secrets.LOGIN_INFO['ID'])
            pw = input("PW 입력: ")
            self.driver.find_element(By.XPATH, '//*[@id="input-password"]').send_keys(pw)
            random_sleep(2, 5)
            self.driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/div/form/div[4]/button[1]').click()
            # return self.driver
        else:
            pass
            # return self.driver

    def get_auth(self):
        auth_code = data_info()

        auth_code.domain = 'https://www.tistory.com/oauth/authorize'
        auth_code.url = auth_code.domain + '?client_id=' + secrets.API_KEY['TISTORY_APP_ID'] + '&redirect_uri=' + \
                        secrets.BLOG_INFO['redirect_uri'] + '&response_type=code'

        auth_code.path = f'./authorization_code_{secrets.BLOG_INFO["BLOG_NAME"]}.txt'
        if os.path.isfile(auth_code.path):
            with open(auth_code.path, 'r', encoding='utf-8') as f:
                code = f.read()
            return code
        elif not os.path.isfile(auth_code.path):
            self.login()
            random_sleep(1, 2)
            self.driver.get(auth_code.url)
            random_sleep(1, 2)
            self.driver.find_element(By.XPATH, '//*[@id="contents"]/div[4]/button[1]').click()
            current_url = self.driver.current_url
            random_sleep(1, 2)
            if 'error' in current_url:
                print("error while getting \'get_auth_url\'")
            random_sleep(2, 5)
            code = current_url.split('=')[1].split('&')[0]
            with open(auth_code.path, 'w+', encoding='utf-8') as f:
                f.write(code)
            return code

    def get_access_token(self):
        USER_AGENT = chrome.browser().USER_AGENT
        access_token = data_info()
        access_token.url = 'https://www.tistory.com/oauth/access_token'
        access_token.path = f'./access_token_{secrets.BLOG_INFO["BLOG_NAME"]}.txt'
        auth_code = self.get_auth()

        if os.path.isfile(access_token.path):
            with open(access_token.path, 'r', encoding='utf-8') as f:
                return f.read()
        elif not os.path.isfile(access_token.path):
            params = {
                'client_id': secrets.API_KEY['TISTORY_APP_ID'],
                'client_secret': secrets.API_KEY['TISTORY_SECRET_KEY'],
                'redirect_uri': secrets.BLOG_INFO['redirect_uri'],
                'code': f'{auth_code}',
                'grant_type': 'authorization_code'
            }
            # Access-Token 발급
            request = requests.get(access_token.url, params=params,
                                   headers={'Accept': 'application/xml; charset=utf-8', 'User-Agent': USER_AGENT})
            if 'error' in request.text:
                print(request.text)
                exit()
            token = request.text.split('=')[1]
            with open(access_token.path, 'w+', encoding='utf-8') as f:
                f.write(token)
            return token


class data_info:
    def __init__(self):
        self.path = None
        self.domain = None
        self.url = None
