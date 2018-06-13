import requests
from lxml import etree
import time

headers_base = {
'Host': 'ershou.gandianli.com',
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.9',
}

def download_gandianli():
    f = open("gandianli.txt", 'a')

    for i in range(1,10):
        url_str = "http://ershou.gandianli.com/list.php?catid=&page=%d&price=0&thumb=0&vip=0&day=0&order=&list=1" % i
        print("url_str : " + url_str)

        response = requests.get(url=url_str, headers=headers_base)
        # print(response.status_code)

        html = etree.HTML(response.text)

        goods_list = html.xpath("//div[@class='goods_waper f_l g-clearfix']//a[@class='px13 f_n']/text()")
        # print(goods_list)
        price_list = html.xpath("//div[@class='goods_waper f_l g-clearfix']//strong[@class='g_price']/text()")
        # print(price_list)
        browse_times_list = html.xpath("//div[@class='goods_waper f_l g-clearfix']//div[@class='f_r']/text()")
        browse_times_list = [one[2:-1] for one in browse_times_list]
        # print(browse_times_list)

        for one_goods, one_price, one_browse_time in zip(goods_list, price_list, browse_times_list) :
            print( one_goods + "|+|" + one_price + '|+|' + one_browse_time )
            f.write(one_goods + "|+|" + one_price + '|+|' + one_browse_time + "\n")

        # print('i : ', i, len(goods_list))
        time.sleep(3)

    f.close()
    return True

if __name__ == '__main__' :
    download_gandianli()

