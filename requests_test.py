# 导入模块
import requests

# url地址
# url_str = 'https://cn.bing.com/'
url_str = 'https://www.baidu.com/'

# 请求头信息,一个字典形式
headers_base = {
    'Host': 'www.baidu.com',
    'Connection': 'keep-alive',
     'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
     'Accept-Language': 'zh-CN,zh;q=0.9',
}
# 获取响应头部信息
# response = requests.get(url=url_str)
response = requests.get(url=url_str, headers=headers_base)
print(response.status_code) #打印状态码
# print(response.headers)   #打印响应头部信息
# print(response.cookies)   #打印cookies值
print(response.text)   #打印响应文本信息
