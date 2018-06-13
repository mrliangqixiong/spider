import socket
import time

# address family : 1、AF_INET（internet进程间通信）；2、AF_UNIX（同一IP进程间通信）
# 套接字类型: 1、SOCK_STREAM（TCP-IP协议）；2、SOCK_DGRAM（UDP协议）
skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 通过域名获取网站 IP
www = 'www.gandianli.com'
# www = 'www.baidu.com'
# www = 'cn.bing.com'
server_ip = socket.gethostbyname(www)
# server_ip = '127.0.0.1'

# 链接 ip
skt.connect( (server_ip, 80) )
# skt.connect( (server_ip,443) )

# 发送信息，注意：信息类型为 字节
# 注意：要将 Accept-Encoding: gzip, deflate 去除，否则返回来的是压缩后的数据
# 如果是 https 的可能行，也可能不行
# msg = b'''GET http://gandianli.com/ HTTP/1.1\r\nHost: gandianli.com\r\nConnection: keep-alive\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36\r\nUpgrade-Insecure-Requests: 1\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\nAccept-Language: zh-CN,zh;q=0.9\r\n\r\n'''
# msg = b'''GET https://www.baidu.com/ HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: keep-alive\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36\r\nUpgrade-Insecure-Requests: 1\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\nAccept-Language: zh-CN,zh;q=0.9\r\n\r\n'''
# msg = b'''GET https://cn.bing.com/dict/search?q=%E4%BD%A0%E5%A5%BD&qs=n&form=Z9LH5&sp=-1&pq=%E4%BD%A0%E5%A5%BD&sc=2-2&sk=&cvid=3349A27168374F79B4C2B207F3F1626E HTTP/1.1\r\nHost: cn.bing.com\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\nReferer: https://cn.bing.com/\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.9\r\nCookie: _EDGE_V=1; MUID=398A25BBC8276AE939AD2ED9C9906BDB; MUIDB=398A25BBC8276AE939AD2ED9C9906BDB; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=D59B80FC428D4B628E4B958D3FD9DBB5&dmnchg=1; SRCHUSR=DOB=20171224; SRCHHPGUSR=CW=1366&CH=662&DPR=1&UTC=480&WTS=63649693872; ipv6=hit=1514100671559&t=4; _SS=SID=0C382BF822F96DA41672209A234E6CB9&HV=1514097116&bIm=129167; _EDGE_S=mkt=zh-cn&F=1&SID=0C382BF822F96DA41672209A234E6CB9\r\n\r\n'''


# 下载图片
# 注意：下载图片后，删除头部信息是不要用 UE，要用 vi 因为 ue保存时会自动修改里面的其他值
msg = b'''GET http://img.gandianli.com/201611/14/17094291732.png.thumb.png HTTP/1.1
Host: img.gandianli.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36
Accept: image/webp,image/apng,image/*,*/*;q=0.8
Referer: http://www.gandianli.com/sell/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9


'''

skt.sendall(msg)

# 发送数据之后，等待接受数据
with open('www.htm', 'w') as f:
    pass

res = skt.recv(4096)
while len(res) :
    print(res)
    print(len(res))
    with open('www.htm', 'ab') as f:
        f.write(res)
    res = None
    res = skt.recv(4096)

# 关闭 socket
skt.close()

