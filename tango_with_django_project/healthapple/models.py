from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
	user = models.OneToOneField(User)
	picture = models.ImageField(upload_to='profile_images',default = None, blank = True)
	
	def __unicode__(self):
		return self.user.username
		
class Category(models.Model):
	# many to one relationship with user
	
	person = models.ForeignKey(Person, default=None, null=True, blank=True)
	name = models.CharField(max_length=128)
		
	def __unicode__(self):
		return self.name
		
class Page(models.Model):
	# many to one relationship with Category
	category = models.ForeignKey(Category, default=None, null=True, blank=True)
	title = models.CharField(max_length = 128)
	summary = models.CharField(max_length = 128, default ="")
	url = models.URLField()
	flesch_score = models.DecimalField(max_digits=5,decimal_places=2,default = 0.00)
	polarity_score = models.DecimalField(max_digits=4,decimal_places=2,default = 0.00)
	subjectivity_score = models.DecimalField(max_digits=4,decimal_places=2,default = 0.00)
	
	def __unicode__(self):
		return self.title
		

