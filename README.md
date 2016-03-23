# HEALTHAPPLE 
## A Federated Health Search Application
### by LB06-GROUP-A

####Synopsis

The purpose of this application is to help people find out about particular conditions and to save the information that they find
into different folders. The application lets people search across two different medical sites (medline and healthfinder) and 
the general web (bing). People using the application would like to self-diagnose, i.e. given some symptoms find out what are the likely conditions. They would also like to find out information about particular conditions, treatments and medicines. The application should help the users understand if the information is easy to read, is loaded with sentiment and subjectivity.

####Installation
The url for the deployed application is http://bartekxx12.pythonanywhere.com/healthapple
First, you will have to git clone the repo into any directory you like by typing git clone https://github.com/lauramoreby/LB06-GROUP-A.git

You will then have to makemigrations to create the database and migrate to apply the database. This can be done by typing python manage.py makemigrations followed by python manage.py migrate

You have to make a virtual environment and workon the virtual environment. Then go to directory that has requirements.txt and
type pip install -r requirements.txt.

You should run the population script by typing python populate_healthapple.py in your terminal.
After you have done this step, test users will be created with a sample category and page. The test users are jill, jim and joe.

To run the server, type python manage.py runserver

You might also run into missing corpus error when you submit a query. To fix this issue, you will have to download a python module
called corpora by running this code in your terminal, python -m textblob.download_corpora

Note: To save a page, user has to be logged in or else, error will occur

####API

For this application, we used three APIs, namely BingSearch API, MedlinePlus API and Healthfinder API.

We also used Google API for inline query suggestions.

####Contributors

ocherwei : Ong Cher Wei 2126200o

mohsinullah : Mohsin Ullah 2086644u

Baetek : Bartek Juszczak 2135441j

lauramoreby : Laura Moreby 2167714m
