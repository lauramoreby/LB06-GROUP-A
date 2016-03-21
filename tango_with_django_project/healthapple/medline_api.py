import json
import urllib, urllib2

from textstat.textstat import textstat
from textblob import TextBlob
import xml.etree.ElementTree
import xml2json
import xml.etree.ElementTree as ET
import sys
from xml.dom import minidom
from bs4 import BeautifulSoup as Soup



if __name__ == '__main__':
    main()

def main():
    user_query = raw_input()
    run_query(user_query)
    
def run_query(search_terms):
    # Specify the base
    root_url = 'https://wsearch.nlm.nih.gov/ws/query?db=healthTopics&term='
    
    # Construct the latter part of our request's URL.
    search_url = root_url + search_terms

    # Create our results list which we'll populate.
    results = []

    try:
        # Connect to the server and read the response generated.
        response = urllib2.urlopen(search_url).read()
        

        # Open file and write xml code to file to be parsed later on
        # soup = Soup(response)
        # soup.prettify()
        # f = open('xml.xml','w')
        # f.write(soup.prettify().encode('utf-8').strip())
        # f.close()
        # print soup.content
        root = xml.dom.minidom.parseString(response)
        print root
        resultset = root.getElementsByTagNameNS('title','url')
        print resultset
        return resultset

        # Loop through each page returned, populating out results list.
        for result in parse_response:
            blob = TextBlob(result['Description'])
            for sentence in blob.sentences:
                polarity_score = sentence.sentiment.polarity
                subjectivity_score = sentence.sentiment.subjectivity
                
            results.append({
            'title': result['Title'],
            'link': result['Url'],
            'summary': result['Description'],
            'flesch_score': '{0:.2f}'.format(textstat.flesch_reading_ease(result['Description'])),
            'polarity_score': '{0:.2f}'.format(polarity_score),
            'subjectivity_score': '{0:.2f}'.format(subjectivity_score),
            'source':'MedlinePlus'})


    # Catch a URLError exception - something went wrong when connecting!
    except urllib2.URLError as e:
        print "Error when querying the MedlinePlus API: ", e

    # Return the list of results to the calling function.
    return results

