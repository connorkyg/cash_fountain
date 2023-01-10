import requests
import time
import os
import random
from Tistory.config import secrets
from Coupang.data import titles
from Coupang.data import tags
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import subprocess

subprocess.Popen(
    r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"')  # 디버거 크롬 구동
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
options = webdriver.ChromeOptions()
options.add_argument(f'user-agent={USER_AGENT}')
options.add_argument("lang=ko_KR")
path = r"D:/Development/Python/Coupang Partners/utils/chromedriver.exe"
driver = webdriver.Chrome(service=Service(path), options=options)
url_login = 'https://www.tistory.com/auth/login'


def random_sleep(self):
    return time.sleep(random.sample(range(2, 5), 1)[0])


class selenium:
    def __init__(self):
        return

    def open_url(self, url):
        self.url = url
        driver.get(self.url)

    def tis_login(self):
        url_login = 'https://www.tistory.com/auth/login'
        self.open_url(url_login)

        driver.get(url_login)
        driver.find_element(By.CLASS_NAME, 'txt_login').click()
        driver.find_element(By.XPATH, '//*[@id="input-loginKey"]').send_keys(secrets.LOGIN_INFO['ID'])
        driver.find_element(By.XPATH, '//*[@id="input-password"]').send_keys(secrets.LOGIN_INFO['PW'])
        random_sleep()
        driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/div/form/div[4]/button[1]').click()
        random_sleep()
        driver.get(get_auth_url)
        print(driver.current_url)
        if 'error' in driver.current_url:
            print("error while getting \'get_auth_url\'")
        random_sleep()
        driver.find_element(By.XPATH, '//*[@id="contents"]/div[4]/button[1]').click()
        random_sleep()

        auth_code = driver.current_url.split('=')[1].split('&')[0]
        print(f'Authorization code: {auth_code}')
        with open(path_auth_code, 'w', encoding='utf-8') as f:
            f.write(auth_code)

    def __exit__(self, exc_type, exc_val, exc_tb):
        driver.quit()

        driver.get(self.url)
        driver.find_element(By.CLASS_NAME, 'txt_login').click()
        driver.find_element(By.XPATH, '//*[@id="input-loginKey"]').send_keys(secrets.LOGIN_INFO['ID'])
        driver.find_element(By.XPATH, '//*[@id="input-password"]').send_keys(secrets.LOGIN_INFO['PW'])

        driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/div/form/div[4]/button[1]').click()

        driver.get(get_auth_url)
        print(driver.current_url)
        if 'error' in driver.current_url:
            print("error while getting \'get_auth_url\'")
        driver.find_element(By.XPATH, '//*[@id="contents"]/div[4]/button[1]').click()
