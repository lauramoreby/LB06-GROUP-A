from django.conf.urls import patterns, url
from healthapple import views

urlpatterns = [
	
	url(r'^$',views.index, name='index'),
	url(r'^healthapplesearchapi/', views.search, name='search_api'),
	url(r'^searchsuggestionapi/', views.suggestion, name='suggestion_api'),
	url(r'^user_profile/',views.user_profile, name='user_profile'),
        url(r'^save_page/$', views.save_page, name='save_page'),
        url(r'^add_category/$', views.add_category, name='add_category'),
		url(r'^create_profile/$', views.create_profile, name='create_profile'),
]
