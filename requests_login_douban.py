# 导入模块
import requests
import json
import time
from lxml import etree

# 登陆界面请求头信息
headers_base = {
'Host': 'www.douban.com',
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.9',
}
# 登陆后请求头信息
headers_2 = {
'Host': 'www.douban.com',
'Connection': 'keep-alive',
'Cache-Control': 'max-age=0',
'Origin': 'https://www.douban.com',
'Upgrade-Insecure-Requests': '1',
'Content-Type': 'application/x-www-form-urlencoded',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Referer': 'https://www.douban.com/',
'Accept-Language': 'zh-CN,zh;q=0.9',
}

headers_3 = {
'Host': 'www.douban.com',
'Connection': 'keep-alive',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
'Referer': 'https://www.douban.com/',
'Accept-Language': 'zh-CN,zh;q=0.9',
}

# 获取 cookies
# 登陆url
url_str = 'https://www.douban.com/'
# 生成session()对象 sess
sess = requests.session()
response = sess.get(url=url_str, headers=headers_base)

# 获取验证码id
html = etree.HTML(response.text)
captcha_id = html.xpath("//input[@name='captcha-id']/@value")
print(captcha_id)

# 判断是否有验证码
if len(captcha_id) :
    captcha_id = captcha_id[0]
    img_url = 'https://www.douban.com/misc/captcha?id=%s&size=s' % captcha_id
    print('img_url : ', img_url)
    response = sess.get(url=img_url, headers=headers_3)
    with open("captcha.jpg", 'wb') as f:
        f.write(response.content)

    captcha_code = input("请输入验证码 >>>")

    # 登陆信息表单
    form_data = {
        'source': 'index_nav',
        'form_email': 'xxxxx@163.com',
        'form_password': 'xxxxxx',
        'captcha-solution': captcha_code,
        'captcha-id': captcha_id
    }
    print(form_data)
    # 登陆url
    url_str = 'https://www.douban.com/accounts/login'
    response = sess.post(url=url_str, headers=headers_2, data=form_data)
    print(response.text)
else :
    form_data = {
        'source': 'index_nav',
        'form_email': 'xxxxxx@163.com',
        'form_password': 'xxxxxx',
    }

    url_str = 'https://www.douban.com/accounts/login'
    response = sess.post(url=url_str, headers=headers_2, data=form_data)
    print(response.text)
