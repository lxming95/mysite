from django.test import TestCase

# Create your tests here.
from urllib import request
import ssl
import base64 as b64

# import urllib3
# import requests

#  忽略警告：InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised.
# requests.packages.urllib3.disable_warnings()

ssl._create_default_https_context = ssl._create_unverified_context
# 一个PoolManager实例来生成请求, 由该实例对象处理与线程池的连接以及线程安全的所有细节
# http = urllib3.PoolManager()

url = b'aHR0cDovL3d3dy45OXd3OC5jb20='
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER'}
req = request.Request(url=b64.b64decode(url).decode(), headers=headers)
req.unredirected_hdrs = {}
page = request.urlopen(req)
link = page.geturl()
print(link)
print(page.read)

# 通过request()方法创建一个请求：
# r = http.request('GET', url)
# print(r.status)  # 200
# # print(r._pool.host)
# print(r._pool.headers)
# 获得html源码,utf-8解码
# print(r.data.decode())
