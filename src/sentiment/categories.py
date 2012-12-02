

# Load the AlchemyAPI module code.
import AlchemyAPI


# Create an AlchemyAPI object.
alchemyObj = AlchemyAPI.AlchemyAPI()


# Load the API key from disk.
alchemyObj.loadAPIKey("api_key.txt");


# Categorize a web URL.
result = alchemyObj.URLGetCategory("http://www.techcrunch.com/");
print result


# Categorize some text.
result = alchemyObj.TextGetCategory("Latest on the War in Iraq.");
print result


# Load a HTML document to analyze.
htmlFileHandle = open("data/example.html", 'r')
htmlFile = htmlFileHandle.read()
htmlFileHandle.close()


# Categorize a HTML document.
result = alchemyObj.HTMLGetCategory(htmlFile, "http://www.test.com/");
print result


