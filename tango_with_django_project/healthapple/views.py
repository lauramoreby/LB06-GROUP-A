from django.shortcuts import render
from healthapple.models import Category, Page, Person
from django.contrib.auth.models import User
from healthapple.forms import CategoryForm, PageForm, UserForm, PersonForm
from healthapple.healthfinder_api import run_query as health
from healthapple.bing_search import run_query as bing
from django.http import HttpResponse
import urllib2
import ast
import json
import urllib2, base64
from multiprocessing.dummy import Pool as ThreadPool
from django.contrib.auth.decorators import login_required

query = ''

def index(request):

    return render(request, 'healthapple/index.html', {})

def user_profile(request):
    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        
        person = Person.objects.get(user=request.user)
        category = Category.objects.filter(person=person)
        
        category_list = []
        if len(category) != 0:
            for cat in category:
                category_list.append(cat)
        
            # Retrieve all of the associated pages.
            pages = Page.objects.filter(category=category)
            context_dict['pages'] = pages
        else:
            pass
        # Adds our results list to the template context under name pages.
        
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category_list
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'healthapple/user_profile.html', context_dict)

def create_profile(request):

    user = request.user
    
    if request.method == 'POST':
        
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            person = form.save(commit=False)
            person.user = user
            # if user does not choose any photo, just proceed
            # else, save that picture
            if len(request.FILES)!=0:
                person.picture = request.FILES['picture']
            person.save()
            return user_profile(request)
        else:
            print form.errors

    else:
        form = PersonForm()

        # If the form or details are bad or no form was supplied, render the form with error messages (if there are any)
    return render(request, "healthapple/create_profile.html", {'form': form})

def add_category(request):
    try:
        person = Person.objects.get(user=request.user)
    except Person.DoesNotExist:
        person = None

    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            cat = form.save(commit=False)
            cat.person = person
            cat.save()

            # Now call the index() view.
            # The user will be shown the homepage
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = CategoryForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'healthapple/add_category.html', {'form': form})

@login_required
def save_page(request):
    try:
        # show lists of categories the user have
        person = Person.objects.get(user=request.user)
        cat = Category.objects.filter(person=person)
        category_list = []
        for cat in cat:
            category_list.append(cat)
            
    except Category.DoesNotExist:
        cat = None
        
    context_dict = {}
    
    if request.method == 'POST':
        form = PageForm(request.POST)
        print form.is_valid()
        if form.is_valid():
            page = form.save(commit=False)
            if len(category_list)!= 0:
                page.category = category_list[0]
                context_dict['category']=category_list[0]
            page.save()

            # probably better to use a redirect here.
            return index(request)
        else:
            print form.errors
    else:
        form = PageForm()

    context_dict['form']=form
    
    return render(request, 'healthapple/save_page.html', context_dict)

def api_handler(api_name):
  global query
  if api_name == 'bing':
    return bing(query)
  if api_name == 'health':
    return health(query)

def api_pool():
  apis = [
    'bing',
    'health'
    ]
  pool = ThreadPool(2)
  results = pool.map(api_handler, apis)
  pool.close()
  pool.join()
  return results[0] + results[1]

def search(request):
    global query
    if request.method == 'GET':
        query = request.GET.urlencode()[2:]
        results = api_pool()
        d = {}
        i = 1
        for item in results:
          d[i] = item
          i += 1
        return HttpResponse(json.dumps(d))
    else:
        print "Failed in views.py"
        return HttpResponse("Invalid")

def suggestion(request):
    if request.method == 'GET':
        query = request.GET.urlencode()[2:]
        #make a request to that url + query. should be a function to make a http request
        link = urllib2.urlopen("http://suggestqueries.google.com/complete/search?client=firefox&q=" + query).read()
        splitLink = link.split(',')
        d = {}
        l = []
        for item in splitLink:
            item = item.replace('[','')
            item = item.replace(']','')
            item = item.replace('"','')
            l += [{'suggestion':item}]
        d['result'] = l
        return HttpResponse()
    else:
        return HttpResponse("Invalid")

