import time
from Tistory.post import post

keyword = post.keyword
now = time.strftime('%Y%m%d_%H%M%S')


def top_ten(product_data):
    # product 정보 -> HTML 문법 (+ Posting 양식에 넣음)
    data_file = f'Tistory/log/{now}_{keyword}.txt'
    f = open(data_file, 'w+', encoding='utf-8')
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
        # 무료배송
        if product_data[i]['isFreeShipping'] == 'True':
            product_isFreeShip = '무료배송 ✔'
        else:
            product_isFreeShip = ''

        f.write(f'''<div>{product_rank}번<br>
{product_name}<br>
{product_price}원<br>
<img src={product_img} href={product_url}><br>
<button type="button">
최저가 사러가기
</button>
<br>
{product_isRocket}<br>
{product_isFreeShip}<br>
''')
    f.write('''<p style="text-align: right;" data-ke-size="size14"><span style="color: #dddddd;">'''
            '''<i>파트너스&nbsp;활동을&nbsp;통해&nbsp;일정액의&nbsp;수수료를&nbsp;제공받을&nbsp;수&nbsp;있음</i></span></p>''')
    f.close()
    f = open(data_file, 'r', encoding='utf-8')
    content = f.readlines()

    return content
