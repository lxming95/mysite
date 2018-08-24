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
from django.conf.urls import url, include
from sp2ad import views
import article.views
from DjangoUeditor import urls as djud_urls
from mysite import settings

urlpatterns = [
    # url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    # url('testlo/', views.testlo),
    url('^key/$', views.getkey),
    url('^refreshkey/$', views.refreshkey),
    url('^refreshhome/$', views.refreshhome),
    url('^gethome/$', views.gethome),
    url('^home/$', views.home),
    # path('hello/', views.hello),
    url(r'^$', views.homepage),
    # url(r'^image/$', views.itchademo, name="image"),

    url('^blog/$', article.views.home, name='home'),
    # url(r'^(?P<id>\d+)/$', article.views.detail, name='detail'),
    url(r'^blog/(?P<id>\d+)/$', article.views.detail, name='detail'),

    url(r'^ueditor/', include(djud_urls)),

]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handler404 = views.page_not_found  # 404
