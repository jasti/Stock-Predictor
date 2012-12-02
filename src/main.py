'''
Created on Dec 2, 2012

@author: zudec
'''


# Fetch data from Twitter
import tweetstream
import sentiment.AlchemyAPI as AlchemyAPI

import thread
import time
import stock.ystockquote as ystockquote




# Define a function for the thread
def call_sentiment_analysis():
    alchemyObj = AlchemyAPI.AlchemyAPI()
    # Load the API key from disk.
    alchemyObj.loadAPIKey("api_key.txt");
    # Extract sentiment from a web URL.
    result = alchemyObj.URLGetTextSentiment("http://www.reuters.com/article/2012/11/30/us-china-apple-iphone-idUSBRE8AT06G20121130?type=companyNews");
    
    
    # Stubbing dummy quote, but ideally get hold of the right stock and lookup price
    print ystockquote.get_price('GOOG')
    
    # Kick off another thread that will fetch the price of the same quote after 5 mins.
    print result    
   
      

words = []
people = [1652541]
locations = []   

stream = tweetstream.FilterStream("PDSStern", "rebeccaBlack", track=words,follow=people, locations=locations)
print "Connected to Reuters twitter stream and listening.."
for tweet in stream:
    
    print tweet
    
    
    print "Spawning a new thread and going back to listening.."
    
    # Spawn a new thread for sentiment analysis and 'trade' engine
    
    
    try:
        thread.start_new_thread(call_sentiment_analysis, () )
    except:
        print "Error: unable to start thread"

    

    # Once previous action is done, kick off another thread to look for stock price in 5 mins and document 

