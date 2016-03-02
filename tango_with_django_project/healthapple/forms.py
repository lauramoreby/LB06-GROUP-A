from django import forms
from healthapple.models import Page, Category, UserProfile
from django.contrib.auth.models import User, UserProfile

class CategoryForm(forms.ModelForm):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=128)
	
	class Meta:
		model = Category
		fields = ('name',)
		
class PageForm(forms.ModelForm):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length = 128, help_text="Please enter the title of the page.")
	summary = models.CharField(max_length = 128, default = "default")
	url = models.URLField(max_length=200, help_text="Please enter the URL of the page.")
	flesch_score = models.IntegerField(default = 0)
	sentiment_score = models.IntegerField(default = 0)
	subjectivity_score = models.IntegerField(default = 0)
	
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
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture')