# 爬中央大學附近的 foodpanda 美食
import requests
import random


class Randomcrawlrestaurant:
    def __init__(self):
        pass

    def crawlrestaurant(self):
        url = 'https://disco.deliveryhero.io/listing/api/v1/pandora/vendors'
        query = {
            'longitude': 121.1952988,  # 中央大學經度
            'latitude': 24.9681558,  # 中央大學緯度
            'language_id': 6,
            'include': 'characteristics',
            'dynamic_pricing': 0,
            'configuration': 'Variant1',
            'country': 'tw',
            'budgets': '',  # 低中高123
            'cuisine': '',
            'sort': 'rating_desc',  # 評分最高
            'food_characteristic': '',
            'use_free_delivery_label': False,
            'vertical': 'restaurants',
            'limit': 50,
            'offset': 0,
            'customer_type': 'regular'
        }
        headers = {
            'x-disco-client-id': 'web',
        }
        r = requests.get(url=url, params=query, headers=headers)

        if r.status_code == requests.codes.ok:
            data = r.json()

            restaurants = data['data']['items']

            # for restaurant in restaurants[:50]:
            #    print(restaurant['name'])
            #    print(restaurant['redirection_url'])
            #    print(restaurant['rating'])
            #    print(
            #        '-----------------------------------------------------------------------------------')

            # random
            draw = random.choice(restaurants[:50])
            content1 = "抽到" + draw['name'] + "\n" + "評價為" + \
                str(draw['rating']) + "\n" + draw['redirection_url']
            # print("抽到" + draw['name'])
            # print("排名為" + str(draw['rating']))
            # print(draw['redirection_url'])
            return content1
        else:
            content2 = "請求失敗"
            return content2
            # print('請求失敗')
