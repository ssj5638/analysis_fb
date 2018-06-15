import collect
import analyze
import visualize

if __name__ == '__main__':      # __name__ 내장 속성
    items = [
    #   ('jtbcnews', '2017-01-01', '2017-12-31')
        {'pagename': 'jtbcnews', 'since': '2017-01-01', 'until': '2017-12-31'},
        {'pagename': 'chosun', 'since': '2017-01-01', 'until': '2017-12-31'}
    ]
    # 데이터 수집 (collection)
    for item in items:
        resultfile = collect.crawling(**item, fetch = False)        # 파일 name만 꺼내옴
        item['resultfile'] = resultfile         # 데이터 분석에서 사용하기 위함
    #   collect.crawling(*item)
    #   collect.crawling("jtbcnews", '2017-01-01', '2017-12-31')

    # 데이터 분석 (analyze)
    # for item in items:
        # print(item['resultfile'])
    # json데이터를 str로
    for item in items:
        data = analyze.json_to_str(item['resultfile'], 'message')           # 본문 내용을 str로 변환
        print(data)
        # item['count_wordfreq'] = analyze.count_wordfteq(data)            # item['word_freq'] 시각화용


    # 데이터 시각화 (visualize)

