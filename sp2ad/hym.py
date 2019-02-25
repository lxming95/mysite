import base64 as b64
import urllib.parse
from urllib import request
from urllib.error import URLError

import socket

import itchat
from bs4 import BeautifulSoup
from lxml import etree

ym8 = b'aHR0cDovLzh5bS5jbi9ycHRsaXN0'
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER'}


# deadline = "2018-12-06 19:57:57"
# deadlink = ""


def gethtml(url):
	socket.setdefaulttimeout(20)  # 设置socket层的超时时间为20秒
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


def getList():
	index = b64.b64decode(ym8).decode()
	html = gethtml(index)
	# print (html)
	soup = BeautifulSoup(html, 'html.parser')
	lists = soup.find_all('div', attrs={'class': 'list-group'}, limit=200)
	lists = etree.HTML(str(lists))
	listsa = lists.xpath('//div/a')
	listst = lists.xpath('//div/a/text()')
	liststs = lists.xpath('//div/a/span')
	# for h in list:
	# print (h.tag)
	# print (h.attrib)
	# print (h.text)
	# return listsa, listst, liststs
	# for ai in zip(listsa, listst, liststs):
	# 	yield (ai[0].attrib["href"], ai[1], ai[2].text)
	list = []
	for ai in zip(listsa, listst, liststs):
		list.append((ai[0].attrib["href"], ai[1], ai[2].text))
	return list


# /html/body/div[2]/div[1]/a[2]/text()
# /html/body/div[2]/div[1]/a[2]/span


def isNew(ti, line):
	import time, datetime
	timestamp = time.time()
	timestruct = time.localtime(timestamp)
	date = time.strftime('%Y-%m-%d', timestruct)  # 2016-12-22 10:49:57
	da = time.strptime(date + " " + ti, '%Y-%m-%d %H:%M:%S')
	da = time.mktime(da)
	# now = time.time()
	now = time.strptime(line, '%Y-%m-%d %H:%M:%S')
	now = time.mktime(now)
	# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(da)),
	#       time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now)))
	if da - now < 0:
		return
	else:
		return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(da))


def ma(fun):
	import time

	deadline = "2019-01-04 10:16:00"
	deadlink = ""
	while (1):
		a = getList()[::-1]
		# for ai in a:

		for b in a:
			ti = isNew(b[2], deadline)
			if ti and b[0] != deadlink:
				fun(b64.b64decode(ym8).decode() + b[0], b[1], b[2])
				deadline = ti
				deadlink = b[0]
		time.sleep(10)


if __name__ == "__main__":
	# ma(print)
	import time

	itchat.auto_login(hotReload=True, )
	# itchat.auto_login()
	maps = itchat.search_friends(name="明")
	ming = maps[0]['UserName']
	# itchat.send('Hello', toUserName=ming)
	ym = b'aHR0cDovLzh5bS5jbg=='
	deadline = "2018-12-06 21:47:00"
	nowNum = "236248"
	print("start loop")
	while (1):
		try:
			a = getList()[::-1]
		except Exception as E:
			continue
		# for ai in a:
		for b in a:
			# ti = isNew(b[2], deadline)
			# if ti and b[0] != deadlink:
			if b[0].split('/')[2] > nowNum:
				msg = b[2] + b[1] + "," + b64.b64decode(ym).decode() + b[0]
				itchat.send(msg, toUserName=ming)
				nowNum = b[0].split('/')[2]
				print(msg)
		time.sleep(30)
