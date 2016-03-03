from django.conf.urls import patterns, url
from healthapple import views

urlpatterns = [
	
	url(r'^$',views.index, name='index'),
	url(r'^search_result/', views.search, name='search'),

]