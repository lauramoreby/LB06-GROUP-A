# HEALTHAPPLE 
## A federated health search application
### by LB06-GROUP-A

####Synopsis

The purpose of this application is to help people find out about particular conditions and to save the information that they find
into different folders. The application lets people search across two different medical sites (medline and healthfinder) and 
the general web (bing). People using the application would like to self-diagnose, i.e. given some symptoms find out what are the likely conditions. They would also like to find out information about particular conditions, treatments and medicines. The application should help the users understand if the information is easy to read, is loaded with sentiment and subjectivity.

####Installation

First you have to make a virtual environment and workon the virtualenvironment. Then go to directory that has requirements.txt and
type pip install -r requirements.txt

You should run the population script by typing python populate_healthapple.py in your terminal.
After you done this step, test users will be created with a sample category and page. The test users are jill, jim and joe

You might also run into missing corpus error when you submit a query. To fix this issue, you will have to download a python module
called corpora by running this code in your terminal, python -m textblob.download_corpora

####API

For this application, we uses three API, namely BingSearch API, MedlinePlus API and Healthfinder API

We also used Google API for inline query suggestions

####Contributors

ocherwei : Ong Cher Wei 2126200o

mohsinullah : Mohsin Ullah 2086644u

Baetek : Bartek Juszczak 2135441j

lauramoreby : Laura Moreby 2167714m
