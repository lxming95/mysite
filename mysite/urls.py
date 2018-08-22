"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from mysite import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # url('testlo/', views.testlo),
    url('^key/$', views.getkey),
    url('^refreshkey/$', views.refreshkey),
    url('^gethome/$', views.gethome),
    url('^home/$', views.home),
    # path('hello/', views.hello),
    url(r'^$', views.homepage),
    # url(r'^image/$', views.itchademo, name="image"),

]
# handler404 = views.page_not_found  # 404