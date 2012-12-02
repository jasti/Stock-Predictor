
import urllib
import sys

from xml.etree import ElementTree as etree

class AlchemyAPI_Params(object):
  _url = ""
  _html = ""
  _text = ""
  _outputMode = ""
  _customParameters = ""
  def getUrl(self):
    return self._url
  def setUrl(self, url):
    self._url = url
  def getHtml(self):
    return self._html
  def setHtml(self, html):
    self._html = html
  def getText(self):
    return self._text
  def setText(self, text):
    self._text = text
  def getOutputMode(self):
    return self._mode
  def setOutputMode(self, mode):
    if mode != "xml":
      raise Exception, 'Error setting output mode.'
    self._outputMode = mode
  def getCustomParameters(self):
    return self._customParameters
  def setCustomParameters(self, *values):
    self._customParameters = ""
    for i in len(values):
      self._customParameters += "&" + values[i] + "=" + urllib.quote(values[i + 1])
      i = i + 1
  def getParameterString(self):
    retString = ""
    if self._url != "":
      retString += "&url=" + urllib.quote(self._url)
    if self._html != "":
      retString += "&html=" + urllib.quote(self._html)
    if self._text != "":
      retString += "&text=" + urllib.quote(self._text)
    if self._outputMode != "":
      retString += "&outputMode=" + urllib.quote(self._outputMode)
    if self._customParameters != "":
      retString += self._customParameters
    return retString


class AlchemyAPI_NamedEntityParams(AlchemyAPI_Params):
  _disambiguate = ""
  _linkedData = ""
  _coreference = ""
  _quotations = ""
  _sourceText = ""
  _showSourceText = ""
  _maxRetrieve = ""
  _baseUrl = ""
  _cQuery = ""
  _xPath = ""
  _sentiment = ""
  def getDisambiguate(self):
    return self._disambiguate
  def setDisambiguate(self, setting):
    if setting != 1:
      if setting != 0:
        raise Exception, 'Error setting Disambiguate.'
    self._disambiguate = setting
  def getLinkedData(self):
    return self._linkedData
  def setLinkedData(self, setting):
    if setting != 1:
      if setting != 0:
        raise Exception, 'Error setting LinkedData.'
    self._linkedData = setting
  def getCoreference(self):
    return self._coreference
  def setCoreference(self, setting):
    if setting != 1:
      if setting != 0:
        raise Exception, 'Error setting Coreference.'
    self._coreference = setting
  def getQuotations(self):
    return self._quotations
  def setQuotations(self, setting):
    if setting != 1:
      if setting != 0:
        raise Exception, 'Error setting Quotations.'
    self._quotations = setting
  def getShowSourceText(self):
    return self._showSourceText
  def setShowSourceText(self, setting):
    if setting != 1:
      if setting != 0:
        raise Exception, 'Error setting ShowSourceText.'
    self._showSourceText = setting
  def getSourceText(self):
    return self._quotations
  def setSourceText(self, setting):
    if setting != 'cleaned_or_raw':
      if setting != 'cleaned':
        if setting != 'raw':
          if setting != 'cquery':
            if setting != 'xpath':
              raise Exception, 'Error setting SourceText.'
    self._sourceText = setting
  def getMaxRetrieve(self):
    return self._maxRetrieve
  def setMaxRetrieve(self, setting):
    self._maxRetrieve = setting
  def getBaseUrl(self):
    return self._baseUrl
  def setBaseUrl(self, setting):
    self._baseUrl = setting
  def getConstraintQuery(self):
    return self._cQuery
  def setConstraintQuery(self, setting):
    self._cQuery = setting
  def getXPath(self):
    return self._xPath
  def setXPath(self, setting):
    self._xPath = setting
  def getSentiment(self):
    return self._sentiment
  def setSentiment(self, setting):
    if setting != 1:
      if setting != 0:
        raise Exception, 'Error setting Sentiment.'
    self._sentiment = setting
  def getParameterString(self):
    retString = super(AlchemyAPI_NamedEntityParams, self).getParameterString()
    if self._disambiguate != "":
      retString += "&disambiguate=" + str(self._disambiguate)
    if self._linkedData != "":
      retString += "&linkedData=" + str(self._linkedData)
    if self._coreference != "":
      retString += "&coreference=" + str(self._coreference)
    if self._quotations != "":
      retString += "&quotations=" + str(self._quotations)
    if self._sourceText != "":
      retString += "&sourceText=" + urllib.quote(self._sourceText)
    if self._showSourceText != "":
      retString += "&showSourceText=" + str(self._showSourceText)
    if self._maxRetrieve != "":
      retString += "&maxRetrieve=" + str(self._maxRetrieve)
    if self._baseUrl != "":
      retString += "&baseUrl=" + urllib.quote(self._baseUrl)
    if self._cQuery != "":
      retString += "&cquery=" + urllib.quote(self._cQuery)
    if self._xPath != "":
      retString += "&xpath=" + urllib.quote(self._xPath)
    if self._sentiment != "":
      retString += "&sentiment=" + str(self._sentiment)
    return retString


