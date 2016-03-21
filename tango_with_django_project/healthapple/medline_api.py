import json
import urllib, urllib2

<<<<<<< HEAD
import xmltodict
from textstat.textstat import textstat
from textblob import TextBlob
import xml.etree.ElementTree
from xml.dom import minidom

=======
from textstat.textstat import textstat
from textblob import TextBlob
import xml.etree.ElementTree
import xml2json
import xml.etree.ElementTree as ET
import sys
from xml.dom import minidom
from bs4 import BeautifulSoup as Soup
>>>>>>> eff4179f86a6151ff14c3e8e896843d24a4f053c



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

<<<<<<< HEAD
        # Open file and write xml code to file to be parsed later on
        # file = open("temp.xml","w")
        # file.truncate()
        # file.write(response)


        # Convert the string response to a Python dictionary object.

        parse_response = xmltodict.parse(response)
        #print parse_response
        # parse_response = minidom.parse("temp.xml")
        # itemlist = parse_response.getElementsByTagName()
        #return type(parse_response)
        #return

        #file.close()
=======

        # Open file and write xml code to file to be parsed later on
        soup = Soup(response)
        soup.prettify()
        f = open('xml.txt','w')
        f.truncate()
        #f.write(soup.prettify().encode('utf-8').strip())

        lst = []

        for tag in soup.find_all(True):
            # f.write(tag.prettify().encode('utf-8').strip())
            # f.write("/n")
            # f.write("/n")
            lst += [[tag]]
            if soup.List:
                blob = TextBlob(tag['linksummary'])
                for sentence in blob.sentences:
                    polarity_score = sentence.sentiment.polarity
                    subjectivity_score = sentence.sentiment.subjectivity
                results.append({
                'title': tag['title'],
                'link': tag['url'],
                'summary': tag['linksummary'],
                'flesch_score': '{0:.2f}'.format(textstat.flesch_reading_ease(tag['linksummary'])),
                'polarity_score': '{0:.2f}'.format(polarity_score),
                'subjectivity_score': '{0:.2f}'.format(subjectivity_score),
                'source':'MedlinePlus'})




        dict = {}

        keynum = 0

        for x in lst:
            f.write(str(x)+"\n")
            f.write("\n")
            f.write("\n")

        return results
        # root = xml.dom.minidom.parseString(response)
        # print root
        # resultset = root.getElementsByTagNameNS('title','url')
        # print resultset
        # return resultset

        # Loop through each page returned, populating out results list.
        #for i in lst:

            # blob = TextBlob(result['Description'])
            # for sentence in blob.sentences:
            #     polarity_score = sentence.sentiment.polarity
            #     subjectivity_score = sentence.sentiment.subjectivity
            #
            # results.append({
            # 'title': result['Title'],
            # 'link': result['Url'],
            # 'summary': result['Description'],
            # 'flesch_score': '{0:.2f}'.format(textstat.flesch_reading_ease(result['Description'])),
            # 'polarity_score': '{0:.2f}'.format(polarity_score),
            # 'subjectivity_score': '{0:.2f}'.format(subjectivity_score),
            # 'source':'MedlinePlus'})
>>>>>>> eff4179f86a6151ff14c3e8e896843d24a4f053c


        # Loop through each page returned, populating out results list.
        l=[]
        for result in parse_response:
            l+= [parse_response[result]]
        return l
    #         blob = TextBlob(result['Description'])
    #         for sentence in blob.sentences:
    #             polarity_score = sentence.sentiment.polarity
    #             subjectivity_score = sentence.sentiment.subjectivity
    #
    #         results.append({
    #         'title': result['Title'],
    #         'link': result['Url'],
    #         'summary': result['Description'],
    #         'flesch_score': '{0:.2f}'.format(textstat.flesch_reading_ease(result['Description'])),
    #         'polarity_score': '{0:.2f}'.format(polarity_score),
    #         'subjectivity_score': '{0:.2f}'.format(subjectivity_score),
    #         'source':'MedlinePlus'})
    #
    #
    # # Catch a URLError exception - something went wrong when connecting!
    except urllib2.URLError as e:
<<<<<<< HEAD
         print "Error when querying the Bing API: ", e
    #
    # # Return the list of results to the calling function.
    # return results
=======
        print "Error when querying the MedlinePlus API: ", e

    # Return the list of results to the calling function.
    return results

>>>>>>> eff4179f86a6151ff14c3e8e896843d24a4f053c
