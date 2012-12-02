

# Load the AlchemyAPI module code.
import AlchemyAPI


# Create an AlchemyAPI object.
alchemyObj = AlchemyAPI.AlchemyAPI()


# Load the API key from disk.
alchemyObj.loadAPIKey("api_key.txt");


# Categorize a web URL.
result = alchemyObj.URLGetAuthor("http://www.denverpost.com/breakingnews/ci_20109534/rtd-gets-cool-reaction-proposed-rail-westminster-buses");
print result


# Load a HTML document to analyze.
htmlFileHandle = open("data/example.html", 'r')
htmlFile = htmlFileHandle.read()
htmlFileHandle.close()


# Categorize a HTML document.
result = alchemyObj.HTMLGetAuthor(htmlFile, "http://www.test.com/");
print result