class AlchemyAPI_CategoryParams(AlchemyAPI_Params):
  _sourceText = ""
  _baseUrl = ""
  _cQuery = ""
  _xPath = ""
  def getSourceText(self):
    return self._quotations
  def setSourceText(self, setting):
    if setting != 'cleaned_or_raw':
      if setting != 'cquery':
        if setting != 'xpath':
          raise Exception, 'Error setting SourceText.'
    self._sourceText = setting
  def getBaseUrl(self):
    return self._baseUrl
  def setBaseUrl(self, setting):
    self._baseUrl = setting
  def getConstraintQuery(self):
    return self._cQuery
  def setConstraintQuery(self, setting):
    self._cQuery = setting
  def getXPath(self):
    return self._xPath
  def setXPath(self, setting):
    self._xPath = setting
  def getParameterString(self):
    retString = super(AlchemyAPI_CategoryParams, self).getParameterString()
    if self._sourceText != "":
      retString += "&sourceText=" + urllib.quote(self._sourceText)
    if self._baseUrl != "":
      retString += "&baseUrl=" + urllib.quote(self._baseUrl)
    if self._cQuery != "":
      retString += "&cquery=" + urllib.quote(self._cQuery)
    if self._xPath != "":
      retString += "&xpath=" + urllib.quote(self._xPath)
    return retString


class AlchemyAPI_LanguageParams(AlchemyAPI_Params):
  _sourceText = ""
  _cQuery = ""
  _xPath = ""
  def getSourceText(self):
    return self._sourceText
  def setSourceText(self, setting):
    if setting != 'cleaned_or_raw':
      if setting != 'cleaned':
        if setting != 'raw':
          if setting != 'cquery':
            if setting != 'xpath':
              raise Exception, 'Error setting SourceText.'
    self._sourceText = setting
  def getConstraintQuery(self):
    return self._cQuery
  def setConstraintQuery(self, setting):
    self._cQuery = setting
  def getXPath(self):
    return self._xPath
  def setXPath(self, setting):
    self._xPath = setting
  def getParameterString(self):
    retString = super(AlchemyAPI_LanguageParams, self).getParameterString()
    if self._sourceText != "":
      retString += "&sourceText=" + urllib.quote(self._sourceText)
    if self._cQuery != "":
      retString += "&cquery=" + urllib.quote(self._cQuery)
    if self._xPath != "":
      retString += "&xpath=" + urllib.quote(self._xPath)
    return retString


