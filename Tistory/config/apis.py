import requests
from Tistory.config import auth
from Tistory.config import secrets
from Coupang.data import titles
from Coupang.data import tags
import random

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
# todo: input
BLOG_NAME = secrets.BLOG_INFO['BLOG_NAME']

def read_list():
    access_token = auth.get_access_token()
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
    access_token = auth.get_access_token()
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
    access_token = auth.get_access_token()
    baseUrl = 'https://www.tistory.com/apis/post/write'
    tag = random.sample(tags.tag_list, 4)
    data = {
        'access_token': f'{access_token}',
        'output': 'json',
        'blogName': f'{BLOG_NAME}',
        'title': f'{random.sample(titles.title_list, 1)[0]} {keyword} {random.sample(titles.title_end, 1)[0]}',
        'content': f'{content}',
        'visibility': 3,
        'tag': f'{tag[0]}, {tag[1]}, {tag[2]}, {tag[3]}'
    }

    response = requests.post(baseUrl, data=data, headers={'Accept': 'application/xml; charset=utf-8', 'User-Agent': USER_AGENT})
    print(response.text)

    return response
