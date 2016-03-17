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

def bing_search(search_terms,results):
    bing_url = urllib2.Request("https://api.datamarket.azure.com/Bing/Search/Web?$format=json&Query=%27" + query.replace(' ', '%27'))
    BING_API_KEY = 'Mbvcga7Sl8UTLHaKpLNYal5wSguMpYk010YbXGYVO7Q'
    base64string = base64.encodestring('%s:%s' % ('', 'Mbvcga7Sl8UTLHaKpLNYal5wSguMpYk010YbXGYVO7Q')).replace('\n', '')
    bing_url.add_header("Authorization", "Basic %s" % base64string)


    urls = [
    bing_url,
    ]

    # Make the Pool of workers
    pool = ThreadPool(100)

    # Open the urls in their own threads
    # and return the results
    results = pool.map(urllib2.urlopen, urls)


    for item in results:
        print item.read()

    #close the pool and wait for the work to finish
    pool.close()
    pool.join()



def run_query(search_terms):

    query = search_terms + " "

    bing_url = urllib2.Request("https://api.datamarket.azure.com/Bing/Search/Web?$format=json&Query=%27" + query.replace(' ', '%27'))
    BING_API_KEY = 'Mbvcga7Sl8UTLHaKpLNYal5wSguMpYk010YbXGYVO7Q'
    base64string = base64.encodestring('%s:%s' % ('', 'Mbvcga7Sl8UTLHaKpLNYal5wSguMpYk010YbXGYVO7Q')).replace('\n', '')
    bing_url.add_header("Authorization", "Basic %s" % base64string)


    urls = [
    bing_url,
    ]

    # Make the Pool of workers
    pool = ThreadPool(100)

    # Open the urls in their own threads
    # and return the results
    results = pool.map(urllib2.urlopen, urls)

    #close the pool and wait for the work to finish
    pool.close()
    pool.join()

    # Return the list of results to the calling function.
    return results

