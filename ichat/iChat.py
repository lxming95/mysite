# coding=utf8
import threading
from xml.etree import ElementTree
import itchat
import os
import random
import time
from apscheduler.schedulers.background import BlockingScheduler

isreplay = True
isFriendChat, isGroupChat, isMpChat = False, False, True

usename = "小亚"
userName = ""
Honey = r"@4ad09d4a77e747d96b5670ef61f63d96"
me = r"@883c64fdb70a51631e3899df15e6d3fc53c36da0885a130ae56440fb21bf98d8"
me2 = ""

scheduler = BlockingScheduler()


# ['Note', 'Text', 'Picture', 'Sharing']
@itchat.msg_register(['Sharing'], isFriendChat=isFriendChat, isGroupChat=isGroupChat, isMpChat=isMpChat)
def simreplay(msg):
	global usename
	if isreplay and userName == msg['FromUserName']:
		time.sleep(random.random() * 2)
		print(getweatherfromXml(msg['Content']))
		if usename == "小亚" or usename == Honey:
			print("send to 小亚", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
			itchat.send(msgtohoney(msg['Content']), toUserName=itchat.search_friends(name="小亚")[0]['UserName'])
		# itchat.send(getweatherfromXml(msg['Content']), toUserName=itchat.search_friends(name=usename)[0]['UserName'])
		elif usename == me2:
			print("send to ", usename, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
			itchat.send(msgtohoney(msg['Content']), toUserName=usename)
		else:
			print("send to ", usename, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
			itchat.send(getweatherfromXml(msg['Content']), toUserName=usename)

	print("send end")
	del msg  # 对象的别名被显式的销毁，引用计数值为0，等待垃圾回收。该释放的变量及时释放，如果不及时释放，长期积累占用内存


# 发送给普通朋友的消息
@itchat.msg_register(['Text'], isFriendChat=True, isGroupChat=False, isMpChat=False)
def msgfromfrd(msg):
	if isreplay:
		global usename
		print("receive", msg['Content'], "from ", msg['User']['RemarkName'])
		if msg['FromUserName'] != me:
			# print (msg)
			time.sleep(random.random() * 2)
			sendmsg(msg['Content'])
			usename = msg['FromUserName']

	del msg  # 对象的别名被显式的销毁，引用计数值为0，等待垃圾回收。该释放的变量及时释放，如果不及时释放，长期积累占用内存


# 从 富文本xml中提取想要的信息
def getweatherfromXml(text):
	dic = {"weather": '', "now": ''}
	root = ElementTree.fromstring(text)
	lst_node = root.getiterator("title")
	if lst_node is not None:
		dic["weather"] = next(lst_node).text
	lst_node = root.getiterator("des")
	if lst_node is not None:
		dic["now"] = next(lst_node).text
	# msgtohoney(dic)
	return dic["weather"] + dic["now"]


# 发送给honey 的文字处理
def msgtohoney(text):
	# print("send to honey")
	dic = {"weather": '', "now": ''}
	root = ElementTree.fromstring(text)
	lst_node = root.getiterator("title")
	if lst_node is not None:
		dic["weather"] = next(lst_node).text
	lst_node = root.getiterator("des")
	if lst_node is not None:
		dic["now"] = next(lst_node).text
	if "不会有雨" in dic["weather"] or "不会下雨" in dic["weather"] or "不下雨" in dic["weather"] or "没有雨" in dic["weather"]:
		dic["weather"] += "，不需要带伞，爱你哦宝贝。"
	elif "雨" in dic["weather"]:
		dic["weather"] += "，出门记得带伞哦!爱你哦宝贝。"
	return dic["weather"] + dic["now"]


# 发送消息给彩云
def sendmsg(text):
	print("send to 彩云")
	itchat.send(text, toUserName=userName)


# 发送消息给 小亚
def sendmsgforhoney():
	global usename
	print("定时send")
	usename = "小亚"
	itchat.send("保定天气", toUserName=userName)


# 定时线程
def run_thread(name):
	# print(name+"thread is ttart")
	print('Run child process %s (%s)...' % (name, os.getpid()))
	# scheduler.add_job(sendmsgforhoney, 'cron', day_of_week='0-6', hour=8, minute=30, end_date='2099-06-30')
	scheduler.add_job(sendmsgforhoney, 'cron', day_of_week='0-6', hour=7, minute=30, end_date='2099-06-30',
	                  misfire_grace_time=60)
	scheduler.start()


def simplereplay():
	global userName
	itchat.auto_login(hotReload=True, enableCmdQR=False)
	## 获取名字中含有特定字符的公众号，也就是按公众号名称查找,返回值为一个字典的列表
	mps = itchat.search_mps(name='彩云天气')
	userName = mps[0]['UserName']
	# itchat.send("天气", toUserName=userName)
	print("天气")
	print('sentend')
	# t2 = Process(target=run_thread3, args=("b"))
	t2 = threading.Thread(target=run_thread, args=("b"))
	t2.start()
	# t2.join()
	itchat.run()
	print('next')


def runRpfrHoney():
	itchat.auto_login(hotReload=True, )
	## 获取名字中含有特定字符的公众号，也就是按公众号名称查找,返回值为一个字典的列表
	global userName, me, me2, Honey
	mps = itchat.search_mps(name='彩云天气')
	userName = mps[0]['UserName']

	maps = itchat.search_friends()
	me = maps['UserName']
	maps = itchat.search_friends(name="明")
	me2 = maps[0]['UserName']
	maps = itchat.search_friends(name="小亚")
	Honey = maps[0]['UserName']

	# 默认会发送一套数据测试
	# s = itchat.send("天气", toUserName=userName)
	# if s["BaseResponse"]["ErrMsg"] =="请求成功":
	# print(s["BaseResponse"]["ErrMsg"])

	print("天气 program start")
	# print('sentend')
	t2 = threading.Thread(target=run_thread, args=("b"))
	t2.start()
	itchat.run()


if __name__ == '__main__':
	itchat.auto_login(hotReload=True, )
	maps = itchat.search_friends(name="明")
	ming = maps[0]['UserName']
	# itchat.send('Hello', toUserName=ming)
	ym8 = b'aHR0cDovLzh5bS5jbi9ycHRsaXN0'
	deadline = "2018-12-06 19:57:59"
	import time, base64 as b64
	from sp2ad.hym import getList, isNew

	while (1):
		a = getList()[::-1]
		for b in a:
			if isNew(b[2], deadline):
				itchat.send(b64.b64decode(ym8).decode() + b[0] + "," + b[1] + "," + b[2], toUserName=ming)
		time.sleep(10)
