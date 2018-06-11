# facebook api wrapper functions

from urllib.parse import urlencode
from .web_request import json_request   # 함수 import

BASE_URL_FB_API = 'https://graph.facebook.com/v3.0' # python에는 상수 없음 대문자로 표시
ACCESS_TOKEN = "EAACEdEose0cBANwlZArNRD4Q4skV6tFFd6VZCxgwmyZCf4c09ZBUYzNdKRGPodjwN0kQQPQGxFWHJsGN4SRfNgKN3bxlKqegbBcp2Eu7ZA7LkFBlhlPysvbbitluZB1NDFNZBgamKjjlu9GvGfY5Wc8w2NKcen2m5WdhLXix2xyLzWOIM1jG1uhnSTm5lZCZCZBImShgA2t1g9eAZDZD"


def fb_gen_url(base=BASE_URL_FB_API, node = '', **params):       # **params : dict 형대로 받기

    url = '%s/%s/?%s' % (base, node, urlencode(params))    # dict을 파라미터로 바꿔주는 함수
    return url


def fb_name_to_id(pagename):
    url = fb_gen_url(node=pagename, access_token = ACCESS_TOKEN)
    json_result = json_request(url=url)

    return json_result.get('id')

def fb_fetch_posts(pagename, since, until):        # 중요!!! crawler
    url = fb_gen_url(node=fb_name_to_id(pagename)+"/posts",
                     fields='id,message,link,name,type,shares,reactions,created_time,comments.limit(0).summary(true).limit(0).summary(true)',
                     since=since, until=until, limit=50, access_token=ACCESS_TOKEN)

    json_result = json_request(url=url)
    print(json_result)