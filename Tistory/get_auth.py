import requests
import api_config
from selenium import webdriver
from selenium.webdriver.common.by import By

# todo: urllib 사용해서 호출

if __name__ == '__main__':
    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    # Authentication code 발급
    # authentication code 허가하기 페이지 접속 -> 허가하기 -> authentication code 저장
    get_auth_baseUrl = 'https://www.tistory.com/oauth/authorize'
    redirect_uri = 'http://koc4.tistory.com'

    options = webdriver.ChromeOptions()
    options.add_argument('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36')
    options.add_argument("lang=ko_KR")
    path = r"utils/chromedriver.exe"
    driver = webdriver.Chrome(path, options=options)
    driver.implicitly_wait(3)

    get_auth_url = get_auth_baseUrl + '?client_id=' + api_config.API_KEY['TISTORY_APP_ID'] + '&redirect_uri=' + redirect_uri + '&response_type=code'
    driver.get(get_auth_url)
    driver.implicitly_wait(3)

    allow_auth_code = driver.find_elements(By.CLASS_NAME, "confirm").click()
    driver.implicitly_wait(3)

    #todo: split
    print(driver.current_url)
    auth_code=driver.current_url
    driver.close()

    # todo: 마지막 실행일시로부터 1시간 경과 시 auth_code 재발급 코드 작성
    access_token_url = 'https://www.tistory.com/oauth/access_token'
    redirect_uri = 'http://koc4.tistory.com'
    get_access_token_params = {
        'client_id': api_config.API_KEY['TISTORY_APP_ID'],
        'client_secret': api_config.API_KEY['TISTORY_SECRET_KEY'],
        'redirect_uri': redirect_uri,
        'code': '9f0ddba8f5d08f7395a42a437d8392ef13e41bf5c80248cee363f0c3e459abebfbf82e10',
        'grant_type': 'authorization_code'
    }


    # Access-Token 발급
    get_access_token = requests.get(access_token_url, params=get_access_token_params, headers = {'Accept': 'application/xml; charset=utf-8', 'User-Agent': USER_AGENT})
    access_token = get_access_token.text.split('=')
    print(access_token[1])