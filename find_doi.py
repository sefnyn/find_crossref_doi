"""

Find Crossref DOI for specific title and journal

Usage:
    >>> import find_doi
    >>> find_doi.find(title, journal)

Returns:


Execute module as a script:
    python3 find_doi.py title journal

    e.g.
    python3 find_doi.py "Non-cuttable material inspired by seashells" "TheScienceBreaker"


Request URL:
https://api.crossref.org/works?mailto=sefnyn%40gmail.com&query=query.title%3Dnon-cuttable%2Bmaterial%2Binspired%2Bby%2Bseashells%26container-title%3Dthesciencebreaker

Curl:
curl -X 'GET' \
  'https://api.crossref.org/works?mailto=sefnyn%40gmail.com&query=query.title%3Dnon-cuttable%2Bmaterial%2Binspired%2Bby%2Bseashells%26container-title%3Dthesciencebreaker' \
  -H 'accept: application/json'

"""

#import crossref_commons.retrieval
import json
import sys
import urllib
import requests
from requests.structures import CaseInsensitiveDict

#test dois
#  Stefan:  10.25250/thescbr.brk569
#  Jas:     10.1021/acsanm.1c03151

def find(title, journal):
    new_title = title.replace(' ', '+')
    new_journal = journal.replace(' ', '+')

    url = 'https://api.crossref.org/works'
    headers = {'user-agent': 'Python-script-written-by-Syrotiuk'}
    params = {'mailto': 'pzvx49@durham.ac.uk',
               'query.title': new_title,
               'query.container-title': new_journal,
               'select': 'DOI,author,title,container-title,volume,issue,page,published'
             }
 
    response = requests.get(url, headers=headers, params=params)
    print(response.status_code)

    if response.status_code == 200:
        bibrec = read(response.json()['message']['items'][0])
        print(bibrec)
    elif response.status_code == 429:
        print('Too many API requests.  Please wait a short while and try your request again at a lower rate and/or with lower concurrency.')
    else:
        print('Did not find ' + title + ' in Crossref database')
        return None

def read(d):
    bibrec = dict(author = [], title = "", journal = "", issue = "", volume = "", pages = "", pub_year = "", doi = "")
    try:
        bibrec['author']   = d['author']
    except KeyError:
        print('Did not find author')
    bibrec['title']    = d['title']
    bibrec['journal']  = d['container-title']
    try:
        bibrec['volume']   = d['volume']
    except KeyError:
        print('Did not find volume')
    try:
        bibrec['issue']    = d['issue']
    except KeyError:
        print("Did not find issue")
    try:
        bibrec['pages']    = d['page']
    except KeyError:
        print('Did not find pages')
    bibrec['pub_year']     = d['published']['date-parts'][0][0]
    bibrec['doi']          = 'http://doi.org/' + d['DOI']

    return bibrec


def main():
    find(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    sys.exit(main())  # 

