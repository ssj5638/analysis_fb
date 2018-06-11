# http test

from urllib.request import Request, urlopen      # 모듈 가져오기
from datetime import *
import sys

try:
    url = 'http://www.naver.com'
    request = Request(url)
    resp = urlopen(request)     # 요청 응답
    resp_body = resp.read().decode("utf-8") # 디코딩
    print(resp_body)
except Exception as e:
    print('%s %s' %(e, datetime.now()), file = sys.stderr)
