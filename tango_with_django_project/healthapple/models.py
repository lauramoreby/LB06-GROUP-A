from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Person(models.Model):
	user = models.OneToOneField(User)
	picture = models.ImageField(upload_to='profile_images', blank = True)
	
	def __unicode__(self):
		return self.user.username
		
class Category(models.Model):
	# many to one relationship with user
	
	person = models.ForeignKey(Person, default=None, null=True, blank=True)
	name = models.CharField(max_length=128)
	
	def save(self, *args, **kwargs):
        # Uncomment if you don't want the slug to change every time the name changes
        # if self.id is None:
            #self.slug = slugify(self.name)
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)
		
	def __unicode__(self):
		return self.name
		
class Page(models.Model):
	# many to one relationship with Category
	category = models.ForeignKey(Category)
	title = models.CharField(max_length = 128)
	summary = models.CharField(max_length = 128, default ="")
	url = models.URLField()
	flesch_score = models.DecimalField(max_digits=5,decimal_places=2,default = 0.00)
	sentiment_score = models.DecimalField(max_digits=4,decimal_places=2,default = 0.00)
	subjectivity_score = models.DecimalField(max_digits=4,decimal_places=2,default = 0.00)
	
	def __unicode__(self):
		return self.title
		

