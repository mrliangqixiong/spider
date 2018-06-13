import requests
from lxml import etree
import re
import time
import json

headers_1 = {
'Host': 'tieba.baidu.com',
'Connection': 'keep-alive',
'Accept': '*/*',
'X-Requested-With': 'XMLHttpRequest',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
'Accept-Language': 'zh-CN,zh;q=0.9',
}

headers_2 = {
'Host': 'tieba.baidu.com',
'Connection': 'keep-alive',
'Accept': '*/*',
'X-Requested-With': 'XMLHttpRequest',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
'Referer': 'https://tieba.baidu.com/index.html',
'Accept-Language': 'zh-CN,zh;q=0.9',
}

sess = requests.session()
response = sess.get(url="https://tieba.baidu.com/index.html", headers=headers_1)
# print(response.text)

html = etree.HTML(response.text)
text_list = html.xpath("//a[@class='title feed-item-link']/text()")
for one_text in text_list:
    print(one_text)

last_tid = re.compile(r'last_tid":(\d+)').search(response.text).group().split(':')[1].strip()
print('last_tid : ', last_tid)


for i in range(1, 3):
    url_str = 'https://tieba.baidu.com/f/index/feedlist?is_new=1&tag_id=all&limit=20&offset=' \
              + str(i * 20) + '&last_tid=' + str(last_tid) + '&_=' + str(int(1000 * time.time()))

    print(url_str)

    response = sess.get(url=url_str, headers=headers_2)
    json_obj = json.loads(response.text, encoding='utf-8')
    last_tid = json_obj['data']['last_tid']
    print('last_tid : ', last_tid)

    html = etree.HTML(json_obj['data']['html'])
    text_list = html.xpath("//a[@class='title feed-item-link']/text()")
    for one_text in text_list:
        print(one_text)

    time.sleep(3)
