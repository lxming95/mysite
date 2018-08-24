import re
import urllib.parse
# import request
from urllib import request
from urllib.error import URLError

from bs4 import BeautifulSoup

# index = r'https://99mm4.com/'


# lasttime = 1534836232.4316688


def gethtml(url):
    try:
        page = request.urlopen(url)
        htmlcode = page.read().decode()  # 读取页面源码
        # htmlcode = htmlcode.decode('utf-8')
        # print(htmlcode)  # 在控制台输出
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
            page = request.urlopen(get_video)
            link = page.geturl()
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
    re99 = gethtml(r'https://github.com/99redizhi/99re/wiki')
    soup = BeautifulSoup(re99, 'html.parser')
    all_div = soup.find_all('div', attrs={'class': 'markdown-body'}, limit=2)
    links = {}
    for item in all_div:
        a_title = find_all(item, 'a', 'nofollow', 'rel')
        if a_title is not None:
            # 链接
            links["href"] = a_title[0]['href']
    # print(links['href'])
    try:
        page = request.urlopen(links['href'])
        link = page.geturl()
        return link
    except URLError as e:
        # print(e)
        if hasattr(e, 'code'):
            print(e.code)
        return "erro"


# print(link)


if __name__ == '__main__':
    print('')
