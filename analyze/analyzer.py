import json
import re           # 정규 표현식


def json_to_str (filename, key):
    jsonfile = open(filename, 'r', encoding='utf-8')        # 파일 읽어들이기
    json_string = jsonfile.read()
    # print(json_string)                        # 스트링으로 출력
    jsonfile.close()

    data = ''
    json_data = json.loads(json_string)         # 파이썬 객체로 만들기
    # print(json_data)                          # 객체이기 때문에 리스트로 출력 됨

    for item in json_data:
        value = item.get(key)
        if value is None:
            continue                            # for문으로 돌아가기

        data += re.sub('[^\w]', '', value)      # [^\w] 공백 문자로 시작하는 문자열

    return (data)

