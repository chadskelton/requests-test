import requests
r = requests.post('https://bweb.kwantlen.ca/pls/prodss/bwysched.p_search_fields', data = {'term_code':'201920', 'wsea_code':'ACAD'})
