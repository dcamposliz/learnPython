#! python3
# feelingLucky.py - opens several google search results for a specific query

# to run this program, enter:
#
#   python3 feelingLucky.py <QUERY>
#
# of course, replace <QUERY> with your actual query of interest

import requests, sys, webbrowser, bs4

print('Googling...') # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links
soup = bs4.BeautifulSoup(res.text, "html.parser")

# Open a browser tab for each result
linkElems = soup.select('.r a')
numOpen = min(10, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://www.google.com' + linkElems[i].get('href'))
