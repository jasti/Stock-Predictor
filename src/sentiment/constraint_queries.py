

# Load the AlchemyAPI module code.
import AlchemyAPI


# Create an AlchemyAPI object.
alchemyObj = AlchemyAPI.AlchemyAPI()


# Load the API key from disk.
alchemyObj.loadAPIKey("api_key.txt");


# Categorize a web URL.
result = alchemyObj.URLGetConstraintQuery("http://microformats.org/wiki/hcard", "1st link");
print result


# Load a HTML document to analyze.
htmlFileHandle = open("data/example.html", 'r')
htmlFile = htmlFileHandle.read()
htmlFileHandle.close()


# Categorize a HTML document.
result = alchemyObj.HTMLGetConstraintQuery(htmlFile, "http://www.test.com/", "1st link");
print result


