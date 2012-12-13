'''
Created on Dec 2, 2012

@author: zudec
'''


# Fetch data from Twitter
import tweetstream
import sentiment.AlchemyAPI as AlchemyAPI

import thread
import time
import stock.ystockquote as ystockquote
import re
import logging


logger = logging.getLogger('Stock-Predictor')
#hdlr1 = logging.FileHandler('../Stock-Predictor.log')
hdlr2 = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
#hdlr1.setFormatter(formatter)
hdlr2.setFormatter(formatter)
#logger.addHandler(hdlr1) 
logger.addHandler(hdlr2) 
logger.setLevel(logging.DEBUG)



STOCK_GUAGE_TIME_INTERVAL_DIFFERENCE = 30



class Predictor(object):
    links_repository = []    
    companies_ticker = {"JPMorgan":"JPM", "AIG":"AIG", "HSBC":"HBC", "INTEL":"INTC", "Agilent": "A", "Alcoa ": "AA", "Apple": "AAPL", "AmerisourceBergen ": "ABC", "Abbott Laboratories": "ABT", "ACE Limited": "ACE", "Accenture": "ACN", "Adobe Systems ": "ADBE", "Adobe": "ADBE", "Analog Devices ": "ADI", "Archer-Daniels-Midland": "ADM", "Automatic Data Processing": "ADP", "ADP": "ADP", "Autodesk ": "ADSK", "ADT ": "ADT", "Ameren ": "AEE", "American Electric Power": "AEP", "AES ": "AES", "Aetna ": "AET", "AFLAC ": "AFL", "Allergan ": "AGN", "American Intl Group ": "AIG", "Apartment Investment & Mgmt": "AIV", "Apartment Investment": "AIV", "Assurant ": "AIZ", "Akamai Technologies ": "AKAM", "Akamai": "AKAM", "Allstate ": "ALL", "Altera ": "ALTR", "Alexion Pharmaceuticals": "ALXN", "Alexion": "ALXN", "Applied Materials ": "AMAT", "Advanced Micro Devices": "AMD", "AMD": "AMD", "Amgen ": "AMGN", "Ameriprise Financial": "AMP", "American Tower": "AMT", "Amazoncom ": "AMZN", "Amazon": "AMZN", "AutoNation ": "AN", "Abercrombie & Fitch Company": "ANF", "Abercrombie": "ANF", "Aon plc": "AON", "Apache": "APA", "Anadarko Petroleum ": "APC", "Air Products & Chemicals ": "APD", "Amphenol": "APH", "Apollo Group ": "APOL", "Airgas ": "ARG", "Allegheny Technologies ": "ATI", "AvalonBay Communities, ": "AVB", "Avon Products": "AVP", "Avon": "AVP", "Avery Dennison ": "AVY", "American Express Co": "AXP", "American Express": "AXP", "Amex": "AXP", "AutoZone ": "AZO", "Boeing Company": "BA", "Bank of America ": "BAC", "BofA": "BAC", "Baxter International ": "BAX", "Bed Bath & Beyond": "BBBY", "BB&T ": "BBT", "Best Buy": "BBY", "Bard": "BCR", "Becton Dickinson": "BDX", "Beam ": "BEAM", "Franklin Resources": "BEN", "Brown-Forman ": "BF.B", "Baker Hughes ": "BHI", "Big Lots ": "BIG", "BIOGEN IDEC ": "BIIB", "The Bank of New York Mellon ": "BK", "BlackRock": "BLK", "Ball ": "BLL", "BMC Software": "BMC", "Bemis Company": "BMS", "Bristol-Myers Squibb": "BMY", "Broadcom ": "BRCM", "Berkshire Hathaway": "BRK.B", "Berkshire": "BRK.B", "Boston Scientific": "BSX", "Peabody Energy": "BTU", "BorgWarner": "BWA", "Boston Properties": "BXP", "Citigroup ": "C", " CA ": "CA", "ConAgra Foods ": "CAG", "ConAgra": "CAG", "Cardinal Health ": "CAH", "Cameron International ": "CAM", "Caterpillar ": "CAT", "Chubb ": "CB", "CBRE Group": "CBG", "CBS ": "CBS", "Coca-Cola": "CCE", "Coke": "CCE", "Crown Castle": "CCI", "Carnival ": "CCL", "Celgene ": "CELG", "Cerner": "CERN", "CF Industries Holdings ": "CF", "Carefusion": "CFN", "Chesapeake Energy": "CHK", "C H Robinson Worldwide": "CHRW", "CIGNA ": "CI", "Cinnati Financial": "CINF", "Colgate-Palmolive": "CL", "Cliffs Natural Resources": "CLF", "The Clorox Company": "CLX", "Comerica ": "CMA", "Comcast ": "CMCSA", "CME Group ": "CME", "Chipotle": "CMG", "Cummins ": "CMI", "CMS Energy": "CMS", "CenterPoint Energy": "CNP", "CONSOL Energy ": "CNX", "Capital One Financial": "COF", "CapitalOne": "COF", "Capital One": "COF", "Cabot Oil & Gas": "COG", "Coach ": "COH", "Rockwell Collins": "COL", "ConocoPhillips": "COP", "Costco": "COST", "Covidien": "COV", "Campbell Soup": "CPB", "Campbell's": "CPB", "Salesforce.com": "CRM", "Salesforce": "CRM", "Computer Sciences ": "CSC", "Cisco": "CSCO", "Cisco Systems": "CSCO", "CSX ": "CSX", "Cintas ": "CTAS", "CenturyLink ": "CTL", "Cognizant Technology Solutions": "CTSH", "Citrix Systems": "CTXS", "Cablevision Systems ": "CVC", "Coventry Health Care ": "CVH", "CVS Caremark ": "CVS", "Chevron ": "CVX", "Dominion Resources": "D", "Du Pont": "DD", "Deere & Co": "DE", "Dell ": "DELL", "Dean Foods": "DF", "Discover Financial Services": "DFS", "Dollar General": "DG", "Quest Diagnostics": "DGX", "D R Horton": "DHI", "Danaher ": "DHR", "Walt Disney": "DIS", "Disney": "DIS", "Discovery Communications": "DISCA", "Dollar Tree": "DLTR", "Dun & Bradstreet": "DNB", "Denbury Resources ": "DNR", "Diamond Offshore Drilling": "DO", "Dover ": "DOV", "Dow Chemical": "DOW", "Dow ": "DOW", "Dr Pepper Snapple Group": "DPS", "Darden Restaurants": "DRI", "DTE Energy Co": "DTE", "DirecTV": "DTV", "Duke Energy": "DUK", "DaVita ": "DVA", "Devon Energy ": "DVN", "Electronic Arts": "EA", " EA ": "EA", "eBay ": "EBAY", "Ecolab ": "ECL", "Consolidated Edison": "ED", "Equifax ": "EFX", "Edison Int'l": "EIX", "Estee Lauder": "EL", "EMC ": "EMC", "Eastman Chemical": "EMN", "Emerson Electric": "EMR", "EOG Resources": "EOG", "Equity Residential": "EQR", "EQT ": "EQT", "Express Scripts": "ESRX", "Ensco plc": "ESV", "E-Trade": "ETFC", "Eaton ": "ETN", "Entergy ": "ETR", "Edwards Lifesciences": "EW", "Exelon ": "EXC", "Expeditors": "EXPD", "Expedia ": "EXPE", "Ford Motor": "F", "Fastenal": "FAST", "Freeport-McMoran Cp & Gld": "FCX", "Family Dollar Stores": "FDO", "FedEx ": "FDX", "FirstEnergy ": "FE", "F5 Networks": "FFIV", "First Horizon National": "FHN", "Federated Investors ": "FII", "Fidelity National Information Services": "FIS", "Fiserv ": "FISV", "Fifth Third Ban": "FITB", "FLIR Systems": "FLIR", "Fluor ": "FLR", "Flowserve ": "FLS", "FMC ": "FMC", "Fossil": "FOSL", "Forest Laboratories": "FRX", "First Solar ": "FSLR", "FMC Technologies ": "FTI", "Frontier Communications": "FTR", "Frontier": "FTR", "AGL Resources ": "GAS", "Gannett": "GCI", "General Dynamics": "GD", "General Electric": "GE", "Gilead Sciences": "GILD", "General Mills": "GIS", "Corning ": "GLW", "GameStop ": "GME", "Genworth Financial ": "GNW", "Google ": "GOOG", "Genuine Parts": "GPC", "Gap (The)": "GPS", "The Gap": "GPS", "Goldman Sachs Group": "GS", "Goldman Sachs": "GS", "Goodyear Tire & Rubber": "GT", "Goodyear": "GT", "Grainger (WW) ": "GWW", "Halliburton": "HAL", "Harman Int'l Industries": "HAR", "Hasbro ": "HAS", "Huntington Bancshares": "HBAN", "Hudson City Ban": "HCBK", "Health Care REIT": "HCN", "HCP ": "HCP", "Home Depot": "HD", "Hess ": "HES", "Hartford Financial SvcGp": "HIG", "Heinz": "HNZ", "Harley-Davidson": "HOG", "Honeywell": "HON", "Starwood Hotels & Resorts": "HOT", "Starwood": "HOT", "Helmerich & Payne": "HP", "Hewlett-Packard": "HPQ", "Block H&R": "HRB", "Hormel Foods ": "HRL", "Harris ": "HRS", "Hospira ": "HSP", "Host Hotels & Resorts": "HST", "The Hershey Company": "HSY", "Hershey": "HSY", "Humana ": "HUM", "International Bus Machines": "IBM", "IntercontinentalExchange ": "ICE", "International Flav/Frag": "IFF", "International Game Technology": "IGT", "Intel ": "INTC", "Intuit ": "INTU", "International Paper": "IP", "Interpublic Group": "IPG", "Ingersoll-Rand PLC": "IR", "Iron Mountain orporated": "IRM", "Intuitive Surgical ": "ISRG", "Illinois Tool Works": "ITW", "Invesco Ltd": "IVZ", "Jabil Circuit": "JBL", "Johnson Controls": "JCI", "Penney (JC)": "JCP", "JC Penney": "JCP", "JDS Uniphase ": "JDSU", "Jacobs Engineering Group": "JEC", "Johnson & Johnson": "JNJ", "J&J": "JNJ", "Juniper Networks": "JNPR", "Joy Global ": "JOY", "JPMorgan Chase & Co": "JPM", "JPMorgan Chase": "JPM", "JPMorgan": "JPM", "Nordstrom": "JWN", "Kellogg Co": "K", "Key": "KEY", "Kimco Realty": "KIM", "KLA-Tencor ": "KLAC", "Kimberly-Clark": "KMB", "Kinder Morgan": "KMI", "Carmax ": "KMX", "Coca Cola": "KO", "Kroger Co": "KR", "Kraft Foods Group": "KRFT", "Kraft": "KRFT", "Kohl's ": "KSS", "Loews ": "L", "Leggett & Platt": "LEG", "Lennar ": "LEN", "Laboratory  of America Holding": "LH", "Life Technologies": "LIFE", "L-3 Communications": "LLL", "Linear Technology ": "LLTC", "Lilly (Eli) & Co": "LLY", "Eli Lilly": "LLY", "Legg Mason": "LM", "Lockheed Martin ": "LMT", "Loln National": "LNC", "Lorillard ": "LO", "Lowe's": "LOW", "Lam Research": "LRCX", "LSI ": "LSI", "Limited Brands ": "LTD", "Leucadia National ": "LUK", "Southwest Airlines": "LUV", "LyondellBasell": "LYB", "Macy's ": "M", "Mastercard ": "MA", "Marriott": "MAR", "Masco ": "MAS", "Mattel ": "MAT", "McDonald's ": "MCD", "Microchip Technology": "MCHP", "McKesson ": "MCK", "Moody's ": "MCO", "Mondelez International": "MDLZ", "Medtronic ": "MDT", "MetLife ": "MET", "McGraw-Hill": "MHP", "Mead Johnson": "MJN", "McCormick & Co": "MKC", "Marsh & McLennan": "MMC", "3M": "MMM", "Monster Beverage": "MNST", "Altria Group ": "MO", "Molex ": "MOLX", "Monsanto": "MON", "The Mosaic Company": "MOS", "Marathon Petroleum": "MPC", "Merck & Co": "MRK", "Marathon Oil ": "MRO", "Morgan Stanley": "MS", "Microsoft ": "MSFT", "Motorola Solutions ": "MSI", "M&T Bank ": "MTB", "Micron Technology": "MU", "Murphy Oil": "MUR", "MeadWestvaco ": "MWV", "Mylan ": "MYL", "Noble Energy ": "NBL", "Nabors Industries Ltd": "NBR", "NASDAQ OMX Group": "NDAQ", "Noble ": "NE", "NextEra Energy Resources": "NEE", "Newmont Mining  (Hldg Co)": "NEM", "NetFlix ": "NFLX", "Newfield": "NFX", "NiSource ": "NI", "NIKE ": "NKE", "Northrop Grumman ": "NOC", "National Oilwell Varco ": "NOV", "NRG Energy": "NRG", "Norfolk Southern ": "NSC", "NetApp": "NTAP", "Northern Trust ": "NTRS", "Northeast Utilities": "NU", "Nucor ": "NUE", "Nvidia ": "NVDA", "Newell Rubbermaid": "NWL", "News ": "NWSA", "NYSE Euronext": "NYX", "Owens-Illinois ": "OI", "ONEOK": "OKE", "Omnicom Group": "OMC", "Oracle ": "ORCL", "O'Reilly Automotive": "ORLY", "Occidental Petroleum": "OXY", "Paychex ": "PAYX", "People's United Bank": "PBCT", "Pitney-Bowes": "PBI", "PACCAR ": "PCAR", "PG&E ": "PCG", "Plum Creek Timber": "PCL", "Priceline.com ": "PCLN", "Precision Castparts": "PCP", "MetroPCS Communications ": "PCS", "Patterson Companies": "PDCO", "Public Serv Enterprise ": "PEG", "PepsiCo ": "PEP", "Pet Smart": "PETM", "Pfizer ": "PFE", "Pripal Financial Group": "PFG", "Procter & Gamble": "PG", "Progressive ": "PGR", "Parker-Hannifin": "PH", "Pulte Homes ": "PHM", "PerkinElmer": "PKI", "ProLogis": "PLD", "Pall ": "PLL", "Philip Morris": "PM", "PNC Financial Services": "PNC", "Pentair": "PNR", "Pinnacle West Capital": "PNW", "Pepco ": "POM", "PPG ": "PPG", "PPL ": "PPL", "Perrigo": "PRGO", "Prudential Financial": "PRU", "Public Storage": "PSA", "Phillips 66": "PSX", "Quanta Services ": "PWR", "Praxair ": "PX", "Pioneer Natural Resources": "PXD", "QUALCOMM ": "QCOM", "QEP Resources": "QEP", "Ryder System": "R", "Reynolds American ": "RAI", "Rowan": "RDC", "Regions": "RF", "Robert Half": "RHI", "Red Hat ": "RHT", "Polo Ralph Lauren ": "RL", "Rockwell Automation ": "ROK", "Roper Industries": "ROP", "Ross Stores ": "ROST", "Range Resources ": "RRC", "RR Donnelley & Sons": "RRD", "Republic Services ": "RSG", "Raytheon": "RTN", "Sprint Nextel ": "S", "SAIC": "SAI", "Starbucks ": "SBUX", "SCANA ": "SCG", "Charles Schwab": "SCHW", "Spectra Energy ": "SE", "New Sealed Air": "SEE", "Sherwin-Williams": "SHW", "Sigma-Aldrich": "SIAL", "Smucker (JM)": "SJM", "Schlumberger": "SLB", "SLM ": "SLM", "Snap-On ": "SNA", "SanDisk ": "SNDK", "Scripps Networks Interactive ": "SNI", "Southern": "SO", "Simon Property Group ": "SPG", "Staples ": "SPLS", "Stericycle ": "SRCL", "Sempra Energy": "SRE", "SunTrust Banks": "STI", "St Jude Medical": "STJ", "State Street ": "STT", "Seagate Technology": "STX", "Constellation Brands": "STZ", "Stanley Black & Decker": "SWK", "Southwestern Energy": "SWN", "Safeway ": "SWY", "Stryker ": "SYK", "Symantec ": "SYMC", "Sysco ": "SYY", "AT&T ": "T", "Molson Coors Brewing Company": "TAP", "Teradata ": "TDC", "TECO Energy": "TE", "Integrys Energy Group ": "TEG", "TE Connectivity Ltd": "TEL", "Teradyne ": "TER", "Target ": "TGT", "Tenet Healthcare ": "THC", "Titanium Metals ": "TIE", "Tiffany": "TIF", "TJX Companies ": "TJX", "Torchmark ": "TMK", "Thermo Fisher Scientific": "TMO", "TripAdvisor": "TRIP", "T Rowe Price Group": "TROW", "The Travelers Companies ": "TRV", "Tyson Foods": "TSN", "Tesoro Petroleum Co": "TSO", "Total System Services": "TSS", "Time Warner Cable ": "TWC", "Time Warner ": "TWX", "Texas Instruments": "TXN", "Textron ": "TXT", "Tyco International": "TYC", "United Health Group ": "UNH", "Unum Group": "UNM", "Union Pacific": "UNP", "United Parcel Service": "UPS", "Urban Outfitters": "URBN", "US Ban": "USB", "United Technologies": "UTX", "Visa ": "V", "Varian Medical Systems": "VAR", "VF ": "VFC", "Viacom ": "VIAB", "Valero Energy": "VLO", "Vulcan Materials": "VMC", "Vornado Realty Trust": "VNO", "Verisign ": "VRSN", "Ventas ": "VTR", "Verizon Communications": "VZ", "Walgreen Co": "WAG", "Waters ": "WAT", "Western Digital": "WDC", "Wisconsin Energy ": "WEC", "Wells Fargo": "WFC", "Whole Foods": "WFM", "Whirlpool ": "WHR", "Windstream ": "WIN", "WellPoint ": "WLP", "Waste Management ": "WM", "Williams Cos": "WMB", "Wal-Mart": "WMT", "Watson Pharmaceuticals": "WPI", "Washington Post": "WPO", "WPX Energy": "WPX", "Western Union": "WU", "Weyerhaeuser ": "WY", "Wyndham Worldwide": "WYN", "Wynn Resorts": "WYNN", "United States Steel ": "X", "Xcel Energy ": "XEL", "XL Capital": "XL", "Xilinx ": "XLNX", "Exxon Mobil ": "XOM", "Dentsply International": "XRAY", "Xerox ": "XRX", "Xylem ": "XYL", "Yahoo ": "YHOO", "Yum! Brands ": "YUM", "Zions Ban": "ZION", "Zimmer Holdings": "ZMH"}
    def perform_analysis(self, newsId, company_name, news_link):
        
        sentiment, sentiment_score = self.perform_sentiment_analysis(company_name, news_link)
        
      
        # If sentiment is positive, perform financial analysis, if not, ignore
     
        try:
            thread.start_new_thread(Predictor.perform_financial_analysis, (Predictor(), newsId, company_name, sentiment, sentiment_score))
        except:
            logger.error("Error: unable to start thread")
       
    


