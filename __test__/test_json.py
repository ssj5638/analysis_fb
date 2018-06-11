# test json

from urllib.request import Request, urlopen      # 모듈 가져오기
from datetime import *
import sys
import json

try:
    url = 'http://kickscar.cafe24.com:8080/myapp-api/api/user/list'
    request = Request(url)
    resp = urlopen(request)     # 요청 응답
    resp_body = resp.read().decode("utf-8") # 디코딩
    print(type(resp_body), ":", resp_body)

    json_result = json.loads(resp_body)
    print(type(json_result), json_result)
    data = json_result['data']
    print(type(data), ":", data)

except Exception as e:
    print('%s %s' %(e, datetime.now()), file = sys.stderr)