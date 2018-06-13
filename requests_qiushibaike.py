import requests
from lxml import etree
import time

headers_base = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Language':'zh-CN,zh;q=0.9',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Host':'www.qiushibaike.com',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
}

url_str = 'https://www.qiushibaike.com/'
response = requests.get(url=url_str, headers=headers_base)
html = etree.HTML(response.text)
# 获取最大页码,取最后一个 [-1 ],   strip()去掉前面空格
max_page = html.xpath("//ul/li/a/span[@class='page-numbers']/text()")[-1].strip()
print(max_page)

for i in range(1, int(max_page) + 1):
    url_str = 'https://www.qiushibaike.com/8hr/page/%d/' % i
    response = requests.get(url=url_str, headers=headers_base)

    html = etree.HTML(response.text)
    sub_url_list = html.xpath("//a[@class='contentHerf']/@href")
    print(sub_url_list)

    for sub_url in sub_url_list:
        # print(sub_url)
        # 拼接了连接
        url_str = "https://www.qiushibaike.com" + sub_url
        print('url_str : ', url_str)
        response = requests.get(url=url_str, headers=headers_base)
        html = etree.HTML(response.text)
        text_list = html.xpath("//div[@class='content']/text()")
        print(''.join(text_list).strip())

        time.sleep(1)
