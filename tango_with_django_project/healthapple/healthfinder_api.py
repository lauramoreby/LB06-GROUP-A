import json
import urllib, urllib2

from textstat.textstat import textstat
from textblob import TextBlob
from keys import HEALTHFINDER_API_KEY


if __name__ == '__main__':
    main()

def main():
    user_query = raw_input()
    run_query(user_query)

def run_query(search_terms):

    # Wrap quotes around our query terms as required by the Bing API.
    # The query we will then use is stored within variable query.
    query = "'{0}'".format(search_terms)
    query = urllib.quote(query)

    # Construct the latter part of our request's URL.
    # Sets the format of the response to JSON and sets other properties.
    search_url = "http://healthfinder.gov/developer/Search.json?api_key="+ HEALTHFINDER_API_KEY + "&keyword="+query

    # Create our results list which we'll populate.
    results = []

    try:
        # Connect to the server and read the response generated.
        response = urllib2.urlopen(search_url).read()

        # Convert the string response to a Python dictionary object.
        json_response = json.loads(response)

        # Loop through each page returned, populating out results list.
        for result in json_response["Result"]:
            l=[]
            for i in result:
                l+=[i]
            return l
            blob = TextBlob(result['Description'])
            for sentence in blob.sentences:
                sentiment_score = sentence.sentiment.polarity
                subjectivity_score = sentence.sentiment.subjectivity

            results.append({
            'title': result['Title'],
            'link': result['Url'],
            'summary': result['Description'],
            'flesch_score': '{0:.2f}'.format(textstat.flesch_reading_ease(result['Description'])),
            'sentiment_score': '{0:.2f}'.format(sentiment_score),
            'subjectivity_score': '{0:.2f}'.format(subjectivity_score),
            'source':'Bing'})


    # Catch a URLError exception - something went wrong when connecting!
    except urllib2.URLError as e:
        print "Error when querying the Bing API: ", e

    # Return the list of results to the calling function.
    return results

