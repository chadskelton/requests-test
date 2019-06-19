import requests
import scraperwiki

scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})

r = requests.get('http://vancouversun.com/')

print(r.text)