class AlchemyAPI_ConceptParams(AlchemyAPI_Params):
  _sourceText = ""
  _showSourceText = ""
  _maxRetrieve = ""
  _cQuery = ""
  _xPath = ""
  _linkedData = ""
  def getSourceText(self):
    return self._sourceText
  def setSourceText(self, setting):
    if setting != 'cleaned_or_raw':
      if setting != 'cquery':
        if setting != 'xpath':
          raise Exception, 'Error setting SourceText.'
    self._sourceText = setting
  def getShowSourceText(self):
    return self._showSourceText
  def setShowSourceText(self, setting):
    if setting != 1:
      if setting != 0:
        raise Exception, 'Error setting ShowSourceText.'
    self._showSourceText = setting
  def getMaxRetrieve(self):
    return self._maxRetrieve
  def setMaxRetrieve(self, setting):
    self._maxRetrieve = setting
  def getLinkedData(self):
    return self._linkedData
  def setLinkedData(self, setting):
    if setting != 1:
      if setting != 0:
        raise Exception, 'Error setting LinkedData.'
    self._linkedData = setting
  def getConstraintQuery(self):
    return self._cQuery
  def setConstraintQuery(self, setting):
    self._cQuery = setting
  def getXPath(self):
    return self._xPath
  def setXPath(self, setting):
    self._xPath = setting
  def getParameterString(self):
    retString = super(AlchemyAPI_ConceptParams, self).getParameterString()
    if self._sourceText != "":
      retString += "&sourceText=" + urllib.quote(self._sourceText)
    if self._showSourceText != "":
      retString += "&showSourceText=" + str(self._showSourceText)
    if self._maxRetrieve != "":
      retString += "&maxRetrieve=" + str(self._maxRetrieve)
    if self._linkedData != "":
      retString += "&linkedData=" + str(self._linkedData)
    if self._cQuery != "":
      retString += "&cquery=" + urllib.quote(self._cQuery)
    if self._xPath != "":
      retString += "&xpath=" + urllib.quote(self._xPath)
    return retString


class AlchemyAPI_KeywordParams(AlchemyAPI_Params):
  _sourceText = ""
  _showSourceText = ""
  _sentiment = ""
  _maxRetrieve = ""
  _baseUrl = ""
  _cQuery = ""
  _xPath = ""
  _keywordExtractMode = ""
  def getSourceText(self):
    return self._sourceText
  def setSourceText(self, setting):
    if setting != 'cleaned_or_raw':
      if setting != 'cquery':
        if setting != 'xpath':
          raise Exception, 'Error setting SourceText.'
    self._sourceText = setting
  def getShowSourceText(self):
    return self._showSourceText
  def setShowSourceText(self, setting):
    if setting != 1:
      if setting != 0:
        raise Exception, 'Error setting ShowSourceText.'
    self._showSourceText = setting
  def getSentiment(self):
    return self._sentiment
  def setSentiment(self, setting):
    if setting != 1:
      if setting != 0:
        raise Exception, 'Error setting Sentiment.'
    self._sentiment = setting
  def getMaxRetrieve(self):
    return self._maxRetrieve
  def setMaxRetrieve(self, setting):
    self._maxRetrieve = setting
  def getBaseUrl(self):
    return self._baseUrl
  def setBaseUrl(self, setting):
    self._baseUrl = setting
  def getConstraintQuery(self):
    return self._cQuery
  def setConstraintQuery(self, setting):
    self._cQuery = setting
  def getXPath(self):
    return self._xPath
  def setXPath(self, setting):
    self._xPath = setting
  def getKeywordExtractMode(self):
    return self._keywordExtractMode
  def setKeywordExtractMode(self, setting):
    if setting != 'strict':
      if setting != 'normal':
        if setting != '':
          raise Exception, 'Error setting KeywordExtractMode.'
    self._keywordExtractMode = setting
  def getParameterString(self):
    retString = super(AlchemyAPI_KeywordParams, self).getParameterString()
    if self._sourceText != "":
      retString += "&sourceText=" + urllib.quote(self._sourceText)
    if self._showSourceText != "":
      retString += "&showSourceText=" + str(self._showSourceText)
    if self._maxRetrieve != "":
      retString += "&maxRetrieve=" + str(self._maxRetrieve)
    if self._baseUrl != "":
      retString += "&baseUrl=" + urllib.quote(self._baseUrl)
    if self._cQuery != "":
      retString += "&cquery=" + urllib.quote(self._cQuery)
    if self._xPath != "":
      retString += "&xpath=" + urllib.quote(self._xPath)
    if self._keywordExtractMode != "":
      retString += "&keywordExtractMode=" + urllib.quote(self._keywordExtractMode)
    if self._sentiment != "":
      retString += "&sentiment=" + str(self._sentiment)
    return retString
	
	
