from django.conf.urls import patterns, url
from healthapple import views

urlpatterns = [
	
	url(r'^$',views.index, name='index'),
	url(r'^healthapplesearchapi/', views.search, name='search_api'),
	url(r'^user_profile/',views.user_profile, name='user_profile'),
]
