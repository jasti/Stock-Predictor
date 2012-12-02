

# Load the AlchemyAPI module code.
import AlchemyAPI  


# Create an AlchemyAPI object.
alchemyObj = AlchemyAPI.AlchemyAPI()


# Load the API key from disk.
alchemyObj.loadAPIKey("api_key.txt")


# Extract a ranked list of relations from a web URL.
result = alchemyObj.URLGetRelations("http://www.techcrunch.com/");
print result


# Extract a ranked list of relations from a text string.
result = alchemyObj.TextGetRelations("Ugly bob attacked beautiful Susan.");
print result


# Load a HTML document to analyze.
htmlFileHandle = open("data/example.html", 'r')
htmlFile = htmlFileHandle.read()
htmlFileHandle.close()


# Extract a ranked list of relations from a HTML document.
result = alchemyObj.HTMLGetRelations(htmlFile, "http://www.test.com/");
print result


params = AlchemyAPI.AlchemyAPI_RelationParams()

params.setDisambiguate(1)
params.setSentiment(1)
params.setEntities(1)
params.setSentimentExcludeEntities(1)

result = alchemyObj.TextGetRelations("Madonna enjoys tasty Pepsi.  I love her style.", params);
print result

params.setRequireEntities(1)

result = alchemyObj.TextGetRelations("Madonna enjoys tasty Pepsi.  I love her style.", params);
print result