class AlchemyAPI_RelationParams(AlchemyAPI_Params):
  _disambiguate = ""
  _linkedData = ""
  _coreference = ""
  _entities = ""
  _sentimentExcludeEntities = ""
  _requireEntities = ""
  _sourceText = ""
  _showSourceText = ""
  _maxRetrieve = ""
  _baseUrl = ""
  _cQuery = ""
  _xPath = ""
  _sentiment = ""
  def getDisambiguate(self):
    return self._disambiguate
  def setDisambiguate(self, setting):
    if setting != 1:
      if setting != 0:
        raise Exception, 'Error setting Disambiguate.'
    self._disambiguate = setting
  def getLinkedData(self):
    return self._linkedData
  def setLinkedData(self, setting):
    if setting != 1:
      if setting != 0:
        raise Exception, 'Error setting LinkedData.'
    self._linkedData = setting
  def getCoreference(self):
    return self._coreference
  def setCoreference(self, setting):
    if setting != 1:
      if setting != 0:
        raise Exception, 'Error setting Coreference.'
    self._coreference = setting
  def getEntities(self):
    return self._entities
  def setEntities(self, setting):
    if setting != 1:
      if setting != 0:
        raise Exception, 'Error setting Entities.'
    self._entities = setting
  def getSentimentExcludeEntities(self):
    return self._sentimentExcludeEntities
  def setSentimentExcludeEntities(self, setting):
    if setting != 1:
      if setting != 0:
        raise Exception, 'Error setting SentimentExcludeEntities.'
    self._sentimentExcludeEntities = setting
  def getRequireEntities(self):
    return self._requireEntities
  def setRequireEntities(self, setting):
    if setting != 1:
      if setting != 0:
        raise Exception, 'Error setting RequireEntities.'
    self._requireEntities = setting
  def getShowSourceText(self):
    return self._showSourceText
  def setShowSourceText(self, setting):
    if setting != 1:
      if setting != 0:
        raise Exception, 'Error setting ShowSourceText.'
    self._showSourceText = setting
  def getSourceText(self):
    return self._quotations
  def setSourceText(self, setting):
    if setting != 'cleaned_or_raw':
      if setting != 'cleaned':
        if setting != 'raw':
          if setting != 'cquery':
            if setting != 'xpath':
              raise Exception, 'Error setting SourceText.'
    self._sourceText = setting
  def getMaxRetrieve(self):
    return self._maxRetrieve
  def setMaxRetrieve(self, setting):
    self._maxRetrieve = setting
  def getBaseUrl(self):
    return self._baseUrl
  def setBaseUrl(self, setting):
    self._baseUrl = setting
  def getConstraintQuery(self):
    return self._cQuery
  def setConstraintQuery(self, setting):
    self._cQuery = setting
  def getXPath(self):
    return self._xPath
  def setXPath(self, setting):
    self._xPath = setting
  def getSentiment(self):
    return self._sentiment
  def setSentiment(self, setting):
    if setting != 1:
      if setting != 0:
        raise Exception, 'Error setting Sentiment.'
    self._sentiment = setting
  def getParameterString(self):
    retString = super(AlchemyAPI_RelationParams, self).getParameterString()
    if self._disambiguate != "":
      retString += "&disambiguate=" + str(self._disambiguate)
    if self._linkedData != "":
      retString += "&linkedData=" + str(self._linkedData)
    if self._coreference != "":
      retString += "&coreference=" + str(self._coreference)
    if self._entities != "":
      retString += "&entities=" + str(self._entities)
    if self._sentimentExcludeEntities != "":
      retString += "&sentimentExcludeEntities=" + str(self._sentimentExcludeEntities)
    if self._requireEntities != "":
      retString += "&requireEntities=" + str(self._requireEntities)
    if self._sourceText != "":
      retString += "&sourceText=" + urllib.quote(self._sourceText)
    if self._showSourceText != "":
      retString += "&showSourceText=" + str(self._showSourceText)
    if self._maxRetrieve != "":
      retString += "&maxRetrieve=" + str(self._maxRetrieve)
    if self._baseUrl != "":
      retString += "&baseUrl=" + urllib.quote(self._baseUrl)
    if self._cQuery != "":
      retString += "&cquery=" + urllib.quote(self._cQuery)
    if self._xPath != "":
      retString += "&xpath=" + urllib.quote(self._xPath)
    if self._sentiment != "":
      retString += "&sentiment=" + str(self._sentiment)
    return retString

