from django.test import TestCase
from healthapple.models import Category, Person
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
