from django import forms
from healthapple.models import Page, Category, Person
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
	name = forms.CharField(max_length=128)
	
	class Meta:
		model = Category
		fields = ('name',)
		
class PageForm(forms.ModelForm):
	title = forms.CharField(max_length = 128, help_text="Please enter the title of the page.")
	summary = forms.CharField(max_length = 128)
	url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
	flesch_score = forms.DecimalField(initial = 0.00)
	sentiment_score = forms.DecimalField(initial = 0.00)
	subjectivity_score = forms.DecimalField(initial = 0.00)
	
	class Meta:
                model = Page
		exclude = ('category',)
		
	def clean(self):
		cleaned_data = self.cleaned_data
                url = cleaned_data.get('url')

                # If url is not empty and doesn't start with 'http://', prepend 'http://'.
                if url and not (url.startswith('http://') or url.startswith('https://')):
                    url = 'http://' + url
                    cleaned_data['url'] = url

                return cleaned_data

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('picture',)
