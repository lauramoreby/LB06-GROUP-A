import json
import urllib, urllib2,base64
from multiprocessing.dummy import Pool as ThreadPool

from textstat.textstat import textstat
from textblob import TextBlob
from keys import *

def main():
    user_query = raw_input()
    run_query(user_query)

if __name__ == '__main__':
    main()

def run_query(search_terms):


    query = search_terms + " "

    bing_url = urllib2.Request("https://api.datamarket.azure.com/Bing/Search/Web?$format=json&Query=%27" + query.replace(' ', '%27'))
    base64string = base64.encodestring('%s:%s' % ('',  BING_API_KEY)).replace('\n', '')
    bing_url.add_header("Authorization", "Basic %s" % base64string)

    healthfinder_url = "http://healthfinder.gov/developer/Search.json?api_key="+ HEALTHFINDER_API_KEY + "&keyword="+query

    medline_url = 'https://wsearch.nlm.nih.gov/ws/' + query

    urls = [
    bing_url,
    healthfinder_url,
    medline_url
    ]

    # Make the Pool of workers
    pool = ThreadPool(100)

    # Open the urls in their own threads
    # and return the results
    responses = pool.map(urllib2.urlopen, urls)

    results = {"bing":[],"healthfinder":[],"medline":[]}

    for item in responses:
        print item


    #close the pool and wait for the work to finish
    pool.close()
    pool.join()

    # Return the list of results to the calling function.
    return responses

