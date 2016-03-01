from django.conf.urls import patterns, include, url
from registration.backends.simple.views import RegistrationView
from django.contrib import admin

class MyRegistrationView(RegistrationView):
    def get_success_url(self,request):
        return '/healthapple/'
		
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^healthapple/',include('healthapple.urls')),
	url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
	url(r'^accounts/',include('registration.backends.simple.urls')),
	
)