# Define a function for the thread
    def perform_sentiment_analysis(self, company_name, news_link):
        alchemyObj = AlchemyAPI.AlchemyAPI()
        # Load the API key from disk.
        alchemyObj.loadAPIKey("api_key.txt");
        # Extract sentiment from a web URL.
        result = alchemyObj.URLGetTextSentiment(news_link);
        #print result
        
        result = re.findall("<type>(.*)</type>|<score>(.*)</score>", result)
        if(result):
            sentiment_type = result[0][0]
            score = result[1][1]
        else:
            thread.exit()
        
        return sentiment_type, score
            



    def perform_financial_analysis(self, newsId, company_name, sentiment, sentiment_score):
        # Stubbing dummy quote, but ideally get hold of the right stock and lookup price

       
        #before
        for i in range(8):
            
            if i == 0:
                
                current_price = ystockquote.get_price(company_name)
            
            #print newsId,company_name,strftime("%Y-%m-%d %H:%M:%S", gmtime()),sentiment,sentiment_score,current_price
            #Sleeping for some time before recording the time again
            time.sleep(STOCK_GUAGE_TIME_INTERVAL_DIFFERENCE)
            #after
            new_price = ystockquote.get_price(company_name)
            
            logger.info('[DATA] : %s,%s,%s,%s,%s,%s,%s', str(newsId), str(company_name), str(time.ctime()), str(sentiment), str(sentiment_score), str(current_price), str(new_price))
            with open("../Stock-Predictor.log", "a") as f:
                f.write(str(newsId) + " " + str(company_name) + " " + str(time.ctime()) + " " + str(sentiment) + " " + str(sentiment_score) + " " + str(current_price) + " " + str(new_price) + "\n")
        # Kick off another thread that will fetch the price of the same quote after 5 mins.
     
