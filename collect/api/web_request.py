from urllib.request import Request, urlopen      # 모듈 가져오기
from datetime import *
import sys
import json


def print_error(e):
    print('%s %s' % (e, datetime.now()), file=sys.stderr)

def html_request(url='', encoding='utf-8', success = None, error=print_error):
    # default 파라미터 // 성공하면 None 에러발생시 print_error 호출 callback형식
    # error 익명 함수
    try:
        request = Request(url)
        resp = urlopen(request)  # 요청 응답
        html = resp.read().decode(encoding)  # 디코딩

        print('%s : success for request[%s]' % (datetime.now(),url)) # 성공 로그

        if callable(success) is False:  # 성공 함수
            return html

        success(html)

    except Exception as e:
        if callable(error) is True:
            error(e)

def json_request(url='', encoding='utf-8', success = None, error = lambda e : print('%s %s'%(e, datetime.now()), file=sys.stderr)):
    try:
        request = Request(url)      # <class 'urllib.request.Request'>
        resp = urlopen(request)     # <class 'http.client.HTTPResponse'>
        json_body = resp.read().decode(encoding)    # <class 'str'>
        json_result = json.loads(json_body)     # <class 'dict'>

        print('%s : success for request [%s]' %(datetime.now(),url))    # 로그 찍기

        if callable(success) is False:      # success 함수를 호출할 수 없으면!
            return json_result

        success(json_result)

    except Exception as e:
        if callable(error) is True:
            error(e)
