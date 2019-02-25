import re
import urllib.parse
# import request
from urllib import request
from urllib.error import URLError
import ssl
from bs4 import BeautifulSoup
from lxml import etree
import datetime

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER'}
biqu = r"https://www.biquge.info/10_10582/"


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


def getAtag():
	html = gethtml("https://www.biquge.info/10_10582/")
	# print (html)
	soup = BeautifulSoup(html, 'html.parser')
	lists = soup.find_all('div', attrs={'class': 'box_con'}, limit=200)
	lists = etree.HTML(str(lists))
	lists = lists.xpath('//dl/dd/a')
	# for h in list:
	# print (h.tag)
	# print (h.attrib)
	# print (h.text)
	return lists


def getadict():
	a = getAtag()
	list = []
	for ia in a:
		dic = {"title": ia.text, "href": biqu + ia.attrib["href"]}
		list.append(dic)
	return list


def getAllnovel():
	lista = getAtag()
	for a in lista:
		html = gethtml(biqu + a.attrib["href"])
		soup = BeautifulSoup(html, 'html.parser')
		novel = soup.find_all('div', attrs={'id': 'content'})
		# print (novel[0].contents)
		yield (novel[0].contents)


def genovel(url):
	# html = gethtml(biqu + a.attrib["href"])
	html = gethtml(url)
	soup = BeautifulSoup(html, 'html.parser')
	novel = soup.find_all('div', attrs={'id': 'content'})
	dic = {"content": "".join(str(novel[0].contents).split())}
	return dic


if __name__ == "__main__":
	a = getAtag()
	list = []
	for ia in a:
		dic = {"title": ia.text, "href": biqu + ia.attrib["href"]}
		list.append(dic)
	print (type(list[0]))
