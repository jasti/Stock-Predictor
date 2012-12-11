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
hdlr1 = logging.FileHandler('../Stock-Predictor.log')
hdlr2=logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr1.setFormatter(formatter)
hdlr2.setFormatter(formatter)
logger.addHandler(hdlr1) 
logger.addHandler(hdlr2) 
logger.setLevel(logging.DEBUG)



STOCK_GUAGE_TIME_INTERVAL_DIFFERENCE = 5



class Predictor(object):
    links_repository = []    
    companies_ticker = {"3M ": "MMM", "ACE Limited": "ACE", "Abbott Laboratories": "ABT", "Abercrombie & Fitch Company A": "ANF", "Accenture": "ACN", "Adobe Systems ": "ADBE", "ADT Corp": "ADT", "Advanced Micro Devices": "AMD", "AES Corp": "AES", "Aetna ": "AET", "AFLAC ": "AFL", "Agilent Technologies ": "A", "AGL Resources ": "GAS", "Air Products & Chemicals ": "APD", "Airgas ": "ARG", "Akamai Technologies ": "AKAM", "Alcoa ": "AA", "Alexion Pharmaceuticals": "ALXN", "Allegheny Technologies ": "ATI", "Allergan ": "AGN", "Allstate Corp": "ALL", "Altera Corp": "ALTR", "Altria Group ": "MO", "Amazon.com ": "AMZN", "Ameren Corp": "AEE", "American Electric Power": "AEP", "American Express ": "AXP", "American Intl Group ": "AIG", "American Tower Corp A": "AMT", "Ameriprise Financial": "AMP", "AmerisourceBergen Corp": "ABC", "Amgen ": "AMGN", "Amphenol Corp A": "APH", "Anadarko Petroleum Corp": "APC", "Analog Devices ": "ADI", "Aon plc": "AON", "Apache Corporation": "APA", "Apartment Investment & Mgmt": "AIV", "Apollo Group ": "APOL", "Apple ": "AAPL", "Applied Materials ": "AMAT", "Archer-Daniels-Midland ": "ADM", "Assurant ": "AIZ", "AT&T ": "T", "Autodesk ": "ADSK", "Automatic Data Processing": "ADP", "AutoNation ": "AN", "AutoZone ": "AZO", "AvalonBay Communities, ": "AVB", "Avery Dennison Corp": "AVY", "Avon Products": "AVP", "Baker Hughes ": "BHI", "Ball Corp": "BLL", "Bank of America Corp": "BAC", "The Bank of New York Mellon Corp.": "BK", "Bard (C.R.) ": "BCR", "Baxter International ": "BAX", "BB&T Corporation": "BBT", "Beam ": "BEAM", "Becton Dickinson": "BDX", "Bed Bath & Beyond": "BBBY", "Bemis Company": "BMS", "Berkshire Hathaway": "BRK.B", "Best Buy  ": "BBY", "Big Lots ": "BIG", "BIOGEN IDEC ": "BIIB", "BlackRock": "BLK", "Block H&R": "HRB", "BMC Software": "BMC", "Boeing Company": "BA", "BorgWarner": "BWA", "Boston Properties": "BXP", "Boston Scientific": "BSX", "Bristol-Myers Squibb": "BMY", "Broadcom Corporation": "BRCM", "Brown-Forman Corporation": "BF.B", "C. H. Robinson Worldwide": "CHRW", "CA, ": "CA", "Cablevision Systems Corp.": "CVC", "Cabot Oil & Gas": "COG", "Cameron International Corp.": "CAM", "Campbell Soup": "CPB", "Capital One Financial": "COF", "Cardinal Health ": "CAH", "Carefusion": "CFN", "Carmax ": "KMX", "Carnival Corp.": "CCL", "Caterpillar ": "CAT", "CBRE Group": "CBG", "CBS Corp.": "CBS", "Celgene Corp.": "CELG", "CenterPoint Energy": "CNP", "CenturyLink ": "CTL", "Cerner": "CERN", "CF Industries Holdings ": "CF", "Charles Schwab": "SCHW", "Chesapeake Energy": "CHK", "Chevron Corp.": "CVX", "Chipotle Mexican Grill": "CMG", "Chubb Corp.": "CB", "CIGNA Corp.": "CI", "Cincinnati Financial": "CINF", "Cintas Corporation": "CTAS", "Cisco Systems": "CSCO", "Citigroup ": "C", "Citrix Systems": "CTXS", "Cliffs Natural Resources": "CLF", "The Clorox Company": "CLX", "CME Group ": "CME", "CMS Energy": "CMS", "Coach ": "COH", "Coca Cola ": "KO", "Coca-Cola Enterprises": "CCE", "Cognizant Technology Solutions": "CTSH", "Colgate-Palmolive": "CL", "Comcast Corp.": "CMCSA", "Comerica ": "CMA", "Computer Sciences Corp.": "CSC", "ConAgra Foods ": "CAG", "ConocoPhillips": "COP", "CONSOL Energy ": "CNX", "Consolidated Edison": "ED", "Constellation Brands": "STZ", "Corning ": "GLW", "Costco ": "COST", "Coventry Health Care ": "CVH", "Covidien plc": "COV", "Crown Castle International Corp.": "CCI", "CSX Corp.": "CSX", "Cummins ": "CMI", "CVS Caremark Corp.": "CVS", "D. R. Horton": "DHI", "Danaher Corp.": "DHR", "Darden Restaurants": "DRI", "DaVita ": "DVA", "Dean Foods": "DF", "Deere & ": "DE", "Dell ": "DELL", "Denbury Resources ": "DNR", "Dentsply International": "XRAY", "Devon Energy Corp.": "DVN", "Diamond Offshore Drilling": "DO", "DirecTV": "DTV", "Discover Financial Services": "DFS", "Discovery Communications": "DISCA", "Dollar General": "DG", "Dollar Tree": "DLTR", "Dominion Resources": "D", "Donnelley (R.R.) & Sons": "RRD", "Dover Corp.": "DOV", "Dow Chemical": "DOW", "Dr Pepper Snapple Group": "DPS", "DTE Energy ": "DTE", "Du Pont (E.I.)": "DD", "Duke Energy": "DUK", "Dun & Bradstreet": "DNB", "E-Trade": "ETFC", "Eastman Chemical": "EMN", "Eaton Corp.": "ETN", "eBay ": "EBAY", "Ecolab ": "ECL", "Edison Int'l": "EIX", "Edwards Lifesciences": "EW", "Electronic Arts": "EA", "EMC Corp.": "EMC", "Emerson Electric": "EMR", "Ensco plc": "ESV", "Entergy Corp.": "ETR", "EOG Resources": "EOG", "EQT Corporation": "EQT", "Equifax ": "EFX", "Equity Residential": "EQR", "Estee Lauder Cos.": "EL", "Exelon Corp.": "EXC", "Expedia ": "EXPE", "Expeditors Int'l": "EXPD", "Express Scripts": "ESRX", "Exxon Mobil Corp.": "XOM", "F5 Networks": "FFIV", "Family Dollar Stores": "FDO", "Fastenal ": "FAST", "Federated Investors ": "FII", "FedEx Corporation": "FDX", "Fidelity National Information Services": "FIS", "Fifth Third Bancorp": "FITB", "First Horizon National": "FHN", "First Solar ": "FSLR", "FirstEnergy Corp": "FE", "Fiserv ": "FISV", "FLIR Systems": "FLIR", "Flowserve Corporation": "FLS", "Fluor Corp.": "FLR", "FMC Corporation": "FMC", "FMC Technologies ": "FTI", "Ford Motor": "F", "Forest Laboratories": "FRX", "Fossil, ": "FOSL", "Franklin Resources": "BEN", "Freeport-McMoran Cp & Gld": "FCX", "Frontier Communications": "FTR", "GameStop Corp.": "GME", "Gannett ": "GCI", "Gap (The)": "GPS", "General Dynamics": "GD", "General Electric": "GE", "General Mills": "GIS", "Genuine Parts": "GPC", "Genworth Financial ": "GNW", "Gilead Sciences": "GILD", "Goldman Sachs Group": "GS", "Goodyear Tire & Rubber": "GT", "Google ": "GOOG", "Grainger (W.W.) ": "GWW", "Halliburton ": "HAL", "Harley-Davidson": "HOG", "Harman Int'l Industries": "HAR", "Harris Corporation": "HRS", "Hartford Financial Svc.Gp.": "HIG", "Hasbro ": "HAS", "HCP ": "HCP", "Health Care REIT": "HCN", "Heinz (H.J.)": "HNZ", "Helmerich & Payne": "HP", "Hess Corporation": "HES", "Hewlett-Packard": "HPQ", "Home Depot": "HD", "Honeywell Int'l ": "HON", "Hormel Foods Corp.": "HRL", "Hospira ": "HSP", "Host Hotels & Resorts": "HST", "Hudson City Bancorp": "HCBK", "Humana ": "HUM", "Huntington Bancshares": "HBAN", "Illinois Tool Works": "ITW", "Ingersoll-Rand PLC": "IR", "Integrys Energy Group ": "TEG", "Intel Corp.": "INTC", "IntercontinentalExchange ": "ICE", "International Bus. Machines": "IBM", "International Flav/Frag": "IFF", "International Game Technology": "IGT", "International Paper": "IP", "Interpublic Group": "IPG", "Intuit ": "INTU", "Intuitive Surgical ": "ISRG", "Invesco Ltd.": "IVZ", "Iron Mountain Incorporated": "IRM", "Jabil Circuit": "JBL", "Jacobs Engineering Group": "JEC", "JDS Uniphase Corp.": "JDSU", "Johnson & Johnson": "JNJ", "Johnson Controls": "JCI", "Joy Global ": "JOY", "JPMorgan Chase & ": "JPM", "Juniper Networks": "JNPR", "Kellogg ": "K", "KeyCorp": "KEY", "Kimberly-Clark": "KMB", "Kimco Realty": "KIM", "Kinder Morgan": "KMI", "KLA-Tencor Corp.": "KLAC", "Kohl's Corp.": "KSS", "Kraft Foods Group": "KRFT", "Kroger ": "KR", "L-3 Communications Holdings": "LLL", "Laboratory Corp. of America Holding": "LH", "Lam Research": "LRCX", "Legg Mason": "LM", "Leggett & Platt": "LEG", "Lennar Corp.": "LEN", "Leucadia National Corp.": "LUK", "Life Technologies": "LIFE", "Lilly (Eli) & ": "LLY", "Limited Brands ": "LTD", "Lincoln National": "LNC", "Linear Technology Corp.": "LLTC", "Lockheed Martin Corp.": "LMT", "Loews Corp.": "L", "Lorillard ": "LO", "Lowe's Cos.": "LOW", "LSI Corporation": "LSI", "LyondellBasell": "LYB", "M&T Bank Corp.": "MTB", "Macy's ": "M", "Marathon Oil Corp.": "MRO", "Marathon Petroleum": "MPC", "Marriott Int'l.": "MAR", "Marsh & McLennan": "MMC", "Masco Corp.": "MAS", "Mastercard ": "MA", "Mattel ": "MAT", "McCormick & ": "MKC", "McDonald's Corp.": "MCD", "McGraw-Hill": "MHP", "McKesson Corp.": "MCK", "Mead Johnson": "MJN", "MeadWestvaco Corporation": "MWV", "Medtronic ": "MDT", "Merck & ": "MRK", "MetLife ": "MET", "MetroPCS Communications ": "PCS", "Microchip Technology": "MCHP", "Micron Technology": "MU", "Microsoft Corp.": "MSFT", "Molex ": "MOLX", "Molson Coors Brewing Company": "TAP", "Mondelez International": "MDLZ", "Monsanto ": "MON", "Monster Beverage": "MNST", "Moody's Corp": "MCO", "Morgan Stanley": "MS", "The Mosaic Company": "MOS", "Motorola Solutions ": "MSI", "Murphy Oil": "MUR", "Mylan ": "MYL", "Nabors Industries Ltd.": "NBR", "NASDAQ OMX Group": "NDAQ", "National Oilwell Varco ": "NOV", "NetApp": "NTAP", "NetFlix ": "NFLX", "Newell Rubbermaid ": "NWL", "Newfield Exploration ": "NFX", "Newmont Mining Corp. (Hldg. )": "NEM", "News Corporation": "NWSA", "NextEra Energy Resources": "NEE", "NIKE ": "NKE", "NiSource ": "NI", "Noble Corp": "NE", "Noble Energy ": "NBL", "Nordstrom": "JWN", "Norfolk Southern Corp.": "NSC", "Northern Trust Corp.": "NTRS", "Northrop Grumman Corp.": "NOC", "Northeast Utilities": "NU", "NRG Energy": "NRG", "Nucor Corp.": "NUE", "Nvidia Corporation": "NVDA", "NYSE Euronext": "NYX", "O'Reilly Automotive": "ORLY", "Occidental Petroleum": "OXY", "Omnicom Group": "OMC", "ONEOK": "OKE", "Oracle Corp.": "ORCL", "Owens-Illinois ": "OI", "PACCAR ": "PCAR", "Pall Corp.": "PLL", "Parker-Hannifin": "PH", "Patterson Companies": "PDCO", "Paychex ": "PAYX", "Peabody Energy": "BTU", "Penney (J.C.)": "JCP", "Pentair Ltd.": "PNR", "People's United Bank": "PBCT", "Pepco Holdings ": "POM", "PepsiCo ": "PEP", "PerkinElmer": "PKI", "Perrigo": "PRGO", "PetSmart, ": "PETM", "Pfizer ": "PFE", "PG&E Corp.": "PCG", "Philip Morris International": "PM", "Phillips 66": "PSX", "Pinnacle West Capital": "PNW", "Pioneer Natural Resources": "PXD", "Pitney-Bowes": "PBI", "Plum Creek Timber ": "PCL", "PNC Financial Services": "PNC", "Polo Ralph Lauren Corp.": "RL", "PPG Industries": "PPG", "PPL Corp.": "PPL", "Praxair ": "PX", "Precision Castparts": "PCP", "Priceline.com ": "PCLN", "Principal Financial Group": "PFG", "Procter & Gamble": "PG", "Progressive Corp.": "PGR", "ProLogis": "PLD", "Prudential Financial": "PRU", "Public Serv. Enterprise ": "PEG", "Public Storage": "PSA", "Pulte Homes ": "PHM", "QEP Resources": "QEP", "Quanta Services ": "PWR", "QUALCOMM ": "QCOM", "Quest Diagnostics": "DGX", "Range Resources Corp.": "RRC", "Raytheon ": "RTN", "Red Hat ": "RHT", "Regions Financial Corp.": "RF", "Republic Services ": "RSG", "Reynolds American ": "RAI", "Robert Half International": "RHI", "Rockwell Automation ": "ROK", "Rockwell Collins": "COL", "Roper Industries": "ROP", "Ross Stores ": "ROST", "Rowan Cos.": "RDC", "Ryder System": "R", "Safeway ": "SWY", "SAIC": "SAI", "Salesforce.com": "CRM", "SanDisk Corporation": "SNDK", "SCANA Corp": "SCG", "Schlumberger Ltd.": "SLB", "Scripps Networks Interactive ": "SNI", "Seagate Technology": "STX", "Sealed Air Corp.(New)": "SEE", "Sempra Energy": "SRE", "Sherwin-Williams": "SHW", "Sigma-Aldrich": "SIAL", "Simon Property Group ": "SPG", "SLM Corporation": "SLM", "Smucker (J.M.)": "SJM", "Snap-On ": "SNA", "Southern ": "SO", "Southwest Airlines": "LUV", "Southwestern Energy": "SWN", "Spectra Energy Corp.": "SE", "Sprint Nextel Corp.": "S", "St Jude Medical": "STJ", "Stanley Black & Decker": "SWK", "Staples ": "SPLS", "Starbucks Corp.": "SBUX", "Starwood Hotels & Resorts": "HOT", "State Street Corp.": "STT", "Stericycle ": "SRCL", "Stryker Corp.": "SYK", "SunTrust Banks": "STI", "Symantec Corp.": "SYMC", "Sysco Corp.": "SYY", "T. Rowe Price Group": "TROW", "Target Corp.": "TGT", "TE Connectivity Ltd.": "TEL", "TECO Energy": "TE", "Tenet Healthcare Corp.": "THC", "Teradata Corp.": "TDC", "Teradyne ": "TER", "Tesoro Petroleum ": "TSO", "Texas Instruments": "TXN", "Textron ": "TXT", "The Hershey Company": "HSY", "The Travelers Companies ": "TRV", "Thermo Fisher Scientific": "TMO", "Tiffany & ": "TIF", "Time Warner ": "TWX", "Time Warner Cable ": "TWC", "Titanium Metals Corp": "TIE", "TJX Companies ": "TJX", "Torchmark Corp.": "TMK", "Total System Services": "TSS", "TripAdvisor": "TRIP", "Tyson Foods": "TSN", "Tyco International": "TYC", "U.S. Bancorp": "USB", "Union Pacific": "UNP", "United Health Group ": "UNH", "United Parcel Service": "UPS", "United States Steel Corp.": "X", "United Technologies": "UTX", "Unum Group": "UNM", "Urban Outfitters": "URBN", "V.F. Corp.": "VFC", "Valero Energy": "VLO", "Varian Medical Systems": "VAR", "Ventas ": "VTR", "Verisign ": "VRSN", "Verizon Communications": "VZ", "Viacom ": "VIAB", "Visa ": "V", "Vornado Realty Trust": "VNO", "Vulcan Materials": "VMC", "Wal-Mart Stores": "WMT", "Walgreen ": "WAG", "Walt Disney ": "DIS", "Washington Post  B": "WPO", "Waste Management ": "WM", "Waters Corporation": "WAT", "Watson Pharmaceuticals": "WPI", "WellPoint ": "WLP", "Wells Fargo": "WFC", "Western Digital": "WDC", "Western Union ": "WU", "Weyerhaeuser Corp.": "WY", "Whirlpool Corp.": "WHR", "Whole Foods Market": "WFM", "Williams Cos.": "WMB", "Windstream Corporation": "WIN", "Wisconsin Energy Corporation": "WEC", "WPX Energy, ": "WPX", "Wyndham Worldwide": "WYN", "Wynn Resorts Ltd": "WYNN", "Xcel Energy ": "XEL", "Xerox Corp.": "XRX", "Xilinx ": "XLNX", "XL Capital": "XL", "Xylem ": "XYL", "Yahoo ": "YHOO", "Yum! Brands ": "YUM", "Zimmer Holdings": "ZMH", "Zions Bancorp": "ZION"}

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
        for i in range(3):
            
            if i ==0:
                
                current_price = ystockquote.get_price(company_name)
            
            #print newsId,company_name,strftime("%Y-%m-%d %H:%M:%S", gmtime()),sentiment,sentiment_score,current_price
            #Sleeping for some time before recording the time again
            time.sleep(STOCK_GUAGE_TIME_INTERVAL_DIFFERENCE)
            #after
            new_price = ystockquote.get_price(company_name)
            
            logger.info('[DATA] : %s,%s,%s,%s,%s,%s,%s',str(newsId),str(company_name), str(time.ctime()), str(sentiment), str(sentiment_score), str(current_price), str(new_price))
    
        # Kick off another thread that will fetch the price of the same quote after 5 mins.
     
companies = []

def checkIfValidTweet(tweetData):
        news_link = ''
        company_name = 'DUMMY'
        # Check if the news link is about a news source we care about
        
        # search the tweet for any of the
        for key, value in Predictor.companies_ticker.iteritems():
            match = re.search(key, tweetData, re.I)       
            if match:
                logger.debug("Company name matched : %s ",key)
                company_name = value
       
        link_exists = re.search("http", tweetData)
        if link_exists:
            news_link = re.search("(?P<url>(http|https)?://[^\s]+)", tweetData).group("url")
            logger.debug("Found link : %s ",news_link)
    
        # Parse the link out of the tweet
    
        # Check if the new tweet is part of already parsed tweet. Don't do analysis again
    
        if((news_link not in Predictor.links_repository) and news_link != '' and company_name!='DUMMY' ):
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

test_tweet_text = "@Reuters Apple is awesome http://www.reuters.com/article/2012/12/07/apple-manufacturing-idUSL1E8N63YT20121207"  
for tweet in stream:
#while True:
     
    
    logger.debug("Incoming tweet: %s", tweet["text"])
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
        logger.debug("Uninterested Tweet: %s", tweet["text"])     

    # Once previous action is done, kick off another thread to look for stock price in 5 mins and document 

