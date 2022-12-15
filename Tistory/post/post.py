from Coupang.config import apis as coupangApis
from Tistory.config import apis as tistoryApis
from Tistory.post import filing


keyword = 'bbb'
limit = 10
url = f"/v2/providers/affiliate_open_api/apis/openapi/products/search?keyword={keyword}&limit={limit}"
# todo: input

if __name__ == '__main__':
    # POSTING - TOP 10 사러가기
    # product_data = coupangApis.get_product(url)
    # content = filing.top_ten(product_data)
    # print(content[1])
    path = './20221209_122141_bbb.txt'
    f = open(path, 'r', encoding='utf-8')
    content = f.read()
    tistoryApis.exec_post(keyword, content)