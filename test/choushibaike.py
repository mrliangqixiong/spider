import requests
from lxml import etree
import time

# 头部信息
headers_base = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',

}

url_str = 'https://www.qiushibaike.com/'

response=requests.get(url=url_str,header=headers_base)
print(response.text)
html = etree.HTML(response.text)
