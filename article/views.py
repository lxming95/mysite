from django.shortcuts import render
from article.models import Article
from django.http import Http404
import datetime
from django.shortcuts import render, HttpResponse, redirect


# Create your views here.


def home(request):
	post_list = Article.objects.all()  # 获取全部的Article对象
	return render(request, 'blog.html', {'post_list': post_list})


def detail(request, id):
	try:
		post = Article.objects.get(id=str(id))
	except Article.DoesNotExist:
		raise Http404
	return render(request, 'post.html', {'post': post})


def addnovel(request):
	Article.objects.create(title="ceshi", category="test", date_time=datetime.datetime.now(), content="test add")
	return HttpResponse("Ok")


def delnovel(request, id):
	# Article.objects.create(title="ceshi", category="test", date_time=datetime.datetime.now(), content="test add")
	Article.objects.filter(id=id).delete()
	return redirect("/blog/")


def novellist(request):
	from sp2ad.xiaoshuo import getadict
	post_list = getadict()
	return render(request, 'novellist.html', {'post_list': post_list})


def novel(request, url):
	from sp2ad.xiaoshuo import genovel
	novle = genovel(url)
	return render(request, 'novel.html', {'post': novle})
