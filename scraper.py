import requests
import scraperwiki
import BeautifulSoup

scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})

html = requests.get('http://www.chadskelton.com/')

htmlpage = html.content

soup = BeautifulSoup(htmlpage)

print soup
