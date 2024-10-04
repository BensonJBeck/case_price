from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

req = Request(url= 'https://www.csgodatabase.com/cases/',
    headers={'User-Agent': 'Mozilla/5.0'})

page = urlopen(req).read()
soup = BeautifulSoup(page, 'html.parser')

price_dat = soup.find_all('span', attrs={'class': 'price'})

total = 0.0

for i in price_dat[5:34]:
    total += float(i.text.strip()[1:])

print('$ ' + str(total/29))
    
