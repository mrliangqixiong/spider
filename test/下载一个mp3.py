# 导入模块,正则,json数据,requests
import requests
import re
import json

# 找到下载一个mp3
# url = 'http://zhangmenshiting.qianqian.com/data2/music/0680f756526189f9568219d538b3f379/559935472/559935472.mp3?xcode=bb78fce8b26d5c79aca186416cbdae39'
#
# 发送http 请求
# response = requests.get(url)
# print(response.content) # 是二进制 的数据
#  写入文件
# filename = '1.mp3' #文件名
# with open(filename, 'wb') as f: # write bytes 写二进制
#     f.write(response.content)



def get_mp3_by_sid(sid):
    """
    根据MP3id下载MP3
    :param sid: songid
    :return: 
    """
    # 根据sid 获取 下载mp3 地址
    # sid = '540560826'
    api = 'http://tingapi.ting.baidu.com/v1/restserver/ting?method=baidu.ting.song.play&format=jsonp&callback=jQuery17202741599001012014_1513517333931&songid=%s&_=1513517334915' % sid
    # api = 'http://tingapi.ting.baidu.com/v1/restserver/ting?method=baidu.ting.song.play&format=jsonp&callback=jQuery17202741599001012014_1513517333931&songid=540560826&_=1513517334915'
    # 访问api
    response = requests.get(api)
    data = response.text
    # print(data)
    data = re.findall(r'\((.*)\)', data)[0]
    data = json.loads(data)
    # print(data)
    # 取得歌曲的信息(名字,mp3地址)
    mp3_name = data['songinfo']['title']
    mp3_url = data['bitrate']['file_link']
    print(mp3_name)
    print(mp3_url)

    # # 发送http 请求
    response = requests.get(mp3_url)
    # print(response.content) # 是二进制 的数据
    # 写文件
    filename = '%s.mp3' % mp3_name
    with open(filename, 'wb') as f: # write bytes 写二进制
        f.write(response.content)


# get_mp3_by_sid('540130926')
def get_sids_by_name(query):
    # 根据查询的内容获取sid
    # 'http://music.baidu.com/search?key=%E5%BC%A0%E5%AD%A6%E5%8F%8B'
    # query = '张学友'
    api = 'http://music.baidu.com/search'
    data = {
        'key': query
    }
    response = requests.get(api, params=data)
    html = response.text
    # sid&quot;:269399533
    sids = re.findall(r'sid&quot;:(\d+),', html)
    return sids

sids = get_sids_by_name('泰勒斯威夫特')
for sid in sids:
    get_mp3_by_sid(sid)