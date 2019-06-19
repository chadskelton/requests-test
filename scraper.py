import requests
import scraperwiki
import BeautifulSoup

scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})

html = requests.get('https://bweb.kwantlen.ca/pls/prodss/bwysched.p_select_term?wsea_code=ACAD')

htmlpage = html.content

print htmlpage

soup = BeautifulSoup(htmlpage)

print soup
