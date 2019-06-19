import requests
import scraperwiki

scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})

r = requests.post('https://bweb.kwantlen.ca/pls/prodss/bwysched.p_search_fields')

print r
