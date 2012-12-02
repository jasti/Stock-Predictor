

# Load the AlchemyAPI module code.
import AlchemyAPI


# Create an AlchemyAPI object.
alchemyObj = AlchemyAPI.AlchemyAPI()


# Load the API key from disk.
alchemyObj.loadAPIKey("api_key.txt");


# Detect the language for a web URL.
result = alchemyObj.URLGetLanguage("http://www.techcrunch.fr/");
print result


# Detect the language for a text string. (requires at least 100 characters text)
result = alchemyObj.TextGetLanguage("Hello my name is Bob Jones.  I am speaking to you at this very moment.  Are you listening to me, Bob?");
print result


# Load a HTML document to analyze.
htmlFileHandle = open("data/example.html", 'r')
htmlFile = htmlFileHandle.read()
htmlFileHandle.close()


# Detect the language for a HTML document.
result = alchemyObj.HTMLGetLanguage(htmlFile, "http://www.test.com/");
print result


