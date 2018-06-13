import requests
import json
import time
from lxml import etree

headers_base = {
'Host': 'www.zhihu.com',
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Referer': 'https://www.zhihu.com/signup?next=%2F',
'Accept-Language': 'zh-CN,zh;q=0.9',
}

cookies = {
'aliyungf_tc':'AQAAAH648xH/5wQAuF5ccUrAQnn0292Y',
'_xsrf':'5b103790-7b04-4ff5-bc97-ed7bf6f45097',
'q_c1':'056461e5af344b7bbd8f2ca0086dedb7|1519893886000|1519893886000',
'_zap':'dc9fe67b-f396-4da5-9173-416082b32256',
'capsion_ticket':'2|1:0|10:1519893894|14:capsion_ticket|44:N2VkYTIyMTU3N2RmNDIxZTgwMzU3OTU4ZWM3MWVkOTc=|811f94ffd403c87df15bcb333387dbf48db6f45eb54268b3a66b2800362705ac',
'z_c0':'2|1:0|10:1519893903|4:z_c0|80:MS4xYm4wY0FRQUFBQUFtQUFBQVlBSlZUWThMaFZ0R0lRT3Z2MEdzSmJWMjFXNEU2Z3c0R1RyR0FRPT0=|00acbd212bbfa8b99e75ef46cf06bdbb29bc9dbf5acecb5fcf3f81ac686e434c',
}

sess = requests.session()

for k, v in cookies.items():
    sess.cookies[k] = v

print(sess.cookies)

response = sess.get(url="https://www.zhihu.com/", headers=headers_base)
# print( response.text )
with open('zhihu.html', 'w') as f:
    f.write(response.text)

