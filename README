Project that listens on a news source and makes a prediction on the sentiment. Based on the sentiment, allows one to make a decision.
Once decision is made, the project allows one to go out to a historical ticker source to see if the action yielded any profits.

Project consists of three packages :

1. Twitter api and related parsing
Goes out to twitter and listens on interesting news from  Reuters via the Twitter streaming API
Also filters on the information that we are interested in and the time of the day. 
The news is captured and written to  output.


2. Sentiment 

The sentiment analysis takes the input from package 1 and looks up the sentiment using a sentiment analysis API
Based on the score back from the API, we will make a decision to execute or not

3. Stock analyser

After a gap of 5 mins ( Assuming this is the time it takes for information to flow to the general market), we will query a finance API just after executing the query and 5 mins after. 
If we decided to previously buy the stock ( based on a positive sentiment) and there is an increase in the stock price, we are in profit and vice-versa.






   
