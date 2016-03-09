from django.conf.urls import patterns, url
from healthapple import views

urlpatterns = [
	
	url(r'^$',views.index, name='index'),
	url(r'^bing_search_result/', views.search, name='search'),
	url(r'^user_profile/',views.user_profile, name='user_profile'),
]