import requests
from Tistory.config import auth
from Tistory.config import secrets

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
# todo: input
BLOG_NAME = secrets.BLOG_INFO['BLOG_NAME']


def read_list():
    access_token = auth.access_token()
    # https://www.tistory.com/apis/post/list?access_token={access-token}&output={output-type}&blogName={blog-name}&page={page-number}
    baseUrl = 'https://www.tistory.com/apis/post/list'
    params = {
        'access_token': f'{access_token}',
        'output': 'json',
        'blogName': f'{BLOG_NAME}',
        'page': 1
    }
    response = requests.get(baseUrl, params=params, headers={'Accept': 'application/xml; charset=utf-8', 'User-Agent': USER_AGENT})
    print(response.text)


def read_post():
    access_token = auth.access_token()
    # https://www.tistory.com/apis/post/read?access_token={access-token}&blogName={blog-name}&postId={post-id}
    baseUrl = 'https://www.tistory.com/apis/post/list'
    params = {
        'access_token': f'{access_token}',
        'output': 'json',
        'blogName': f'{BLOG_NAME}',
        'page': 1
    }
    response = requests.get(baseUrl, params=params, headers={'Accept': 'application/xml; charset=utf-8', 'User-Agent': USER_AGENT})
    print(response.text)


def exec_post(keyword, content):
    access_token = auth.access_token()
    baseUrl = 'https://www.tistory.com/apis/post/write'
    # todo: dict에 인자?
    data = {
        'access_token': f'{access_token}',
        'output': 'json',
        'blogName': f'{BLOG_NAME}',
        'title': f'TOP 10 of {keyword}',
        'content': f'{content}',
        'visibility': 3,
        'tag': '트렌드, 꿀팁, 내돈내산, 리뷰, 최저가'
    }
    response = requests.post(baseUrl, data=data, headers={'Accept': 'application/xml; charset=utf-8', 'User-Agent': USER_AGENT})

    print(response.text)
    return response
