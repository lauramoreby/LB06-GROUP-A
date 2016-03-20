from django.shortcuts import render
from healthapple.models import Category, Page
from healthapple.forms import CategoryForm, PageForm, UserForm, PersonForm
from healthapple.medline_api import run_query
from django.http import HttpResponse

def index(request):

    return render(request, 'healthapple/index.html', {})

def user_profile(request):

	return render(request, 'healthapple/user_profile.html', {})
	
def add_category(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

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

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
                form.save(commit=True)

                # probably better to use a redirect here.
                return index(request)    
        else:
            print form.errors
    else:
        form = PageForm()

    context_dict = {'form':form}

    return render(request, 'healthapple/save_page.html', context_dict)

	
def search(request):
    if request.method == 'GET':
        query = request.GET.urlencode()[2:]
        api_results = run_query(query)
        return HttpResponse(api_results)
    else:
        return HttpResponse("Invalid")

	
