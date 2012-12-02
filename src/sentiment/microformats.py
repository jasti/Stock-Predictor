

# Load the AlchemyAPI module code.
import AlchemyAPI


# Create an AlchemyAPI object.
alchemyObj = AlchemyAPI.AlchemyAPI()


# Load the API key from disk.
alchemyObj.loadAPIKey("api_key.txt");


# Extract Microformats from a web URL.
result = alchemyObj.URLGetMicroformats("http://microformats.org/wiki/hcard");
print result


# Load a HTML document to analyze.
htmlFileHandle = open("data/microformats.html", 'r')
htmlFile2 = htmlFileHandle.read()
htmlFileHandle.close()


# Extract Microformats from a HTML document.
result = alchemyObj.HTMLGetMicroformats(htmlFile2, "http://www.test.com/");
print result


