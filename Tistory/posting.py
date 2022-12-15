import requests

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
REDIRECT_URI = 'http://koc4.tistory.com'


def read_list():
    # https://www.tistory.com/apis/post/list?access_token={access-token}&output={output-type}&blogName={blog-name}&page={page-number}
    baseUrl = 'https://www.tistory.com/apis/post/list'
    params = {
        'access_token': '5c02130ccaaea73d1123eb34730ec78f_8d741ea510a6f6987c5565bd2fbe945b',
        'output': 'json',
        'blogName': 'koc4',
        'page': 1
    }
    response = requests.get(baseUrl, params=params, headers={'Accept': 'application/xml; charset=utf-8', 'User-Agent': USER_AGENT})
    print(response.text)


def read_post():
    # https://www.tistory.com/apis/post/read?access_token={access-token}&blogName={blog-name}&postId={post-id}
    baseUrl = 'https://www.tistory.com/apis/post/list'
    params = {
        'access_token': '5c02130ccaaea73d1123eb34730ec78f_8d741ea510a6f6987c5565bd2fbe945b',
        'output': 'json',
        'blogName': 'koc4',
        'page': 1
    }
    response = requests.get(baseUrl, params=params, headers={'Accept': 'application/xml; charset=utf-8', 'User-Agent': USER_AGENT})
    print(response.text)


def exec_post(keyword):
    # https://www.tistory.com/apis/post/write?access_token={access-token}&output={output-type}&blogName={blog-name}&title={title}&content={content}&visibility={visibility}&category={category-id}&published={published}&slogan={slogan}&tag={tag}&acceptComment={acceptComment}&password={password}
    baseUrl = 'https://www.tistory.com/apis/post/write'
    # todo: dict에는 인자를 넣지 못하는가?
    data = {
        'access_token': '5c02130ccaaea73d1123eb34730ec78f_8d741ea510a6f6987c5565bd2fbe945b',
        'output': 'json',
        'blogName': 'search4u',
        'title': f'TOP 10 of {keyword}',
        'content': 'sample content',
        'visibility': 3,
        'tag': '리뷰, test, sample, sample_tag',
    }
    response = requests.post(baseUrl, data=data, headers={'Accept': 'application/xml; charset=utf-8', 'User-Agent': USER_AGENT})
    print(response.text)


def example():
    return 0
