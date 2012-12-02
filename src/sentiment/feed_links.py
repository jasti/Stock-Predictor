

# Load the AlchemyAPI module code.
import AlchemyAPI


# Create an AlchemyAPI object.
alchemyObj = AlchemyAPI.AlchemyAPI()


# Load the API key from disk.
alchemyObj.loadAPIKey("api_key.txt");


# Extract RSS / ATOM feed links from a web URL.
result = alchemyObj.URLGetFeedLinks("http://www.techcrunch.com/");
print result


# Load a HTML document to analyze.
htmlFileHandle = open("data/example.html", 'r')
htmlFile = htmlFileHandle.read()
htmlFileHandle.close()


# Extract RSS / ATOM feed links from a HTML document.
result = alchemyObj.HTMLGetFeedLinks(htmlFile, "http://www.test.com/");
print result


