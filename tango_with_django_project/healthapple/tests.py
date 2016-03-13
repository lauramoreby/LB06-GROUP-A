from django.test import TestCase
from healthapple.models import Category, Person, Page
from django.contrib.auth.models import User

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('jack')
        User.objects.create_user('jill')

    def test__user(self):
        """Test create user creates correct user"""
        jack = User.objects.get(id=1)
        jill = User.objects.get(id=2)
        self.assertEqual(jack, User.objects.get(username='jack'))
        self.assertEqual(jill, User.objects.get(username='jill'))

class UserTestPasswordCase(TestCase):
    def setUp(self):
        User.objects.create_user('jack', password = 'jack')
        User.objects.create_user('jill', password = 'jill')

    def test__user_password(self):
        """Test password not equal to text format"""
        jack_password = User.objects.filter(id=1).values_list('password', flat=True)
        jill_password = User.objects.filter(id=2).values_list('password', flat=True)
        
        self.assertFalse(jack_password == 'jack')
        self.assertFalse(jill_password == 'jill')

class PersonTestCase(TestCase):
    def setUp(self):
        jack = User.objects.create_user('jack')
        jill = User.objects.create_user('jill')

        Person.objects.create(user = jack)
        Person.objects.create(user = jill)

    def test__person(self):
        """Test create person"""
        jack = Person.objects.get(id=1)
        jill = Person.objects.get(id=2)
        
        self.assertEqual(jack, Person.objects.get(id=1))
        self.assertEqual(jill, Person.objects.get(id=2))

class CategoryTestCase(TestCase):
    def setUp(self):
        jack = User.objects.create_user('jack')
        jill = User.objects.create_user('jill')

        jack_person = Person.objects.create(user = jack)
        jill_person = Person.objects.create(user = jill)

        Category.objects.create(name='Fever',person=jack_person)
        Category.objects.create(name='Insomnia',person=jill_person)

    def test__category(self):
        """Test create Category links to specific user"""
        jack = Person.objects.get(id=1)
        jill = Person.objects.get(id=2)

        jack_category = Category.objects.get(person=jack)
        jill_category = Category.objects.get(person=jill)
        
        self.assertEqual(jack_category, Category.objects.get(name='Fever'))
        self.assertEqual(jill_category, Category.objects.get(name='Insomnia'))

class PageTestCase(TestCase):
    def setUp(self):
        jack = User.objects.create_user('jack')
        jill = User.objects.create_user('jill')

        jack_person = Person.objects.create(user = jack)
        jill_person = Person.objects.create(user = jill)

        fever_cat = Category.objects.create(name='Fever',person=jack_person)
        insomnia_cat = Category.objects.create(name='Insomnia',person=jill_person)

        Page.objects.create(category=fever_cat,
                            title='Fever',
                            summary='This is about fever',
                            url='http://www.fever.com',
                            flesch_score = 80.00,
                            sentiment_score = 0.05,
                            subjectivity_score = 0.05)
        
        Page.objects.create(category=insomnia_cat,
                            title='Insomnia',
                            summary='This is about insomnia',
                            url='http://www.insomnia.com',
                            flesch_score = 90.00,
                            sentiment_score = 0.10,
                            subjectivity_score = 0.10)
        
    def test__page(self):
        """Test create page with correct relationship to specific category"""
        jack = Person.objects.get(id=1)
        jill = Person.objects.get(id=2)

        jack_category = Category.objects.get(person=jack)
        jill_category = Category.objects.get(person=jill)

        jack_page = Page.objects.get(category=jack_category)
        jill_page = Page.objects.get(category=jill_category)
        
        self.assertEqual(jack_page, Page.objects.get(id=1))
        self.assertEqual(jill_page, Page.objects.get(id=2))

    def test_page_title(self):
        """Test create page with correct relationship to specific category"""
        jack = Person.objects.get(id=1)
        jill = Person.objects.get(id=2)

        jack_category = Category.objects.get(person=jack)
        jill_category = Category.objects.get(person=jill)

        fever_page = Page.objects.get(id=1).title
        insomnia_page = Page.objects.get(id=2).title

        self.assertEqual(unicode('Fever'),fever_page)
        self.assertEqual(unicode('Insomnia'),insomnia_page)

    def test_page_scores(self):
        """Test checking scores saved"""
        jack = Person.objects.get(id=1)
        jill = Person.objects.get(id=2)

        jack_category = Category.objects.get(person=jack)
        jill_category = Category.objects.get(person=jill)

        fever_flesch_score = Page.objects.get(id=1).flesch_score
        fever_sentiment_score = Page.objects.get(id=1).sentiment_score
        fever_subjectivity_score = Page.objects.get(id=1).subjectivity_score
        insomnia_flesch_score = Page.objects.get(id=2).flesch_score
        insomnia_sentiment_score = Page.objects.get(id=2).sentiment_score
        insomnia_subjectivity_score = Page.objects.get(id=2).subjectivity_score

        "unicode is used to synchronise the format"
        self.assertEqual(80.00,fever_flesch_score)
        self.assertEqual(unicode(0.05),unicode(fever_sentiment_score))
        self.assertEqual(unicode(0.05),unicode(fever_subjectivity_score))
        self.assertEqual(90.00,insomnia_flesch_score)
        self.assertEqual(unicode(0.10),unicode(insomnia_sentiment_score))
        self.assertEqual(unicode(0.10),unicode(insomnia_subjectivity_score))
