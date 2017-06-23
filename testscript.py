from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.tradingview.com/chart/?symbol=BITSTAMP:BTCUSD'
 #read data from url
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
#html
pageSoup = soup(page_html,"html.parser")
#grab videogame container
containers = pageSoup.findAll("div",{"class" : "s-item-container"})
pageSoup.div
