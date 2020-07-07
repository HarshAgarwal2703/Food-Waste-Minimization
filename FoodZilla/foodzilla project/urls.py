from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('index.html', views.index, name = 'index'),
	path('stats.html', views.stats, name = 'stats'),
	path('upload.html', views.upload, name = 'upload'),
	path('feed.html', views.feed, name = 'feed'),
	path('org.html', views.org, name='org'),
	# path('recieve', views.recieve, name='recieve'),
]
