

# Load the AlchemyAPI module code.
import AlchemyAPI


# Create an AlchemyAPI object.
alchemyObj = AlchemyAPI.AlchemyAPI()


# Load the API key from disk.
alchemyObj.loadAPIKey("api_key.txt");


# Extract sentiment from a web URL.
result = alchemyObj.URLGetTextSentiment("http://www.reuters.com/article/2012/11/30/us-china-apple-iphone-idUSBRE8AT06G20121130?type=companyNews");
print result


# Extract sentiment from a text string.
#result = alchemyObj.TextGetTextSentiment("Analysis: Google's Android finally earns respect with developers");
#print result
'''

# Load a HTML document to analyze.
htmlFileHandle = open("data/example.html", 'r')
htmlFile = htmlFileHandle.read()
htmlFileHandle.close()


# Extract sentiment from a HTML document.
result = alchemyObj.HTMLGetTextSentiment(htmlFile, "http://www.test.com/");
print result


# Enable keyword-targeted sentiment.
kparams = AlchemyAPI.AlchemyAPI_KeywordParams()
kparams.setSentiment(1)

# Extract keywords with keyword-targeted sentiment.
result = alchemyObj.TextGetRankedKeywords("Mr. Miagi was the greatest sensei of all time.", kparams);
print result


# Enable entity-targeted sentiment.
eparams = AlchemyAPI.AlchemyAPI_NamedEntityParams()
eparams.setSentiment(1)

# Extract entities with entity-targeted sentiment.
result = alchemyObj.TextGetRankedNamedEntities("Mr. Miagi was the greatest sensei of all time.", eparams);
print result

'''

