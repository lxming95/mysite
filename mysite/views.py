import json

import time

from django.shortcuts import render, HttpResponse
# from itchatdemo import itchatlogin
import threading

# Create your views here.
from mysite.file_rw import writejson, readjson
from mysite.spiderDemo import get_link, get_home

s = r'https://media2.99kk44.com/remote_control.php?time=1534833978&cv=e0051df0f4cd9ab37ca551e4d1ed2107&lr=0&cv2=996ffd7d8ac8c121b0b0d718ffe52dbd&file=/videos/%s/%s/%s.mp4'
user_DICT = {'k1': 'root1', 'k2': 'root2', 'k3': 'root3'}
lasttime = 1534836232.4316688


def page_not_found(request):
    return render(request, 'index.html')


def testlo(request):
    return render(request, 'testloop.html', {'user_dict': user_DICT})


def home(request):
    return render(request, 'index.html')


def homepage(request):
    # return render(request, '99re.html', {'user_dict': user_DICT})

    return HttpResponse("Sorry, This is not page for U")


def hello(request):
    return HttpResponse("Hello world")


def getkey(request):
    # resp = {'home': get_link()}
    re = readjson('data.json')
    resp = {'key': re["key"]}
    return HttpResponse(json.dumps(resp), content_type="application/json")
    # return render(request, 'key.html', {'key': s})


def refreshkey(request):
    last = readjson('data.json')["time"]
    # print(last)
    if time.time() - last > 20:
        re = readjson('data.json')
        ss = get_link(re["home"])
        if ss == "erro":
            return HttpResponse("Sorry, Please refresh home try again")
        a_dict = {"time": time.time(), "key": get_link(re["home"]), "home": re["home"]}
        writejson(a_dict)
        return HttpResponse("OK")
    else:
        return HttpResponse("Sorry, IT is too frequently")


def refreshhome(request):
    last = readjson('data.json')["time"]
    # print(last)
    if time.time() - last > 20:
        re = readjson('data.json')
        home_link = get_home()
        if s == "erro":
            return HttpResponse("Sorry, We can't open the home")
        a_dict = {"time": time.time(), "key": re["key"], "home": home_link}
        writejson(a_dict)
        return HttpResponse("OK")
    else:
        return HttpResponse("Sorry, IT is too frequently")


def gethome(request):
    re = readjson('data.json')
    resp = {'home': re["home"]}
    return HttpResponse(json.dumps(resp), content_type="application/json")

# def itchademo(request):
#     event_obj = threading.Event()
#     itchatlogin.login()
#     t = threading.Thread(target=itchatlogin.login(), name='login')
#     t.start()
#     print('start')
#     # t.join()
#     image_data = open('../QR.png', "rb").read()
#     print('turn')
#     return HttpResponse(image_data, content_type="image/png")
