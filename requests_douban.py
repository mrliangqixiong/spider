# 导入模块
import requests
from lxml import etree
import time
import json

# 请求头信息
headers_base = {
    'Host': 'movie.douban.com',
    'Connection': 'keep-alive',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
    'Referer': 'https://movie.douban.com/explore',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}


# 定义一个download_douban函数
def download_douban(page):
    for i in range(page):
        url_str = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=time&page_limit=20&page_start=" + str(
            i * 20)
        print("url_str : ", url_str)

        response = requests.get(url=url_str, headers=headers_base)
        # print(response.text)

        json_obj = json.loads(response.text, encoding='utf-8')
        for one_movie in json_obj['subjects']:
            print(one_movie['title'], one_movie['rate'], one_movie['cover'])



        # 睡眠时间
        time.sleep(3)


# 写main函数调用
if __name__ == '__main__':
    download_douban(10)
