import requests
from lxml import etree
import json
import time

headers_base = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
}
def download_douban(page):
    for i in range(page):
        url_str = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=time&page_limit=20&page_start=" + str(i*20)
        # print("url_str",url_str)
        response = requests.get(url=url_str, headers=headers_base)
        # print(response.status_code)
        # print(response.text)

        json_obj = json.loads(response.text, encoding="utf-8")
        for one_movie in json_obj['subjects']:
            print(one_movie['title'], one_movie['rate'], one_movie['cover'])


        time.sleep(3)

if __name__ == '__main__':
    download_douban(10)