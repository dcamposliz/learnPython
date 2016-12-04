#! python3
#----------------------------------------------------------
# scrapeSite.py opens and scrapes a site of your choosing
#----------------------------------------------------------
# execute in the command line:
#
#   python3 scrapeSite.py <site_to_scrape>
#----------------------------------------------------------

# importing required modules
import sys, requests, webbrowser, bs4

# declaring command-line argument as variable
# this argument should be webpage to be scraped
siteToScrape = ''.join(sys.argv[1:])

# opening webpage in default browser
# webbrowser.open(siteToScrape)

# scraping source code for webpage
res = requests.get(siteToScrape)

# checking for errors
res.raise_for_status()

# creating file to dump scraped source code
playFile = open('scrapeMent.txt', 'wb')

# dumping scraped source code into file in "chunks" of 100000 bytes at a time
for chunk in res.iter_content(100000):
    playFile.write(chunk)

noStarchSoup = bs4.BeautifulSoup(res.text, "html.parser")
print(type(noStarchSoup))
