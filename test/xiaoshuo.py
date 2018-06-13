import requests
import re


# 定义小说分类列表函数
def get_novel_sort_list():
    # 请求这个网页
    response = requests.get('http://www.quanshuwang.com/list/1_1.html')
    response.encoding = 'gbk'
    result = response.text
    # print(result)

    reg = r'<a target="_blank" title=".*?" href="(.*?)" class="clearfix stitle">(.*?)</a>'
    novel_url_list = re.findall(reg, result)
    # print(novel_url_list)
    return novel_url_list

def get_novel_content(novel_url):
    response = requests.get(novel_url)
    response.encoding='gbk'
    result = response.text
    reg = r'<a href="(.*?)" class="reader" title=".*?">开始阅读</a>'
    novel_url = re.findall(reg,result)[0]
    # print(novel_url)
    return novel_url


def get_chapter_url_list(novel_content_url):
    response = requests.get(novel_content_url)
    response.encoding='gbk'
    result = response.text
    reg =r'<li><a href="(.*?)" title=".*?">(.*?)</a></li>'
    chapter_url_list = re.findall(reg,result)
    return chapter_url_list


def get_chapter_content(url):
    response = requests.get(url)
    response.encoding = 'gbk'
    result = response.text
    reg = r'style5\(\);</script>(.*?)<script type="text/javascript">style6'
    chapter_content = re.findall(reg, result,re.S)[0]
    print(chapter_content)


for novel_url,novel_name in get_novel_sort_list():
    #  print(novel_url,novel_name)
    novel_content_url = get_novel_content(novel_url)
    for chapter_url,chapter_name in get_chapter_url_list(novel_content_url):
        get_chapter_content(chapter_url)































