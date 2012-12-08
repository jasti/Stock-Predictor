import tweetstream
import sys
import re

#words = ['apple', 'google', 'facebook','amazon','cisco','groupon','nokia','microsoft','intel','sirius','best buy','netflix','dell','hewlett packard']
words = []
people = [1652541]
locations = []   

# write info to file
#g = open('twitter_out', 'w')

max_tweets=3
tweet_num=0

daylist = ['Mon','Tue','Wed','Thu','Fri']

stream = tweetstream.FilterStream("PDSStern", "rebeccaBlack", track=words,follow=people, locations=locations)
for tweet in stream:
        tweet_num=tweet_num+1
        if tweet_num <= max_tweets:
               print "tweet_num: ", tweet_num
               #print tweet
               print "-----" * 10
               print ''
               
               #----------------------------------------------------------
               #  extract relevant info from tweet
               #----------------------------------------------------------
               if tweet.has_key("text"):
                     tweetnum=str(tweet_num).rjust(3)
                     text=tweet['text']
                     #text2=re.search((?:(?!X).)*, text)
                     #print text2
                     user_screen_name = tweet['user']['screen_name']
                     user = user_screen_name.ljust(15)
                     tweet_date       = tweet['created_at']
                     #user_Reuters = re.search("Reuters", user)

                     link_exists = re.search("http", text)
                     outlink = "None"
                     outlink = outlink.ljust(20)
                     if link_exists:
                         outlink= re.search("(?P<url>(http|https)?://[^\s]+)", text).group("url")

                     output=tweetnum + " | " + tweet_date + " | " + user + " | " + outlink + " | " + text
                     output2 = output + "\r"
                     #if user == "Reuters":
                     #if link_exists:
                     #       print output2
                     
                     day = re.findall("^\w{3}", tweet_date)
                     print day
                     time_start = "14:30"
                     time_stop  = "21:00"

                     if day in daylist:
                            print output2
                     #for item in daylist:
                     #       if item == day:
                     #              print output2

                     
       #elif tweet_num > max_tweets:
       #  print "----" * 10
#g.close()


'''
                     link_exists = re.search("http", text)
                     outlink = "None"
                     outlink = outlink.ljust(20)
                     #if link_exists:
                         #outlink= re.search("(?P<url>(http|https)?://[^\s]+)", text).group("url")

                     if user == "Reuters" and link_exists:
                            outlink= re.search("(?P<url>(http|https)?://[^\s]+)", text).group("url")
                            output=tweetnum + " | " + tweet_date + " | " + user + " | " + outlink + " | " + text
                            output2 = output + "\r"
                            print output2
                     #g.write(output)
'''
