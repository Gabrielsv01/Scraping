import requests
import bs4

site = 'https://docs.python.org/3/'

res = requests.get('{}'.format(site))

soup = bs4.BeautifulSoup(res.text,'lxml')

hi = soup.select('title')
print(hi[0].getText())
