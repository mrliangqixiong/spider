# 导入模块
import requests  # 网络请求模块 pip install reauests
import time  # 时间模块

# 请求的网址
url = 'http://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time=1514378948'

# 请求网址,网页源代码
# html = requests.request('GET',url)
# html.encoding = 'utf-8'
# requests.get(url)


# 翻页
timestamp = 1514378948
while type(timestamp) == int or type(timestamp) == float:

    url = 'http://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time=' + str(timestamp)

    html = requests.request('GET', url)
    time.sleep(2)
    for sb in range(20):
        # 提取段子
        content = html.json()['data']['data'][sb]['group']['text']

        # 保存本地
        with open('H:\\新建文件夹\\duanzi.txt', 'a', encoding='utf-8') as f:
            f.write(content + '\n' * 2)






    timestamp = html.json()['data']['max_time']

