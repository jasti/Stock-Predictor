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
import re

STOCK_GUAGE_TIME_INTERVAL = 10



class Predictor(object):
    links_repository = []    

    def perform_analysis(self,newsId,company_name, news_link):
        
        sentiment = self.perform_sentiment_analysis(company_name,news_link)
        
        # If sentiment is positive, perform financial analysis, if not, ignore
        self.perform_financial_analysis(newsId,company_name)
    


# Define a function for the thread
    def perform_sentiment_analysis(self,company_name, news_link):
        alchemyObj = AlchemyAPI.AlchemyAPI()
        # Load the API key from disk.
        alchemyObj.loadAPIKey("api_key.txt");
        # Extract sentiment from a web URL.
        result = alchemyObj.URLGetTextSentiment(news_link);
    
        return result


    def perform_financial_analysis(self,newsId,company_name):
        # Stubbing dummy quote, but ideally get hold of the right stock and lookup price
        #before
        print ystockquote.get_price(company_name)
        
        #Sleeping for some time before recording the time again
        time.sleep(STOCK_GUAGE_TIME_INTERVAL)
        #after
        print ystockquote.get_price(company_name)
    
        # Kick off another thread that will fetch the price of the same quote after 5 mins.
     
companies = []

def checkIfValidTweet(tweetData):
        news_link=''
        # Check if the news link is about a news source
       
        link_exists = re.search("http", tweetData)
        if link_exists:
            news_link= re.search("(?P<url>(http|https)?://[^\s]+)", tweetData).group("url")
       
    
        # Parse the link out of the tweet
    
        # Check if the new tweet is part of already parsed tweet. Don't do analysis again
    
        if((news_link not in Predictor.links_respository) & news_link != '' ):
            Predictor.links_repository.append(news_link)
                # Navigate to the new link
            return True , "APPL", news_link
        else :
            return False
    
    
    
    

words = []
people = [1652541]
locations = []   

stream = tweetstream.FilterStream("PDSStern", "rebeccaBlack", track=words,follow=people, locations=locations)
print "Connected to Reuters twitter stream and listening.."
#for tweet in stream:
while True:
    tweet_text= "@Reuters Apple is awesome http://badass.com/newsAboutApple"    
    
    #print "Incoming tweet: ", tweet["text"]
    isValidTweet, company_ticker_name, news_link =checkIfValidTweet(tweet_text)
    
    if(isValidTweet):
        
        # Create a unique id and keep track 
        uniqueId =str(time.time())
        newsId = uniqueId.replace(".", "")

        # Spawn a new thread for sentiment analysis and 'trade' engine 
        try:
            thread.start_new_thread(Predictor.perform_analysis, (newsId,company_ticker_name, news_link) )
        except:
            print "Error: unable to start thread"

    

    # Once previous action is done, kick off another thread to look for stock price in 5 mins and document 

