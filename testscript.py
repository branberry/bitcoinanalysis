from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://99bitcoins.com/price-chart-history/'
 #read data from url
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
#html
pageSoup = soup(page_html,"html.parser")
#grab videogame container
containers = pageSoup.findAll("div",{"class" : "s-item-container"})
