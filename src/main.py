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
from time import gmtime, strftime


STOCK_GUAGE_TIME_INTERVAL_DIFFERENCE = 5



class Predictor(object):
    links_repository = []    
    companies_ticker = {"APPLE":"APPL", "GOOGLE":"GOOG", "AMAZON":"AMZN", "FACEBOOK":"FB", "CISCO":"CSCO", "GROUPON":"GRPN",
"NOKIA":"NOK", "MICROSOFT":"MSFT", "INTEL":"INTC", "SIRIUS":"SIRI", "BEST BUY":"BBY", "NETFLIX":"NFLX", "DELL":"DELL", 
"HEWLETT PACKARD":"HPQ","SAMSUNG":"SSNLF", "LENOVO":"LNVGY", "IBM":"IBM", "ADOBE":"ADBE", "ORACLE":"ORCL", "QUALCOMM":"QCOM", 
"EMC":"EMC", "VMWARE":"VMW", "TEXAS INSTRUMENTS":"TXM", "AUTOMATIC DATA":"ADP", "YAHOO":"YHOO", "COGNIZANT":"CTSH"}

    def perform_analysis(self,newsId,company_name, news_link):
        
        sentiment, sentiment_score = self.perform_sentiment_analysis(company_name,news_link)
        
      
        # If sentiment is positive, perform financial analysis, if not, ignore
     
        try:
            thread.start_new_thread(Predictor.perform_financial_analysis, (Predictor(),newsId,company_name,sentiment,sentiment_score) )
        except:
            print "Error: unable to start thread"
       
    


# Define a function for the thread
    def perform_sentiment_analysis(self,company_name, news_link):
        alchemyObj = AlchemyAPI.AlchemyAPI()
        # Load the API key from disk.
        alchemyObj.loadAPIKey("api_key.txt");
        # Extract sentiment from a web URL.
        result = alchemyObj.URLGetTextSentiment(news_link);
        #print result
        
        result= re.findall("<type>(.*)</type>|<score>(.*)</score>",result)
        if(result):
            sentiment_type = result[0][0]
            score = result[1][1]
        else:
            thread.exit()
        
        return sentiment_type, score
            



    def perform_financial_analysis(self,newsId,company_name,sentiment,sentiment_score):
        # Stubbing dummy quote, but ideally get hold of the right stock and lookup price

       
        #before
        for i in range(6):
            
        
            current_price = ystockquote.get_price(company_name)
            
            #print newsId,company_name,strftime("%Y-%m-%d %H:%M:%S", gmtime()),sentiment,sentiment_score,current_price
            #Sleeping for some time before recording the time again
            time.sleep(STOCK_GUAGE_TIME_INTERVAL_DIFFERENCE)
            #after
            new_price= ystockquote.get_price(company_name)
            
            print newsId,company_name,time.ctime(),sentiment,sentiment_score,current_price, new_price
    
        # Kick off another thread that will fetch the price of the same quote after 5 mins.
     
companies = []

def checkIfValidTweet(tweetData):
        news_link=''
        company_name= 'DUMMY'
        # Check if the news link is about a news source we care about
        
        # search the tweet for any of the
        for key,value in Predictor.companies_ticker.iteritems():
            match=re.search(key, tweetData, re.I)       
            if match:
                company_name= value
       
        link_exists = re.search("http", tweetData)
        if link_exists:
            news_link= re.search("(?P<url>(http|https)?://[^\s]+)", tweetData).group("url")
       
    
        # Parse the link out of the tweet
    
        # Check if the new tweet is part of already parsed tweet. Don't do analysis again
    
        if((news_link not in Predictor.links_repository) and news_link != '' ):
            Predictor.links_repository.append(news_link)
                # Navigate to the new link
            return True , company_name, news_link
        else :
            return False,company_name,''
    
    
    
    

words = []
people = [1652541]
locations = []   

stream = tweetstream.FilterStream("PDSStern", "rebeccaBlack", track=words,follow=people, locations=locations)
print "Connected to Reuters twitter stream and listening.."

tweet_text= "@Reuters Apple is awesome http://www.reuters.com/article/2012/12/07/apple-manufacturing-idUSL1E8N63YT20121207"  
#for tweet in stream:
while True:
     
    
    #print "Incoming tweet: ", tweet["text"]
    isValidTweet, company_ticker_name, news_link =checkIfValidTweet(tweet_text)
    
    if(isValidTweet):
        
        # Create a unique id and keep track 
        uniqueId =str(time.time())
        newsId = uniqueId.replace(".", "")

        # Spawn a new thread for sentiment analysis and 'trade' engine 
        try:
            thread.start_new_thread(Predictor.perform_analysis, (Predictor(),newsId,company_ticker_name, news_link) )
        except:
            print "Error: unable to start thread"

    

    # Once previous action is done, kick off another thread to look for stock price in 5 mins and document 

