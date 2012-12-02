

# Load the AlchemyAPI module code.
import AlchemyAPI


# Create an AlchemyAPI object.
alchemyObj = AlchemyAPI.AlchemyAPI()


# Load the API key from disk.
alchemyObj.loadAPIKey("api_key.txt");

'''
# Extract a title from a web URL.
result = alchemyObj.URLGetTitle("http://www.techcrunch.com/");
print result

''' 
# Extract page text from a web URL (ignoring navigation links, ads, etc.).
result = alchemyObj.URLGetText("http://www.reuters.com/article/2012/11/30/us-china-apple-iphone-idUSBRE8AT06G20121130?type=companyNews");
print result

'''
# Extract raw page text from a web URL (including navigation links, ads, etc.).
result = alchemyObj.URLGetRawText("http://www.techcrunch.com/");
print result


# Load a HTML document to analyze.
htmlFileHandle = open("data/example.html", 'r')
htmlFile = htmlFileHandle.read()
htmlFileHandle.close()


# Extract a title from a HTML document.
result = alchemyObj.HTMLGetTitle(htmlFile, "http://www.test.com/");
print result


# Extract page text from a HTML document (ignoring navigation links, ads, etc.).
result = alchemyObj.HTMLGetText(htmlFile, "http://www.reuters.com/article/2012/11/30/us-china-apple-iphone-idUSBRE8AT06G20121130?type=companyNews");
print result


# Extract raw page text from a HTML document (including navigation links, ads, etc.).
result = alchemyObj.HTMLGetRawText(htmlFile, "http://www.test.com/");
print result
'''

