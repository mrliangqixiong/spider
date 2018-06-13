import requests
from lxml import etree

headers_base = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
}

headers_2 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
}
def download_gandianli_img():
    for i in range(1, 10):
        url_str = "http://ershou.gandianli.com/list.php?catid=&page=%d&price=0&thumb=0&vip=0&day=0&order=&list=1" % i
        print("url_str : " + url_str)
        response = requests.get(url=url_str, headers=headers_base)

        html = etree.HTML(response.text)
        img_url_list = html.xpath("//div[@class='goods_list_waper g-clearfix']//img[@class='sell_img']/@src")
        for one_img_url in img_url_list:
            # print(one_img_url)
            file_name = one_img_url.split("/")[-1]
            print("file_name: ", file_name)

            response = requests.get(url=one_img_url, headers=headers_2)
            with open("F:/sz第三阶段 爬虫/spider/test/img/" + file_name, "wb") as f:
                f.write(response.content)


if __name__ == '__main__':
    download_gandianli_img()