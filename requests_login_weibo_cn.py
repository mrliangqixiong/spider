# 导入模块
import requests
import json
import time
from lxml import etree

# 登陆请求头信息
headers_base = {
'Host': 'passport.weibo.cn',
'Connection': 'keep-alive',
'Origin': 'https://passport.weibo.cn',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
'Content-Type': 'application/x-www-form-urlencoded',
'Accept': '*/*',
'Referer': 'https://passport.weibo.cn/signin/login?entry=mweibo&r=http%3A%2F%2Fweibo.cn%2F&backTitle=%CE%A2%B2%A9&vt=',
'Accept-Language': 'zh-CN,zh;q=0.9',
}
# 登陆后的请求头信息
headers_2 = {
'Host': 'weibo.cn',
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.9',
}
# 登陆界面url地址
url_str = 'https://passport.weibo.cn/sso/login'

# 账号登陆信息表单
form_data = {
'username':'xxxxxx@163.com',
'password':'xxxxxx',
'savestate':'1',
'r':'http://weibo.cn/',
'ec':'0',
'pagerefer':'',
'entry':'mweibo',
'wentry':'',
'loginfrom':'',
'client_id':'',
'code':'',
'qq':'',
'mainpageflag':'1',
'hff':'',
'hfp':'',
}

# 先登录
# 生成session()对象 sess
sess = requests.session()
response = sess.post(url=url_str, headers=headers_base, data=form_data)
print(response.text)

time.sleep(3)

# 登录后，继续获取页面数据
response = sess.get(url="https://weibo.cn/",  headers=headers_2)
print(response.text)

# 获得下一页的url    [0] 是提取出信息
# 注意加上编码
html = etree.HTML(response.text.encode(encoding='utf-8'))
next_page_url = html.xpath("//div[@id='pagelist']//a/@href")[0]
print('next_page_url : ', next_page_url)

for i in range(5):
    url_str = 'https://weibo.cn' + next_page_url
    response = sess.get(url=url_str, headers=headers_2)

    html = etree.HTML(response.text.encode(encoding='utf-8'))
    next_page_url = html.xpath("//div[@id='pagelist']//a/@href")[0]
    print('next_page_url : ', next_page_url)
    time.sleep(3)

