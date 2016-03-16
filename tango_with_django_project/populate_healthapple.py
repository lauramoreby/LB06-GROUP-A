import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from healthapple.models import Category, Page, Person
from django.contrib.auth.models import User

def populate():

        admin_superuser = add_superuser("admin","admin@admin.com")

        print "superuser created"
        
	jill_user = add_user("jill","jill@jill.com")
	jim_user = add_user("jim","jim@jim.com")
	joe_user = add_user("joe","joe@joe.com")

	print "users created"
	
	jill_person = add_person('jill')
	jim_person = add_person('jim')
	joe_person = add_person('joe')

	print "populating Category,Pages and Person entities"
	
	fever_cat = add_cat('Fever', Person.objects.get(id=1)) 
	
	add_page(cat = fever_cat,
		title="About Fever",
		summary = "This is about fever",
		url = "https://en.wikipedia.org/wiki/Fever",
		flesch_score=0,
		sentiment_score=0,
		subjectivity_score=0)
		
	add_page(cat = fever_cat,
		title="How to cure fever",
		summary = "This is about how to cure fever",
		url = "http://www.wikihow.com/Cure-a-Fever-at-Home",
		flesch_score=0,
		sentiment_score=0,
		subjectivity_score=0)
	
	add_page(cat = fever_cat,
		title="Fever Symptomps",
		summary = "This is about symptoms of fever",
		url = "http://www.nhs.uk/Conditions/Scarlet-fever/Pages/Symptoms.aspx",
		flesch_score=0,
		sentiment_score=0,
		subjectivity_score=0)
		
	AIDS_cat = add_cat('AIDS',Person.objects.get(id=2))
	
	add_page(cat = AIDS_cat,
		title="About AIDS",
		summary = "This is about AIDS",
		url = "http://www.avert.org/about-hiv-aids/what-hiv-aids",
		flesch_score=0,
		sentiment_score=0,
		subjectivity_score=0)
		
	add_page(cat = AIDS_cat,
		title="AIDS symptoms",
		summary = "Symptoms of AIDS",
		url = "http://www.nhs.uk/Conditions/HIV/Pages/Symptomspg.aspx",
		flesch_score=0,
		sentiment_score=0,
		subjectivity_score=0)
	
	add_page(cat = AIDS_cat,
		title="Cure AIDS",
		summary = "This how to cure AIDS",
		url = "http://www.cureaidsreport.org",
		flesch_score=0,
		sentiment_score=0,
		subjectivity_score=0)

	insomnia_cat = add_cat('Insomnia',Person.objects.get(id=3))
	
	add_page(cat = insomnia_cat,
		title="About insomnia",
		summary = "This is about insomnia",
		url = "http://www.nhs.uk/Conditions/Insomnia/Pages/Introduction.aspx",
		flesch_score=0,
		sentiment_score=0,
		subjectivity_score=0)
		
	add_page(cat = insomnia_cat,
		title="Insomnia symptoms",
		summary = "Symptoms of insomnia",
		url = "https://sleepfoundation.org/sleep-disorders-problems/insomnia/symptoms",
		flesch_score=0,
		sentiment_score=0,
		subjectivity_score=0)
	
	add_page(cat = insomnia_cat,
		title="Insomnia cure",
		summary = "This how to cure insomnia",
		url = "http://www.nhs.uk/Conditions/Insomnia/Pages/Treatment.aspx",
		flesch_score=0,
		sentiment_score=0,
		subjectivity_score=0)

	print "population completed."

	
def add_page(cat, title, summary, url, flesch_score, sentiment_score, subjectivity_score):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.summary = summary
    p.url=url
    p.flesch_score = flesch_score
    p.sentiment_score = sentiment_score
    p.subjectivity_score = subjectivity_score
    p.save()
    return p

def add_cat(name, person):
    c = Category.objects.get_or_create(name=name, person=person)[0]
    c.save()
    return c

def add_person(username):
	user = User.objects.get(username=username)
	per = Person.objects.get_or_create(user=user)[0]
	per.save()
	return per

def add_superuser(username, email):
        if User.objects.filter(username=username).exists() and User.objects.filter(username=username)[0].is_superuser:
                sUser = User.objects.get(username=username)
        else:
                sUser = User.objects.create_superuser(username=username,password=username,email=email)

        sUser.save()
        return sUser
        
def add_user(username, email):
        if User.objects.filter(username=username).exists():
                user = User.objects.get(username=username)
        else:
                user = User.objects.create_user(username=username,password=username,email=email)

        user.save()
        return user

# Start execution here!
if __name__ == '__main__':
    print "Starting HealthApple population script..."
    populate()
