import requests
from lxml import etree
import time
import re
import json

# 首页面请求头
headers_base = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Language':'zh-CN,zh;q=0.9',
# 'Cache-Control':'max-age=0',
'Connection':'keep-alive',
# 'Host':'www.qiushibaike.com',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
}

url_str = 'http://neihanshequ.com/'

# 生成一个对话对象
# 用于保存 cookie
sess = requests.session()
# response = requests.get(url=url_str, headers=headers_base)
# 使用会话对象去访问 url
response = sess.get(url=url_str, headers=headers_base)
# print(response.text)

# 生成xpath对象，提取首页面信息
html = etree.HTML(response.text)
text_list = html.xpath("//div[@class='upload-txt  no-mb']//p/text()")
# text_list = html.xpath("//li[@class='share-wrapper right']/@data-text")
for one_text in text_list:
    print(one_text)
    print('------------------------------------')

########################################################################

# 获取首页面的 token 值
token_value = html.xpath("//input[@name='csrfmiddlewaretoken']/@value")[0]
print('token_value : ', token_value)

# 生成动态加载请求的请求头
# 注意：要将 token 值加入头部信息中
headers_2 = {
    'Host': 'neihanshequ.com',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
    'Referer': 'http://neihanshequ.com/',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'X-CSRFToken': token_value
}

# 通过正则表达式获取首页面的 max_time 的值
max_time = re.compile(r'max_time.*').search(response.text).group()
# print(max_time)
max_time = max_time.split("'")[1]
print(max_time)

# 循环发送动态请求
for i in range(5):
    # 通过 max_time 的值拼接动态加载数据的 url
    url_str = "http://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time=" + str(max_time)
    print("url str : ", url_str)

    # 用 会话对象发送请求
    # response = requests.get(url=url_str, headers=headers_2)
    response = sess.get(url=url_str, headers=headers_2)
    # 将获得的数据转换成 json 对象
    json_obj = json.loads(response.text, encoding='utf-8')
    # 提取 json 对象里面的信息
    group_list = json_obj['data']['data']
    for one_group in group_list:
        print(one_group['group']['text'])
        print('----------------------------------')

    # 再从 json 对象中提取 下一次 动态请求的 max_time 值
    max_time = json_obj['data']['max_time']
    print('max_time : ', max_time)

    time.sleep(3)

