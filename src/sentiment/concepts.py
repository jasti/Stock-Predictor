

# Load the AlchemyAPI module code.
import AlchemyAPI


# Create an AlchemyAPI object.
alchemyObj = AlchemyAPI.AlchemyAPI()


# Load the API key from disk.
alchemyObj.loadAPIKey("api_key.txt");


# Extract concept tags from a web URL.
result = alchemyObj.URLGetRankedConcepts("http://www.techcrunch.com/");
print result


# Extract concept tags from a text string.
result = alchemyObj.TextGetRankedConcepts("This thing has a steering wheel, tires, and an engine.  Do you know what it is?");
print result


# Load a HTML document to analyze.
htmlFileHandle = open("data/example.html", 'r')
htmlFile = htmlFileHandle.read()
htmlFileHandle.close()


# Extract concept tags from a HTML document.
result = alchemyObj.HTMLGetRankedConcepts(htmlFile, "http://www.test.com/");
print result


