import requests
import scraperwiki

scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})

r = requests.post('http://vancouversun.com/')

print r.text
