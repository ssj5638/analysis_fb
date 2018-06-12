# test for web_request.json_request

from analysis_fb.collect.api import web_request as wr   # alias (별명 지정)

url = 'http://kickscar.cafe24.com:8080/myapp-api/api/user/list'
# url = 'http://kickscar.cafe2.com:8080/myapp-api/api/user/list' 에러 결과
# <urlopen error [WinError 10060] 연결된 구성원으로부터 응답이 없어 연결하지 못했거나, 호스트로부터 응답이 없어 연결이 끊어졌습니다> 2018-06-11 14:18:29.357434

# json_result 받긔
def success_fetch_user_list(response):
    print(response)


def error_fetch_user_list(e):
    print(e)

wr.json_request(url = url ,success=success_fetch_user_list, error=error_fetch_user_list)    # 기본 에러함수
wr.json_request(url = url, success=success_fetch_user_list)     # web_request에서 정의한 lambda로 출력

"""
json_result = wr.json_request(url)
print(json_result)
"""

