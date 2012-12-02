

# Load the AlchemyAPI module code.
import AlchemyAPI


# Create an AlchemyAPI object.
alchemyObj = AlchemyAPI.AlchemyAPI()


# Load the API key from disk.
alchemyObj.loadAPIKey("api_key.txt");


# Extract topic keywords from a web URL.
result = alchemyObj.URLGetRankedKeywords("http://www.techcrunch.com/");
print result


# Extract topic keywords from a text string.
result = alchemyObj.TextGetRankedKeywords("Hello my name is Bob Jones.  I am speaking to you at this very moment.  Are you listening to me, Bob?");
print result


# Load a HTML document to analyze.
htmlFileHandle = open("data/example.html", 'r')
htmlFile = htmlFileHandle.read()
htmlFileHandle.close()


# Extract topic keywords from a HTML document.
result = alchemyObj.HTMLGetRankedKeywords(htmlFile, "http://www.test.com/");
print result


