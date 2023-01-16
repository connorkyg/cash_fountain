import time
import random
import requests
from urllib import parse

from Tistory.config import manage
from Tistory.config import chrome
from Coupang.data import titles
from Coupang.data import tags
from Tistory.config import secrets
from Coupang.data.keywords import keyword_list
from Coupang.config import apis as coupangApis
from Tistory.config import apis as tistoryApis
from Tistory.post import filing

BLOG_NAME = secrets.BLOG_INFO["BLOG_NAME"]


class api_list:
    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'

    def post_read(self):
        # https://www.tistory.com/apis/post/read?access_token={access-token}&blogName={blog-name}&postId={post-id}
        baseUrl = 'https://www.tistory.com/apis/post/read'
        params = {
            'access_token': f'{manage.tistory().get_access_token()}',
            'blogName': f'{secrets.BLOG_INFO["BLOG_NAME"]}',
            'postId': input("post id: ")
        }
        response = requests.get(baseUrl, params=params, headers={'Accept': 'application/xml; charset=utf-8',
                                                                 'User-Agent': chrome.browser().USER_AGENT})
        print(response.text)

    def post_list(self):
        # https://www.tistory.com/apis/post/list?access_token={access-token}&output={output-type}&blogName={blog-name}&page={page-number}
        baseUrl = 'https://www.tistory.com/apis/post/list'
        params = {
            'access_token': f'{manage.tistory().get_access_token()}',
            'output': 'json',
            'blogName': f'{secrets.BLOG_INFO["BLOG_NAME"]}',
            'page': 1
        }
        response = requests.get(baseUrl, params=params,
                                headers={'Accept': 'application/xml; charset=utf-8',
                                         'User-Agent': chrome.browser().USER_AGENT})
        print(response.text)

    def post_write(self):
        # TODO: 키워드를 DB에 넣어서 random 추출하자!!!!!!!!!!!!!!!!
        keyword = random.choice(keyword_list)
        url_keyword = parse.quote(keyword)
        limit = 10
        url = f"/v2/providers/affiliate_open_api/apis/openapi/products/search?keyword={url_keyword}&limit={limit}"

        product_data = coupangApis.get_product(url)
        manage.random_sleep(2, 5)
        content = filing.top_ten(product_data, keyword)
        manage.random_sleep(2, 5)

        baseUrl = 'https://www.tistory.com/apis/post/write'
        tag = random.sample(tags.tag_list, 4)
        data = {
            'access_token': f'{manage.tistory().get_access_token()}',
            'output': 'json',
            'blogName': f'{secrets.BLOG_INFO["BLOG_NAME"]}',
            'title': f'{random.sample(titles.title_list, 1)[0]} {keyword} {random.sample(titles.title_end, 1)[0]}',
            'content': f'{content}',
            'visibility': 3,
            'tag': f'{tag[0]}, {tag[1]}, {tag[2]}, {tag[3]}'
        }

        response = requests.post(baseUrl, data=data, headers={'Accept': 'application/xml; charset=utf-8',
                                                              'User-Agent': chrome.browser().USER_AGENT})
        print(response.text)
        return response
