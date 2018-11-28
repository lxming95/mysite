import re
import urllib.parse
# import request
from urllib import request
from urllib.error import URLError
import ssl
from bs4 import BeautifulSoup
from lxml import etree

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER'}


def gethtml(url):
	try:
		req = request.Request(url=url, headers=headers)
		page = request.urlopen(req)
		htmlcode = page.read().decode()  # 读取页面源码
		# htmlcode = htmlcode.decode('utf-8')
		# print(htmlcode)  # 在控制台输出
		page.close
		return htmlcode
	except URLError as e:
		print(e)
		return "err"


def PostInChrome(url, data):
	try:
		data = urllib.parse.urlencode(data)
		req = urllib.request.Request(url, data)
		# req.add_header('Referer', 'http://www.python.org/')
		response = request.urlopen(req)
		htmlcode = response.read().decode()
		return htmlcode
	except URLError as e:
		print(e)
		return "err"


if __name__ == "__main__":
	html = gethtml("https://www.biquge.info/10_10582/")
	# print (html)
	soup = BeautifulSoup(html, 'html.parser')
	lists = soup.find_all('div', attrs={'class': 'box_con'}, limit=200)
	lists = etree.HTML(str(lists))
	list = lists.xpath('//dl/dd/a')
	# list = lists.xpath('/dl/dd')
	# for h in list:
	# 	print (h)
	for h in list:
		print (h.text)