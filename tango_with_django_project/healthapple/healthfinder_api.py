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
    # Construct the latter part of our request's URL.
    # Sets the format of the response to JSON and sets other properties.
    search_url = "http://healthfinder.gov/developer/Search.json?api_key="+ HEALTHFINDER_API_KEY + "&keyword="+search_terms

    # Create our results list which we'll populate.
    results = []

    try:
        # Connect to the server and read the response generated.
        response = urllib2.urlopen(search_url).read()
        
        # Convert the string response to a Python dictionary object.
        json_response = json.loads(response)
        if 'Tools' not in json_response["Result"]:
            return []
        
        # Loop through each page returned, populating out results list.
        for result in json_response["Result"]["Tools"]:
            
            blob = TextBlob(result['Contents'])
            for sentence in blob.sentences:
                polarity_score = sentence.sentiment.polarity
                subjectivity_score = sentence.sentiment.subjectivity
            print result

            url = ""
            try:
              
              if type(result['MoreInfo'])== list:
                  url = result['MoreInfo'][0]['Url']
              else:
                  url = result['MoreInfo']['Url']

              if url.endswith('/'):
                  url = url[:-1]
                  
              results.append({
              'title': result['Title'],
              'link': url,
              'summary': result['Contents'],
              'flesch_score': '{0:.2f}'.format(textstat.flesch_reading_ease(result['Contents'])),
              'polarity_score': '{0:.2f}'.format(polarity_score),
              'subjectivity_score': '{0:.2f}'.format(subjectivity_score),
              'source':'HealthFinder'})
            except:
              continue


    # Catch a URLError exception - something went wrong when connecting!
    except urllib2.URLError as e:
        print "Error when querying the HealthFinder API: ", e

    # Return the list of results to the calling function.
    print results
    return results

