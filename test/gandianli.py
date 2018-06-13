import requests
from lxml import etree


headers_base = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
}
def download_gandianli():
    for i in range(1,10):
        f = open("gandianli.txt","a" ,encoding="utf-8")
        url_str = 'http://ershou.gandianli.com/'
        response = requests.get(url=url_str, headers=headers_base)
        # print(response.text)
        # print(response.status_code)
        html = etree.HTML(response.text)
        one_goods_list =html.xpath("//div[@class='title row2 g-clearfix']/a[@class='px13 f_n']/text()")
        # print(one_goods_list)

        price_list = html.xpath("//div[@class='goods_list_waper g-clearfix']//strong[@class='g_price']/text()")
        # print(price_list)

        browse_time_list = html.xpath("//div[@class='goods_info']//div[@class='f_r']/text()")
        # print(browse_time_list)

        for one_goods,one_price,one_browse_time in zip(one_goods_list,price_list,browse_time_list):
            # print(one_goods+"||"+one_price+"||"+one_browse_time)

            f.write(one_goods+"||"+one_price+"||"+one_browse_time+"\n")

        f.flush()
        f.close()
if __name__ == '__main__':
    download_gandianli()