class AlchemyAPI_TextParams(AlchemyAPI_Params):
  _useMetaData = ""
  _extractLinks = ""
  def getUseMetaData(self):
    return self._useMetaData
  def setUseMetaData(self, setting):
    if setting != 1:
      if setting != 0:
        raise Exception, 'Error setting UseMetaData.'
    self._useMetaData = setting
  def getExtractLinks(self):
    return self._extractLinks
  def setExtractLinks(self, setting):
    if setting != 1:
      if setting != 0:
        raise Exception, 'Error setting ExtractLinks.'
    self._extractLinks = setting
  def getParameterString(self):
    retString = super(AlchemyAPI_TextParams, self).getParameterString()
    if self._useMetaData != "":
      retString += "&useMetaData=" + str(self._useMetaData)
    if self._extractLinks != "":
      retString += "&extractLinks=" + str(self._extractLinks)
    return retString


class AlchemyAPI_ConstraintQueryParams(AlchemyAPI_Params):
  _cQuery = ""
  def getConstraintQuery(self):
    return self._cQuery
  def setConstraintQuery(self, setting):
    self._cQuery = setting
  def getParameterString(self):
    retString = super(AlchemyAPI_ConstraintQueryParams, self).getParameterString()
    if self._cQuery != "":
      retString += "&cquery=" + urllib.quote(self._cQuery)
    return retString

class AlchemyAPI_TargetedSentimentParams(AlchemyAPI_Params):
  _showSourceText = ""
  _target = ""
  def getShowSourceText(self):
    return self._showSourceText
  def setShowSourceText(self, setting):
    if setting != 1:
      if setting != 0:
        raise Exception, 'Error setting showSourceText.'
    self._showSourceText = setting
  def getTarget(self):
    return self._target
  def setTarget(self, setting):
    self._target = setting
  def getParameterString(self):
    retString = super(AlchemyAPI_TargetedSentimentParams, self).getParameterString()
    if self._showSourceText != "":
      retString += "&showSourceText=" + str(self._showSourceText)
    if self._target != "":
      retString += "&target=" + str(self._target)
    return retString

