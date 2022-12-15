import requests
from Tistory.config import secrets
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


# todo: urllib 사용해서 호출
# todo: 아직 미완성... click이 잘 안될걸?

def access_token():
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    # Authentication code 발급
    # authentication code 허가하기 페이지 접속 -> 허가하기 -> authentication code 저장
    get_auth_domain = 'https://www.tistory.com/oauth/authorize'
    redirect_uri = f'http://koc4.tistory.com'
    url_login = 'https://www.tistory.com/auth/login'
    get_auth_url = get_auth_domain + '?client_id=' + secrets.API_KEY[
        'TISTORY_APP_ID'] + '&redirect_uri=' + redirect_uri + '&response_type=code'

    options = webdriver.ChromeOptions()
    options.add_argument(f'user-agent={USER_AGENT}')
    options.add_argument("lang=ko_KR")
    path = r"D:/Development/Python/Coupang Partners/utils/chromedriver.exe"
    driver = webdriver.Chrome(service=Service(path), options=options)
    driver.implicitly_wait(2)

    driver.get(get_auth_url)
    if driver.find_element(By.XPATH, '//*[@id="cMain"]/div/div/div/a[1]/span[2]'):
        driver.get(url_login)
        driver.find_element(By.CLASS_NAME, 'txt_login').click()
        driver.find_element(By.XPATH, '//*[@id="input-loginKey"]').send_keys(secrets.LOGIN_INFO['ID'])
        driver.find_element(By.XPATH, '//*[@id="input-password"]').send_keys(secrets.LOGIN_INFO['PW'])
        driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/div/form/div[4]/button[1]').click()
        driver.get(get_auth_url)
        auth_code = driver.current_url.split('=')[1].split('&')[0]
    else:
        auth_code = driver.current_url.split('=')[1].split('&')[0]

    driver.close()

    # todo: 마지막 실행일시로부터 1시간 경과 시 auth_code 재발급 코드 작성
    access_token_url = 'https://www.tistory.com/oauth/access_token'
    get_access_token_params = {
        'client_id': secrets.API_KEY['TISTORY_APP_ID'],
        'client_secret': secrets.API_KEY['TISTORY_SECRET_KEY'],
        'redirect_uri': redirect_uri,
        'code': f'{auth_code}',
        'grant_type': 'authorization_code'
    }

    # Access-Token 발급
    get_access_token = requests.get(access_token_url, params=get_access_token_params,
                                    headers={'Accept': 'application/xml; charset=utf-8', 'User-Agent': USER_AGENT})
    print(get_access_token.text)
    print(get_access_token.text.split('=')[0])
    token = get_access_token.text.split('=')[0].split('&')[0]
    print(token)

    return token
