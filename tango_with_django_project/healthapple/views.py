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

query = ''

def index(request):

    return render(request, 'healthapple/index.html', {})

def user_profile(request):

	return render(request, 'healthapple/user_profile.html', {})
	
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

	
def save_page(request):

    try:
        # show lists of categories the user have
        person = Person.objects.get(user=request.user)
        cat = Category.objects.filter(person=person)
        print cat
    except Category.DoesNotExist:
        cat = None

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            page = form.save(commit=False)
            page.save()

            # probably better to use a redirect here.
            return index(request)    
        else:
            print form.errors
    else:
        form = PageForm()

    return render(request, 'healthapple/save_page.html', {'form': form})

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
  return results[1] + results[0]
  
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
