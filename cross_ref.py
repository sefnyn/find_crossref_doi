"""

Retrieve bibliographic information from DOI

Usage:
    >>> import cross_ref
    >>> cross_ref.get_pub(doi)

    Returns a Python dictionary with structure:
    {
        'author': 
            [{'ORCID': 
                'http://orcid.org/0000-0001-5966-6083', 
                'authenticated-orcid': True, 
                'given': 'Harrison J.', 
                'family': 'Cox', 
                'sequence': 'first', 
                'affiliation': [{'name': 'Department of Chemistry, Durham University, Durham DH1 3LE, England, U.K.'}]}, 
            {'given': 'Gary J.', 
                'family': 'Sharples', 
                'sequence': 
                'additional', 
                'affiliation': [{'name': 'Department of Biosciences, Durham University, Durham DH1 3LE, England, U.K.'}]}, 
            {'ORCID': 
                'http://orcid.org/0000-0002-5086-5737', 
                'authenticated-orcid': True, 
                'given': 'Jas Pal S.', 
                'family': 'Badyal', 
                'sequence': 'additional', 
                'affiliation': [{'name': 'Department of Chemistry, Durham University, Durham DH1 3LE, England, U.K.'}]}], 
        'title': ['Tea–Essential Oil–Metal Hybrid Nanocoatings for Bacterial and Viral Inactivation'], 
        'journal': ['ACS Applied Nano Materials'], 
        'issue': '11', 
        'volume': '4', 
        'pages': '12619-12628', 
        'pub_year': 2021
    }

Execute module as a script:
    python3 cross_ref.py prefix/suffix

    e.g.
    python3 cross_ref.py 10.25250/thescbr.brk569
"""

import crossref_commons.retrieval
import json
import sys

#test dois
#  Stefan:  10.25250/thescbr.brk569
#  Jas:     10.1021/acsanm.1c03151

def get_pub(doi):
    """Get bibliographic details for doi.

    doi must be in format xx.xxxx/yyyyyyyyy
    """

    out = 'zcrossref.json'
    fh = open(out, 'w')
    doi = clean(doi)
    try:
        data = crossref_commons.retrieval.get_publication_as_json(doi)
        print('Found doi ' + doi)
        print('Creating JSON file ' + out)
        bib_string = json.dumps(data)
        fh.write(bib_string)
        bibrec = read(data)
        print(bibrec)
        return bibrec
    except ValueError:
        print('Did not find DOI ' + doi + ' in Crossref database')
        return None

def clean(d):
    
    """
    Remove http, https etc and trailing blanks
    """
    d = d.rstrip()
    d = d.replace('http://doi.org/',"")
    d = d.replace('http://dx.doi.org/',"")
    d = d.replace('https://doi.org/',"")
    d = d.replace('https://dx.doi.org/',"")
    return d

def read(d):

    """bibrecord = 
    author=[],
    title="On generating power law noise",
    journal="Astronomy and Astrophysics",
    volume="300",
    issue="11",
    pages="707-710",
    pub_year="1995"
    """
    
    bibrec = dict(author = [], title = "", journal = "", issue = "", volume = "", pages = "", pub_year = "")
    bibrec['author']   = d['author']
    bibrec['title']    = d['title']
    bibrec['journal']  = d['container-title']
    bibrec['volume']   = d['volume']
    try:
        bibrec['issue']    = d['journal-issue']['issue']
    except KeyError:
        print("Did not find issue")
    try:
        bibrec['pages']    = d['page']
    except KeyError:
        print("Did not find pages")
    bibrec['pub_year']     = d['published']['date-parts'][0][0]

    return bibrec

def main():
    get_pub(sys.argv[1])

if __name__ == '__main__':
    sys.exit(main())  # 

