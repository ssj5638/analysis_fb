from analysis_fb.collect.api import api
'''
url = api.fb_gen_url(node = 'jtbcnews', a = 10, b = 20, s = 'kickscar')
print(url)
'''
'''
id = api.fb_name_to_id("jtbcnews")
print(id)
'''

api.fb_fetch_posts("jtbcnews", '2018-01-01', '2018-12-31')
                   