import re
import urllib.parse
# import request
from urllib import request
from urllib.error import URLError
import ssl
from bs4 import BeautifulSoup
import base64 as b64

# index = b'aHR0cDovL3d3dy45OXd3OC5jb20='


# lasttime = 1534836232.4316688
ssl._create_default_https_context = ssl._create_unverified_context
headers = {    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER'}
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
        return "erro"


def linkParser(index):
    cnblogs = gethtml(index)
    if cnblogs == "erro":
        return
    soup = BeautifulSoup(cnblogs, 'html.parser')
    all_div = soup.find_all('div', attrs={'class': 'thumb'}, limit=200)
    links = []
    # 循环div获取详细信息
    for item in all_div:
        link = analyzeLink(item, index)
        links.append(link)
    # print(links)
    return links


def analyzeLink(item, index):
    result = {}
    a_title = find_all(item, 'a', 'kt_imgrc bbb')
    if a_title is not None:
        # 标题
        result["title"] = a_title[0]['title']
        # 链接
        result["href"] = index + a_title[0]['href']
    return result


def find_all(item, attr, c, at='class'):
    return item.find_all(attr, attrs={at: c}, limit=1)


def get_link(index):
    links = linkParser(index)
    if not links:
        return "erro"
    for keys in links:
        # print(keys['href'])
        html = gethtml(keys['href'])
        if html == "erro":
            break
        if re.findall(r"get_file.*.mp4/", html):
            get_video = index + re.findall(r"get_file.*.mp4/", html)[0]
            # print(get_video)
            req = request.Request(url=get_video, headers=headers)
            page = request.urlopen(req)
            link = page.geturl()
            page.close
            link = re.sub(r'&' + link.split(r'&')[5], '', link)
            link = urllib.parse.unquote(link)
            link = re.sub(r'/\d{5}', r'/%s', link)
            return link


# def get_link(index):
#     links = linkParser(index)
#     for keys in links:
#         # print(keys['href'])
#         html = gethtml(keys['href'])
#         if re.findall(r"get_file.*.mp4/", html):
#             get_video = index + re.findall(r"get_file.*.mp4/", html)[0]
#             try:
#                 page = request.urlopen(get_video)
#                 link = page.geturl()
#                 link = re.sub(r'&' + link.split(r'&')[5], '', link)
#                 link = urllib.parse.unquote(link)
#                 link = re.sub(r'/\d{5}', r'/%s', link)
#                 return link
#
#             except URLError as e:
#                 if hasattr(e, 'code'):
#                     return e.code


def get_home():
    s=b'aHR0cHM6Ly9naXRodWIuY29tLzk5cmVkaXpoaS85OXJlL3dpa2k='
    re99 = gethtml(b64.b64decode(s).decode())
    soup = BeautifulSoup(re99, 'html.parser')
    all_div = soup.find_all('div', attrs={'class': 'markdown-body'}, limit=2)
    links = {}
    for item in all_div:
        a_title = find_all(item, 'a', 'nofollow', 'rel')
        if a_title is not None:
            # 链接
            links["href"] = a_title[0]['href']
    print(links['href'])
    try:
        req = request.Request(url=links['href'], headers=headers)
        page = request.urlopen(req)
        link = page.geturl()
        page.close
        return link
    except URLError as e:
        # print(e)
        if hasattr(e, 'code'):
            print(e.code)
        return "erro"


# print(link)


if __name__ == '__main__':
    print('')
