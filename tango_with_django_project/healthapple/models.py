from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
	name = models.CharField(max_length=128)
	
	def __unicode__(self):
		return self.name
		
class Page(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length = 128)
	url = models.URLField()
	readibility_score = models.IntegerField(default = 0)
	subjectivity_score = models.IntegerField(default = 0)
	sentimentality_score = models.IntegerField(default = 0)
	
	def __unicode__(self):
		return self.title
		
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	
	picture = models.ImageField(upload_to='profile_images', blank = True)
	
	def __unicode__(self):
		return self.user.username