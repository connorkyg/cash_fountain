import time
import random

now = time.strftime('%Y%m%d_%H%M%S')
percent = random.sample(range(50, 85), 1)[0]


def top_ten(product_data, keyword):
    # product 정보 -> HTML 문법 (+ Posting 양식에 넣음)
    data_file = f'../log/{now}_{keyword}.txt'
    with open(data_file, 'w+', encoding='utf-8') as f:
        for i in range(10):
            product_name = product_data[i]['productName']
            product_price = product_data[i]['productPrice']
            product_img = product_data[i]['productImage']
            product_url = product_data[i]['productUrl']
            product_rank = product_data[i]['rank']
            # 로켓배송
            if product_data[i]['isRocket'] == 'True':
                product_isRocket = '로켓배송 ✔'
            else:
                product_isRocket = ''
            # # 무료배송
            # # TODO: 무배가 있는 data도 있고 없는 data도 있는듯 함. 재확인 필요
            # if product_data[i]['isFreeShipping'] == 'True':
            #     product_isFreeShip = '무료배송 ✔'
            # else:
            #     product_isFreeShip = ''

            f.write(f'''<div>판매 순위: {product_rank}위<br>
{product_name}<br>
{product_price}원<br>
<img style="width: 40%;" src="{product_img}"><br>
<h2 data-ke-size="size26"><a href="{product_url}" target="_blank" rel="noopener"><span style="color: #0000ff;"><b>
최대 {percent}% 할인 중!
</b></span></a></h2><br>
<h2 data-ke-size="size26"><a href="{product_url}" target="_blank" rel="noopener"><span style="color: #0000ff;"><b>
최저가 사러가기
</b></span></a></h2>
<br>
{product_isRocket}<br><br><br><br>
''')
        f.write('''<p style="text-align: right;" data-ke-size="size14"><span style="color: #dddddd;">'''
                '''<i>파트너스&nbsp;활동을&nbsp;통해&nbsp;일정액의&nbsp;수수료를&nbsp;제공받을&nbsp;수&nbsp;있음</i></span></p>''')

    with open(data_file, 'r', encoding='utf-8') as f:
        content = f.read()
        print(content)

    return content
