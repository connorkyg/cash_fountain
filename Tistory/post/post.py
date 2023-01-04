# -*- coding: utf-8 -*-

import random
import time
from Coupang.config import apis as coupangApis
from Tistory.config import apis as tistoryApis
from Tistory.post import filing
from Coupang.data.keywords import keyword_list
from urllib import parse

# todo: 아니 왜 여기서 선언되는건 두번씩 실행되는건지~~~

# todo: input

if __name__ == '__main__':
    while True:
        try:
            for i in range(10):
                keyword = random.choice(keyword_list)
                url_keyword = parse.quote(keyword)
                limit = 10
                url = f"/v2/providers/affiliate_open_api/apis/openapi/products/search?keyword={url_keyword}&limit={limit}"

                # POSTING - TOP 10 사러가기
                product_data = coupangApis.get_product(url)
                content = filing.top_ten(product_data, keyword)
                tistoryApis.exec_post(keyword, content)
                # tistoryApis.read_post()
            time.sleep(60 * 65)
        except:
            print("error")
            exit()