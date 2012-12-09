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
from time import gmtime, strftime


STOCK_GUAGE_TIME_INTERVAL_DIFFERENCE = 5



class Predictor(object):
    links_repository = []    
    companies_ticker = {"3M ": "MMM", "ACE Limited": "ACE", "Abbott Laboratories": "ABT", "Abercrombie & Fitch mpany A": "ANF", "Accenture": "ACN", "Adobe Systems ": "ADBE", "ADT rp": "ADT", "Advanced Micro Devices": "AMD", "AES rp": "AES", "Aetna ": "AET", "AFLAC ": "AFL", "Agilent Technologies ": "A", "AGL Resources ": "GAS", "Air Products & Chemicals ": "APD", "Airgas ": "ARG", "Akamai Technologies ": "AKAM", "Ala ": "AA", "Alexion Pharmaceuticals": "ALXN", "Allegheny Technologies ": "ATI", "Allergan ": "AGN", "Allstate rp": "ALL", "Altera rp": "ALTR", "Altria Group ": "MO", "Amazon.m ": "AMZN", "Ameren rp": "AEE", "American Electric Power": "AEP", "American Express ": "AXP", "American Intl Group ": "AIG", "American Tower rp A": "AMT", "Ameriprise Financial": "AMP", "AmerisourceBergen rp": "ABC", "Amgen ": "AMGN", "Amphenol rp A": "APH", "Anadarko Petroleum rp": "APC", "Analog Devices ": "ADI", "Aon plc": "AON", "Apache rporation": "APA", "Apartment Investment & Mgmt": "AIV", "Apollo Group ": "APOL", "Apple ": "AAPL", "Applied Materials ": "AMAT", "Archer-Daniels-Midland ": "ADM", "Assurant ": "AIZ", "AT&T ": "T", "Autodesk ": "ADSK", "Automatic Data Processing": "ADP", "AutoNation ": "AN", "AutoZone ": "AZO", "AvalonBay mmunities, ": "AVB", "Avery Dennison rp": "AVY", "Avon Products": "AVP", "Baker Hughes ": "BHI", "Ball rp": "BLL", "Bank of America rp": "BAC", "The Bank of New York Mellon rp.": "BK", "Bard (C.R.) ": "BCR", "Baxter International ": "BAX", "BB&T rporation": "BBT", "Beam ": "BEAM", "Becton Dickinson": "BDX", "Bed Bath & Beyond": "BBBY", "Bemis mpany": "BMS", "Berkshire Hathaway": "BRK.B", "Best Buy  ": "BBY", "Big Lots ": "BIG", "BIOGEN IDEC ": "BIIB", "BlackRock": "BLK", "Block H&R": "HRB", "BMC Software": "BMC", "Boeing mpany": "BA", "BorgWarner": "BWA", "Boston Properties": "BXP", "Boston Scientific": "BSX", "Bristol-Myers Squibb": "BMY", "Broadm rporation": "BRCM", "Brown-Forman rporation": "BF.B", "C. H. Robinson Worldwide": "CHRW", "CA, ": "CA", "Cablevision Systems rp.": "CVC", "Cabot Oil & Gas": "G", "Cameron International rp.": "CAM", "Campbell Soup": "CPB", "Capital One Financial": "F", "Cardinal Health ": "CAH", "Carefusion": "CFN", "Carmax ": "KMX", "Carnival rp.": "CCL", "Caterpillar ": "CAT", "CBRE Group": "CBG", "CBS rp.": "CBS", "Celgene rp.": "CELG", "CenterPoint Energy": "CNP", "CenturyLink ": "CTL", "Cerner": "CERN", "CF Industries Holdings ": "CF", "Charles Schwab": "SCHW", "Chesapeake Energy": "CHK", "Chevron rp.": "CVX", "Chipotle Mexican Grill": "CMG", "Chubb rp.": "CB", "CIGNA rp.": "CI", "Cinnati Financial": "CINF", "Cintas rporation": "CTAS", "Cis Systems": "CS", "Citigroup ": "C", "Citrix Systems": "CTXS", "Cliffs Natural Resources": "CLF", "The Clorox mpany": "CLX", "CME Group ": "CME", "CMS Energy": "CMS", "ach ": "H", "ca la ": "KO", "ca-la Enterprises": "CCE", "gnizant Technology Solutions": "CTSH", "lgate-Palmolive": "CL", "mcast rp.": "CMCSA", "merica ": "CMA", "mputer Sciences rp.": "CSC", "nAgra Foods ": "CAG", "noPhillips": "P", "NSOL Energy ": "CNX", "nsolidated Edison": "ED", "nstellation Brands": "STZ", "rning ": "GLW", "st ": "ST", "ventry Health Care ": "CVH", "vidien plc": "V", "Crown Castle International rp.": "CCI", "CSX rp.": "CSX", "Cummins ": "CMI", "CVS Caremark rp.": "CVS", "D. R. Horton": "DHI", "Danaher rp.": "DHR", "Darden Restaurants": "DRI", "DaVita ": "DVA", "Dean Foods": "DF", "Deere & ": "DE", "Dell ": "DELL", "Denbury Resources ": "DNR", "Dentsply International": "XRAY", "Devon Energy rp.": "DVN", "Diamond Offshore Drilling": "DO", "DirecTV": "DTV", "Disver Financial Services": "DFS", "Disvery mmunications": "DISCA", "Dollar General": "DG", "Dollar Tree": "DLTR", "Dominion Resources": "D", "Donnelley (R.R.) & Sons": "RRD", "Dover rp.": "DOV", "Dow Chemical": "DOW", "Dr Pepper Snapple Group": "DPS", "DTE Energy ": "DTE", "Du Pont (E.I.)": "DD", "Duke Energy": "DUK", "Dun & Bradstreet": "DNB", "E-Trade": "ETFC", "Eastman Chemical": "EMN", "Eaton rp.": "ETN", "eBay ": "EBAY", "Elab ": "ECL", "Edison Int'l": "EIX", "Edwards Lifesciences": "EW", "Electronic Arts": "EA", "EMC rp.": "EMC", "Emerson Electric": "EMR", "Ens plc": "ESV", "Entergy rp.": "ETR", "EOG Resources": "EOG", "EQT rporation": "EQT", "Equifax ": "EFX", "Equity Residential": "EQR", "Estee Lauder s.": "EL", "Exelon rp.": "EXC", "Expedia ": "EXPE", "Expeditors Int'l": "EXPD", "Express Scripts": "ESRX", "Exxon Mobil rp.": "XOM", "F5 Networks": "FFIV", "Family Dollar Stores": "FDO", "Fastenal ": "FAST", "Federated Investors ": "FII", "FedEx rporation": "FDX", "Fidelity National Information Services": "FIS", "Fifth Third Banrp": "FITB", "First Horizon National": "FHN", "First Solar ": "FSLR", "FirstEnergy rp": "FE", "Fiserv ": "FISV", "FLIR Systems": "FLIR", "Flowserve rporation": "FLS", "Fluor rp.": "FLR", "FMC rporation": "FMC", "FMC Technologies ": "FTI", "Ford Motor": "F", "Forest Laboratories": "FRX", "Fossil, ": "FOSL", "Franklin Resources": "BEN", "Freeport-McMoran Cp & Gld": "FCX", "Frontier mmunications": "FTR", "GameStop rp.": "GME", "Gannett ": "GCI", "Gap (The)": "GPS", "General Dynamics": "GD", "General Electric": "GE", "General Mills": "GIS", "Genuine Parts": "GPC", "Genworth Financial ": "GNW", "Gilead Sciences": "GILD", "Goldman Sachs Group": "GS", "Goodyear Tire & Rubber": "GT", "Google ": "GOOG", "Grainger (W.W.) ": "GWW", "Halliburton ": "HAL", "Harley-Davidson": "HOG", "Harman Int'l Industries": "HAR", "Harris rporation": "HRS", "Hartford Financial Svc.Gp.": "HIG", "Hasbro ": "HAS", "HCP ": "HCP", "Health Care REIT": "HCN", "Heinz (H.J.)": "HNZ", "Helmerich & Payne": "HP", "Hess rporation": "HES", "Hewlett-Packard": "HPQ", "Home Depot": "HD", "Honeywell Int'l ": "HON", "Hormel Foods rp.": "HRL", "Hospira ": "HSP", "Host Hotels & Resorts": "HST", "Hudson City Banrp": "HCBK", "Humana ": "HUM", "Huntington Bancshares": "HBAN", "Illinois Tool Works": "ITW", "Ingersoll-Rand PLC": "IR", "Integrys Energy Group ": "TEG", "Intel rp.": "INTC", "InterntinentalExchange ": "ICE", "International Bus. Machines": "IBM", "International Flav/Frag": "IFF", "International Game Technology": "IGT", "International Paper": "IP", "Interpublic Group": "IPG", "Intuit ": "INTU", "Intuitive Surgical ": "ISRG", "Inves Ltd.": "IVZ", "Iron Mountain orporated": "IRM", "Jabil Circuit": "JBL", "Jabs Engineering Group": "JEC", "JDS Uniphase rp.": "JDSU", "Johnson & Johnson": "JNJ", "Johnson ntrols": "JCI", "Joy Global ": "JOY", "JPMorgan Chase & ": "JPM", "Juniper Networks": "JNPR", "Kellogg ": "K", "Keyrp": "KEY", "Kimberly-Clark": "KMB", "Kim Realty": "KIM", "Kinder Morgan": "KMI", "KLA-Tenr rp.": "KLAC", "Kohl's rp.": "KSS", "Kraft Foods Group": "KRFT", "Kroger ": "KR", "L-3 mmunications Holdings": "LLL", "Laboratory rp. of America Holding": "LH", "Lam Research": "LRCX", "Legg Mason": "LM", "Leggett & Platt": "LEG", "Lennar rp.": "LEN", "Leucadia National rp.": "LUK", "Life Technologies": "LIFE", "Lilly (Eli) & ": "LLY", "Limited Brands ": "LTD", "Loln National": "LNC", "Linear Technology rp.": "LLTC", "Lockheed Martin rp.": "LMT", "Loews rp.": "L", "Lorillard ": "LO", "Lowe's s.": "LOW", "LSI rporation": "LSI", "LyondellBasell": "LYB", "M&T Bank rp.": "MTB", "Macy's ": "M", "Marathon Oil rp.": "MRO", "Marathon Petroleum": "MPC", "Marriott Int'l.": "MAR", "Marsh & McLennan": "MMC", "Mas rp.": "MAS", "Mastercard ": "MA", "Mattel ": "MAT", "Mcrmick & ": "MKC", "McDonald's rp.": "MCD", "McGraw-Hill": "MHP", "McKesson rp.": "MCK", "Mead Johnson": "MJN", "MeadWestva rporation": "MWV", "Medtronic ": "MDT", "Merck & ": "MRK", "MetLife ": "MET", "MetroPCS mmunications ": "PCS", "Microchip Technology": "MCHP", "Micron Technology": "MU", "Microsoft rp.": "MSFT", "Molex ": "MOLX", "Molson ors Brewing mpany": "TAP", "Mondelez International": "MDLZ", "Monsanto ": "MON", "Monster Beverage": "MNST", "Moody's rp": "M", "Morgan Stanley": "MS", "The Mosaic mpany": "MOS", "Motorola Solutions ": "MSI", "Murphy Oil": "MUR", "Mylan ": "MYL", "Nabors Industries Ltd.": "NBR", "NASDAQ OMX Group": "NDAQ", "National Oilwell Var ": "NOV", "NetApp": "NTAP", "NetFlix ": "NFLX", "Newell Rubbermaid ": "NWL", "Newfield Exploration ": "NFX", "Newmont Mining rp. (Hldg. )": "NEM", "News rporation": "NWSA", "NextEra Energy Resources": "NEE", "NIKE ": "NKE", "NiSource ": "NI", "Noble rp": "NE", "Noble Energy ": "NBL", "Nordstrom": "JWN", "Norfolk Southern rp.": "NSC", "Northern Trust rp.": "NTRS", "Northrop Grumman rp.": "NOC", "Northeast Utilities": "NU", "NRG Energy": "NRG", "Nur rp.": "NUE", "Nvidia rporation": "NVDA", "NYSE Euronext": "NYX", "O'Reilly Automotive": "ORLY", "Occidental Petroleum": "OXY", "Omnim Group": "OMC", "ONEOK": "OKE", "Oracle rp.": "ORCL", "Owens-Illinois ": "OI", "PACCAR ": "PCAR", "Pall rp.": "PLL", "Parker-Hannifin": "PH", "Patterson mpanies": "PD", "Paychex ": "PAYX", "Peabody Energy": "BTU", "Penney (J.C.)": "JCP", "Pentair Ltd.": "PNR", "People's United Bank": "PBCT", "Pep Holdings ": "POM", "Pepsi ": "PEP", "PerkinElmer": "PKI", "Perrigo": "PRGO", "PetSmart, ": "PETM", "Pfizer ": "PFE", "PG&E rp.": "PCG", "Philip Morris International": "PM", "Phillips 66": "PSX", "Pinnacle West Capital": "PNW", "Pioneer Natural Resources": "PXD", "Pitney-Bowes": "PBI", "Plum Creek Timber ": "PCL", "PNC Financial Services": "PNC", "Polo Ralph Lauren rp.": "RL", "PPG Industries": "PPG", "PPL rp.": "PPL", "Praxair ": "PX", "Precision Castparts": "PCP", "Priceline.m ": "PCLN", "Pripal Financial Group": "PFG", "Procter & Gamble": "PG", "Progressive rp.": "PGR", "ProLogis": "PLD", "Prudential Financial": "PRU", "Public Serv. Enterprise ": "PEG", "Public Storage": "PSA", "Pulte Homes ": "PHM", "QEP Resources": "QEP", "Quanta Services ": "PWR", "QUALMM ": "QM", "Quest Diagnostics": "DGX", "Range Resources rp.": "RRC", "Raytheon ": "RTN", "Red Hat ": "RHT", "Regions Financial rp.": "RF", "Republic Services ": "RSG", "Reynolds American ": "RAI", "Robert Half International": "RHI", "Rockwell Automation ": "ROK", "Rockwell llins": "L", "Roper Industries": "ROP", "Ross Stores ": "ROST", "Rowan s.": "RDC", "Ryder System": "R", "Safeway ": "SWY", "SAIC": "SAI", "Salesforce.m": "CRM", "SanDisk rporation": "SNDK", "SCANA rp": "SCG", "Schlumberger Ltd.": "SLB", "Scripps Networks Interactive ": "SNI", "Seagate Technology": "STX", "Sealed Air rp.(New)": "SEE", "Sempra Energy": "SRE", "Sherwin-Williams": "SHW", "Sigma-Aldrich": "SIAL", "Simon Property Group ": "SPG", "SLM rporation": "SLM", "Smucker (J.M.)": "SJM", "Snap-On ": "SNA", "Southern ": "SO", "Southwest Airlines": "LUV", "Southwestern Energy": "SWN", "Spectra Energy rp.": "SE", "Sprint Nextel rp.": "S", "St Jude Medical": "STJ", "Stanley Black & Decker": "SWK", "Staples ": "SPLS", "Starbucks rp.": "SBUX", "Starwood Hotels & Resorts": "HOT", "State Street rp.": "STT", "Stericycle ": "SRCL", "Stryker rp.": "SYK", "SunTrust Banks": "STI", "Symantec rp.": "SYMC", "Sys rp.": "SYY", "T. Rowe Price Group": "TROW", "Target rp.": "TGT", "TE nnectivity Ltd.": "TEL", "TE Energy": "TE", "Tenet Healthcare rp.": "THC", "Teradata rp.": "TDC", "Teradyne ": "TER", "Tesoro Petroleum ": "TSO", "Texas Instruments": "TXN", "Textron ": "TXT", "The Hershey mpany": "HSY", "The Travelers mpanies ": "TRV", "Thermo Fisher Scientific": "TMO", "Tiffany & ": "TIF", "Time Warner ": "TWX", "Time Warner Cable ": "TWC", "Titanium Metals rp": "TIE", "TJX mpanies ": "TJX", "Torchmark rp.": "TMK", "Total System Services": "TSS", "TripAdvisor": "TRIP", "Tyson Foods": "TSN", "Ty International": "TYC", "U.S. Banrp": "USB", "Union Pacific": "UNP", "United Health Group ": "UNH", "United Parcel Service": "UPS", "United States Steel rp.": "X", "United Technologies": "UTX", "Unum Group": "UNM", "Urban Outfitters": "URBN", "V.F. rp.": "VFC", "Valero Energy": "VLO", "Varian Medical Systems": "VAR", "Ventas ": "VTR", "Verisign ": "VRSN", "Verizon mmunications": "VZ", "Viam ": "VIAB", "Visa ": "V", "Vornado Realty Trust": "VNO", "Vulcan Materials": "VMC", "Wal-Mart Stores": "WMT", "Walgreen ": "WAG", "Walt Disney ": "DIS", "Washington Post  B": "WPO", "Waste Management ": "WM", "Waters rporation": "WAT", "Watson Pharmaceuticals": "WPI", "WellPoint ": "WLP", "Wells Fargo": "WFC", "Western Digital": "WDC", "Western Union ": "WU", "Weyerhaeuser rp.": "WY", "Whirlpool rp.": "WHR", "Whole Foods Market": "WFM", "Williams s.": "WMB", "Windstream rporation": "WIN", "Wisnsin Energy rporation": "WEC", "WPX Energy, ": "WPX", "Wyndham Worldwide": "WYN", "Wynn Resorts Ltd": "WYNN", "Xcel Energy ": "XEL", "Xerox rp.": "XRX", "Xilinx ": "XLNX", "XL Capital": "XL", "Xylem ": "XYL", "Yahoo ": "YHOO", "Yum! Brands ": "YUM", "Zimmer Holdings": "ZMH", "Zions Banrp": "ZION"}

    def perform_analysis(self, newsId, company_name, news_link):
        
        sentiment, sentiment_score = self.perform_sentiment_analysis(company_name, news_link)
        
      
        # If sentiment is positive, perform financial analysis, if not, ignore
     
        try:
            thread.start_new_thread(Predictor.perform_financial_analysis, (Predictor(), newsId, company_name, sentiment, sentiment_score))
        except:
            print "Error: unable to start thread"
       
    


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
        for i in range(6):
            
        
            current_price = ystockquote.get_price(company_name)
            
            #print newsId,company_name,strftime("%Y-%m-%d %H:%M:%S", gmtime()),sentiment,sentiment_score,current_price
            #Sleeping for some time before recording the time again
            time.sleep(STOCK_GUAGE_TIME_INTERVAL_DIFFERENCE)
            #after
            new_price = ystockquote.get_price(company_name)
            
            print newsId, company_name, time.ctime(), sentiment, sentiment_score, current_price, new_price
    
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
                company_name = value
       
        link_exists = re.search("http", tweetData)
        if link_exists:
            news_link = re.search("(?P<url>(http|https)?://[^\s]+)", tweetData).group("url")
       
    
        # Parse the link out of the tweet
    
        # Check if the new tweet is part of already parsed tweet. Don't do analysis again
    
        if((news_link not in Predictor.links_repository) and news_link != ''):
            Predictor.links_repository.append(news_link)
                # Navigate to the new link
            return True , company_name, news_link
        else :
            return False, company_name, ''
    
    
    
    

words = []
people = [1652541]
locations = []   

stream = tweetstream.FilterStream("PDSStern", "rebeccaBlack", track=words, follow=people, locations=locations)
print "Connected to Reuters twitter stream and listening.."

tweet_text = "@Reuters Apple is awesome http://www.reuters.com/article/2012/12/07/apple-manufacturing-idUSL1E8N63YT20121207"  
#for tweet in stream:
while True:
     
    
    #print "Incoming tweet: ", tweet["text"]
    isValidTweet, company_ticker_name, news_link = checkIfValidTweet(tweet_text)
    
    if(isValidTweet):
        
        # Create a unique id and keep track 
        uniqueId = str(time.time())
        newsId = uniqueId.replace(".", "")

        # Spawn a new thread for sentiment analysis and 'trade' engine 
        try:
            thread.start_new_thread(Predictor.perform_analysis, (Predictor(), newsId, company_ticker_name, news_link))
        except:
            print "Error: unable to start thread"

    

    # Once previous action is done, kick off another thread to look for stock price in 5 mins and document 

