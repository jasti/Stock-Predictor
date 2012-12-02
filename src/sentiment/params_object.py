

# Load the AlchemyAPI module code.
import AlchemyAPI


# Create an AlchemyAPI object.
alchemyObj = AlchemyAPI.AlchemyAPI()

# Create a parameters object, and set some API call options.
params = AlchemyAPI.AlchemyAPI_NamedEntityParams()
params.setDisambiguate(0)
params.setQuotations(0)

# Load the API key from disk.
alchemyObj.loadAPIKey("api_key.txt")


# Extract a ranked list of named entities from a web URL, using the supplied parameters object.
result = alchemyObj.URLGetRankedNamedEntities("http://www.techcrunch.com/", params);
print result

params.setDisambiguate(0)
params.setSentiment(1)

# Extract a ranked list of named entities from a text string, using the supplied parameters object.
result = alchemyObj.TextGetRankedNamedEntities("Hello my name is Bob.  I am speaking to you at this very moment.  Are you listening to me, Bob?", params);
print result


# Load a HTML document to analyze.
htmlFileHandle = open("data/example.html", 'r')
htmlFile = htmlFileHandle.read()
htmlFileHandle.close()


# Extract a ranked list of named entities from a HTML document, using the supplied parameters object.
result = alchemyObj.HTMLGetRankedNamedEntities(htmlFile, "http://www.test.com/", params);
print result


