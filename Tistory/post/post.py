# -*- coding: utf-8 -*-

import random
import time
from urllib import parse

from Coupang.data.keywords import keyword_list
from Tistory.config import manage
from Coupang.config import apis as coupangApis
from Tistory.config import apis as tistoryApis
from Tistory.post import filing

if __name__ == '__main__':
    while True:
        try:
            a = int(input("숫자를 입력하세요: "))
            break
        except:
            print("잘못된 입력")
    if a[-1] == 1:
        tistoryApis.api_list().post_read()
    if a[-2] == 1:
        tistoryApis.api_list().post_list()
    if a[-3] == 1:
        tistoryApis.api_list().post_write()  # COMMENT: Tistory에 API 글쓰기가 많아지면 차단됨. Selenium으로 대체
        while True:
            # time.sleep(60 * 65)
            try:
                for i in range(10):
                    keyword = random.choice(keyword_list)
                    url_keyword = parse.quote(keyword)
                    limit = 10
                    url = f"/v2/providers/affiliate_open_api/apis/openapi/products/search?keyword={url_keyword}&limit={limit}"

                    # POSTING - TOP 10 사러가기
                    product_data = coupangApis.get_product(url)
                    time.sleep(5)
                    content = filing.top_ten(product_data, keyword)
                    time.sleep(5)
                    tistoryApis.api_list().post_write(keyword, content) # COMMENT: Tistory에 API 글쓰기가 많아지면 차단됨. Selenium으로 대체
                time.sleep(60 * 65)
            except:
                print("error occured")
                exit()