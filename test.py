import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

if __name__ == '__main__':
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"

    options = webdriver.ChromeOptions()
    options.add_argument(f'user-agent={USER_AGENT}')
    options.add_argument('lang=ko_KR')
    path = 'D:/Development/Python/Coupang Partners/utils/chromedriver.exe'
    driver = webdriver.Chrome(service=Service(path), options=options)
    url = 'https://naver.com'
    driver.get(url)
    # todo: split
    print(driver.current_url)
    auth_code = driver.current_url