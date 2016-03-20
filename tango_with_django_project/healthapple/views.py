from django.shortcuts import render
from healthapple.models import Category, Page, Person
from django.contrib.auth.models import User
from healthapple.forms import CategoryForm, PageForm, UserForm, PersonForm
from healthapple.healthfinder_api import run_query
from django.http import HttpResponse

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

	
def search(request):
    if request.method == 'GET':
        query = request.GET.urlencode()[2:]
        api_results = run_query(query)
        return HttpResponse(api_results)
    else:
        return HttpResponse("Invalid")

	