class AlchemyAPI:
  _apiKey = ""
  _hostPrefix = "access"
  def setAPIHost(self, apiHost):
    self._hostPrefix = apiHost;
    if len(self._hostPrefix) < 2:
      raise Exception, 'Error setting API host.'
  def setAPIKey(self, apiKey):
    self._apiKey = apiKey;
    if len(self._apiKey) < 5:
      raise Exception, 'Error setting API key.'
  def loadAPIKey(self, filename):
    file = open(filename, 'r')
    line = file.readline()
    self._apiKey = line.strip();
    if len(self._apiKey) < 5:
      raise Exception, 'Error loading API key.'
  def URLGetRankedNamedEntities(self, url, namedEntityParams=None):
    self.CheckURL(url)
    if namedEntityParams == None:
      namedEntityParams = AlchemyAPI_NamedEntityParams()
    namedEntityParams.setUrl(url)
    return self.GetRequest("URLGetRankedNamedEntities", "url", namedEntityParams)
  def HTMLGetRankedNamedEntities(self, html, url, namedEntityParams=None):
    self.CheckHTML(html, url)
    if namedEntityParams == None:
      namedEntityParams = AlchemyAPI_NamedEntityParams()
    namedEntityParams.setUrl(url)
    namedEntityParams.setHtml(html)
    return self.PostRequest("HTMLGetRankedNamedEntities", "html", namedEntityParams)
  def TextGetRankedNamedEntities(self, text, namedEntityParams=None):
    self.CheckText(text)
    if namedEntityParams == None:
      namedEntityParams = AlchemyAPI_NamedEntityParams()
    namedEntityParams.setText(text)
    return self.PostRequest("TextGetRankedNamedEntities", "text", namedEntityParams)
  def URLGetRankedConcepts(self, url, conceptParams=None):
    self.CheckURL(url)
    if conceptParams == None:
      conceptParams = AlchemyAPI_ConceptParams()
    conceptParams.setUrl(url)
    return self.GetRequest("URLGetRankedConcepts", "url", conceptParams)
  def HTMLGetRankedConcepts(self, html, url, conceptParams=None):
    self.CheckHTML(html, url)
    if conceptParams == None:
      conceptParams = AlchemyAPI_ConceptParams()
    conceptParams.setUrl(url)
    conceptParams.setHtml(html)
    return self.PostRequest("HTMLGetRankedConcepts", "html", conceptParams)
  def TextGetRankedConcepts(self, text, conceptParams=None):
    self.CheckText(text)
    if conceptParams == None:
      conceptParams = AlchemyAPI_ConceptParams()
    conceptParams.setText(text)
    return self.PostRequest("TextGetRankedConcepts", "text", conceptParams)
  def URLGetRankedKeywords(self, url, keywordParams=None):
    self.CheckURL(url)
    if keywordParams == None:
      keywordParams = AlchemyAPI_KeywordParams()
    keywordParams.setUrl(url)
    return self.GetRequest("URLGetRankedKeywords", "url", keywordParams)
  def HTMLGetRankedKeywords(self, html, url, keywordParams=None):
    self.CheckHTML(html, url)
    if keywordParams == None:
      keywordParams = AlchemyAPI_KeywordParams()
    keywordParams.setUrl(url)
    keywordParams.setHtml(html)
    return self.PostRequest("HTMLGetRankedKeywords", "html", keywordParams)
  def TextGetRankedKeywords(self, text, keywordParams=None):
    self.CheckText(text)
    if keywordParams == None:
      keywordParams = AlchemyAPI_KeywordParams()
    keywordParams.setText(text)
    return self.PostRequest("TextGetRankedKeywords", "text", keywordParams)
  def URLGetLanguage(self, url, languageParams=None):
    self.CheckURL(url)
    if languageParams == None:
      languageParams = AlchemyAPI_LanguageParams()
    languageParams.setUrl(url)
    return self.GetRequest("URLGetLanguage", "url", languageParams)
  def HTMLGetLanguage(self, html, url, languageParams=None):
    self.CheckHTML(html, url)
    if languageParams == None:
      languageParams = AlchemyAPI_LanguageParams()
    languageParams.setUrl(url)
    languageParams.setHtml(html)
    return self.PostRequest("HTMLGetLanguage", "html", languageParams)
  def TextGetLanguage(self, text, languageParams=None):
    self.CheckText(text)
    if languageParams == None:
      languageParams = AlchemyAPI_LanguageParams()
    languageParams.setText(text)
    return self.PostRequest("TextGetLanguage", "text", languageParams)
  def URLGetCategory(self, url, categParams=None):
    self.CheckURL(url)
    if categParams == None:
      categParams = AlchemyAPI_CategoryParams()
    categParams.setUrl(url)
    return self.GetRequest("URLGetCategory", "url", categParams)
  def HTMLGetCategory(self, html, url, categParams=None):
    self.CheckHTML(html, url)
    if categParams == None:
      categParams = AlchemyAPI_CategoryParams()
    categParams.setUrl(url)
    categParams.setHtml(html)
    return self.PostRequest("HTMLGetCategory", "html", categParams)
  def TextGetCategory(self, text, categParams=None):
    self.CheckText(text)
    if categParams == None:
      categParams = AlchemyAPI_CategoryParams()
    categParams.setText(text)
    return self.PostRequest("TextGetCategory", "text", categParams)
  def URLGetText(self, url, textParams=None):
    self.CheckURL(url)
    if textParams == None:
      textParams = AlchemyAPI_TextParams()
    textParams.setUrl(url)
    return self.GetRequest("URLGetText", "url", textParams)
  def HTMLGetText(self, html, url, textParams=None):
    self.CheckHTML(html, url)
    if textParams == None:
      textParams = AlchemyAPI_TextParams()
    textParams.setUrl(url)
    textParams.setHtml(html)
    return self.PostRequest("HTMLGetText", "html", textParams)
  def URLGetRawText(self, url, baseParams=None):
    self.CheckURL(url)
    if baseParams == None:
      baseParams = AlchemyAPI_Params()
    baseParams.setUrl(url)
    return self.GetRequest("URLGetRawText", "url", baseParams)
  def HTMLGetRawText(self, html, url, baseParams=None):
    self.CheckHTML(html, url)
    if baseParams == None:
      baseParams = AlchemyAPI_Params()
    baseParams.setUrl(url)
    baseParams.setHtml(html)
    return self.PostRequest("HTMLGetRawText", "html", baseParams)
  def URLGetTitle(self, url, baseParams=None):
    self.CheckURL(url)
    if baseParams == None:
      baseParams = AlchemyAPI_Params()
    baseParams.setUrl(url)
    return self.GetRequest("URLGetTitle", "url", baseParams)
  def HTMLGetTitle(self, html, url, baseParams=None):
    self.CheckHTML(html, url)
    if baseParams == None:
      baseParams = AlchemyAPI_Params()
    baseParams.setUrl(url)
    baseParams.setHtml(html)
    return self.PostRequest("HTMLGetTitle", "html", baseParams)
  def URLGetFeedLinks(self, url, baseParams=None):
    self.CheckURL(url)
    if baseParams == None:
      baseParams = AlchemyAPI_Params()
    baseParams.setUrl(url)
    return self.GetRequest("URLGetFeedLinks", "url", baseParams)
  def HTMLGetFeedLinks(self, html, url, baseParams=None):
    self.CheckHTML(html, url)
    if baseParams == None:
      baseParams = AlchemyAPI_Params()
    baseParams.setUrl(url)
    baseParams.setHtml(html)
    return self.PostRequest("HTMLGetFeedLinks", "html", baseParams)
  def URLGetMicroformats(self, url, baseParams=None):
    self.CheckURL(url)
    if baseParams == None:
      baseParams = AlchemyAPI_Params()
    baseParams.setUrl(url)
    return self.GetRequest("URLGetMicroformatData", "url", baseParams)
  def HTMLGetMicroformats(self, html, url, baseParams=None):
    self.CheckHTML(html, url)
    if baseParams == None:
      baseParams = AlchemyAPI_Params()
    baseParams.setUrl(url)
    baseParams.setHtml(html)
    return self.PostRequest("HTMLGetMicroformatData", "html", baseParams)
  def URLGetConstraintQuery(self, url, query, cQueryParams=None):
    self.CheckURL(url)
    if len(query) < 2:
      raise Exception, 'Invalid constraint query specified.'
    if cQueryParams == None:
      cQueryParams = AlchemyAPI_ConstraintQueryParams()
    cQueryParams.setUrl(url)
    cQueryParams.setConstraintQuery(query)
    return self.GetRequest("URLGetConstraintQuery", "url", cQueryParams)
  def HTMLGetConstraintQuery(self, html, url, query, cQueryParams=None):
    self.CheckHTML(html, url)
    if len(query) < 2:
      raise Exception, 'Invalid constraint query specified.'
    if cQueryParams == None:
      cQueryParams = AlchemyAPI_ConstraintQueryParams()
    cQueryParams.setUrl(url)
    cQueryParams.setHtml(html)
    cQueryParams.setConstraintQuery(query)
    return self.PostRequest("HTMLGetConstraintQuery", "html", cQueryParams)
  def URLGetTextSentiment(self, url, baseParams=None):
    self.CheckURL(url)
    if baseParams == None:
      baseParams = AlchemyAPI_Params()
    baseParams.setUrl(url)
    return self.GetRequest("URLGetTextSentiment", "url", baseParams)
  def HTMLGetTextSentiment(self, html, url, baseParams=None):
    self.CheckHTML(html, url)
    if baseParams == None:
      baseParams = AlchemyAPI_Params()
    baseParams.setUrl(url)
    baseParams.setHtml(html)
    return self.PostRequest("HTMLGetTextSentiment", "html", baseParams)
  def TextGetTextSentiment(self, text, baseParams=None):
    self.CheckText(text)
    if baseParams == None:
      baseParams = AlchemyAPI_Params()
    baseParams.setText(text)
    return self.PostRequest("TextGetTextSentiment", "text", baseParams)
  def URLGetTargetedSentiment(self, url, target, targetedSentimentParams=None):
    self.CheckURL(url)
    if targetedSentimentParams == None:
      targetedSentimentParams = AlchemyAPI_TargetedSentimentParams()
    targetedSentimentParams.setUrl(url)
    targetedSentimentParams.setTarget(target)
    return self.GetRequest("URLGetTargetedSentiment", "url", targetedSentimentParams)
  def HTMLGetTargetedSentiment(self, html, url, target, targetedSentimentParams=None):
    self.CheckHTML(html, url)
    if targetedSentimentParams == None:
      targetedSentimentParams = AlchemyAPI_TargetedSentimentParams()
    targetedSentimentParams.setUrl(url)
    targetedSentimentParams.setHtml(html)
    targetedSentimentParams.setTarget(target)
    return self.PostRequest("HTMLGetTargetedSentiment", "html", targetedSentimentParams)
  def TextGetTargetedSentiment(self, text, target, targetedSentimentParams=None):
    self.CheckText(text)
    if targetedSentimentParams == None:
      targetedSentimentParams = AlchemyAPI_TargetedSentimentParams()
    targetedSentimentParams.setText(text)
    targetedSentimentParams.setTarget(target)
    return self.PostRequest("TextGetTargetedSentiment", "text", targetedSentimentParams)
  def URLGetRelations(self, url, relationParams=None):
    self.CheckURL(url)
    if relationParams == None:
      relationParams = AlchemyAPI_RelationParams()
    relationParams.setUrl(url)
    return self.GetRequest("URLGetRelations", "url", relationParams)
  def HTMLGetRelations(self, html, url, relationParams=None):
    self.CheckHTML(html, url)
    if relationParams == None:
      relationParams = AlchemyAPI_RelationParams()
    relationParams.setUrl(url)
    relationParams.setHtml(html)
    return self.PostRequest("HTMLGetRelations", "html", relationParams)
  def TextGetRelations(self, text, relationParams=None):
    self.CheckText(text)
    if relationParams == None:
      relationParams = AlchemyAPI_RelationParams()
    relationParams.setText(text)
    return self.PostRequest("TextGetRelations", "text", relationParams)
  def URLGetAuthor(self, url, baseParams=None):
    self.CheckURL(url)
    if baseParams == None:
      baseParams = AlchemyAPI_Params()
    baseParams.setUrl(url)
    return self.GetRequest("URLGetAuthor", "url", baseParams)
  def HTMLGetAuthor(self, html, url, baseParams=None):
    self.CheckHTML(html, url)
    if baseParams == None:
      baseParams = AlchemyAPI_Params()
    baseParams.setUrl(url)
    baseParams.setHtml(html)
    return self.PostRequest("HTMLGetAuthor", "html", baseParams)
  def CheckText(self, text):
    if len(self._apiKey) < 5:
      raise Exception, 'Please load an API key.'
    if len(text) < 5:
      raise Exception, 'Please specify some text to analyze.'
  def CheckHTML(self, html, url):
    if len(self._apiKey) < 5:
      raise Exception, 'Please load an API key.'
    if len(html) < 10:
      raise Exception, 'Please specify a HTML document to analyze.'
    if len(url) < 10:
      raise Exception, 'Please specify a URL to analyze.'
  def CheckURL(self, url):
    if len(self._apiKey) < 5:
      raise Exception, 'Please load an API key.'
    if len(url) < 10:
      raise Exception, 'Please specify a URL to analyze.'
  def PostRequest(self, apiCall, apiPrefix, paramObject):
    endpoint = 'http://' + self._hostPrefix + '.alchemyapi.com/calls/' + apiPrefix + '/' + apiCall
    argText = 'apikey=' + self._apiKey + paramObject.getParameterString()
    handle = urllib.urlopen(endpoint, argText)
    result = handle.read()
    handle.close()
    xpathQuery = './/status'
    nodes = etree.fromstring(result).find(xpathQuery)
    if nodes.text != "OK":
      raise Exception, 'Error making API call.'
    return result
  def GetRequest(self, apiCall, apiPrefix, paramObject):
    endpoint = 'http://' + self._hostPrefix + '.alchemyapi.com/calls/' + apiPrefix + '/' + apiCall
    endpoint += '?apikey=' + self._apiKey + paramObject.getParameterString()
    handle = urllib.urlopen(endpoint)
    result = handle.read()
    handle.close()
    xpathQuery = './/status'
    nodes = etree.fromstring(result).find(xpathQuery)
    if nodes.text != "OK":
      raise Exception, 'Error making API call.'
    return result