companies = []

def checkIfValidTweet(tweetData):
        news_link = ''
        company_name = 'DUMMY'
        # Check if the news link is about a news source we care about
        
        # search the tweet for any of the
        for key, value in Predictor.companies_ticker.iteritems():
            match = re.findall(key, tweetData, re.I)       
            if match:
                logger.debug("Company name matched : %s ", key)
                company_name = value
       
        link_exists = re.search("http", tweetData)
        if link_exists:
            news_link = re.search("(?P<url>(http|https)?://[^\s]+)", tweetData).group("url")
            logger.debug("Tweet with a link %s ", tweetData)
    
        # Parse the link out of the tweet
    
        # Check if the new tweet is part of already parsed tweet. Don't do analysis again
    
        if((news_link not in Predictor.links_repository) and news_link != '' and company_name != 'DUMMY'):
            Predictor.links_repository.append(news_link)
                # Navigate to the new link
            return True , company_name, news_link
        else :
            return False, company_name, ''
    
    
    
    

words = []
people = [1652541]
locations = []   

stream = tweetstream.FilterStream("PDSStern", "rebeccaBlack", track=words, follow=people, locations=locations)
logger.debug("Connected to Reuters twitter stream and listening..")

#test_tweet_text = "U.S. to sell rest of AIG stock, ending $182 billion rescue http://t.co/BSbT9ezC"  
#tweet_text = tweet['text']
for tweet in stream:
#while True:
     
    
    logger.debug("Incoming tweet: %s", tweet['text'])
    isValidTweet, company_ticker_name, news_link = checkIfValidTweet(tweet['text'])
    
    if(isValidTweet):
        
        # Create a unique id and keep track 
        uniqueId = str(time.time())
        newsId = uniqueId.replace(".", "")

        # Spawn a new thread for sentiment analysis and 'trade' engine 
        try:
            thread.start_new_thread(Predictor.perform_analysis, (Predictor(), newsId, company_ticker_name, news_link))
        except:
            logger.error("Error: unable to start thread")

    else :
        logger.debug("Useless Tweet: %s", tweet['text'])     

    # Once previous action is done, kick off another thread to look for stock price in 5 mins and document 

