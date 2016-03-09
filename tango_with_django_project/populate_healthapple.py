import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from healthapple.models import Category, Page

def populate():
	fever_cat = add_cat('Fever')
	
	add_page(cat = fever_cat,
		title="About Fever",
		summary = "This is about fever",
		url = "https://en.wikipedia.org/wiki/Fever",
		flesch_score=1,
		sentiment_score=1,
		subjectivity_score=1)
		
def add_page(cat, title, summary, url, flesch_score, sentiment_score, subjectivity_score):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.summary = summary
    p.url=url
    p.flesch_score = flesch_score
    p.sentiment_score = sentiment_score
    p.subjectivity_score = subjectivity_score
    p.save()
    return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    # c = Category.objects.get_or_create(user=user)[0]
    c.save()
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting HealthApple population script..."
    populate()
