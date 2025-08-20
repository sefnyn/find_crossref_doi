# Check Crossref for one or more journal articles

A couple of scripts that take one or more journal articles and look for DOIs in Crossref.

## Requirements
pip3 install requests

## Find one DOI
Usage:  python3 find_doi.py "title of journal article" "title of journal"   <-- Quotation marks are mandatory

### Example 1:
> >> python3 find_doi.py 'Non-cuttable material inspired by seashells' 'TheScienceBreaker'  
> HTTP response 200  
> Found DOI  
> Did not find pages  
> {'author': [{'given': 'Stefan', 'family': 'Szyniszewski', 'sequence': 'first', 'affiliation': []}, {'given': 'Miranda', 'family': 'Anderson', 'sequence': 'additional', 'affiliation': []}], 'title': ['Non-cuttable material inspired by seashells'], 'journal': ['TheScienceBreaker'], 'issue': '03', 'volume': '07', 'pages': '', 'pub_year': 2021, 'doi': 'http://doi.org/10.25250/thescbr.brk569'}

### Example 2:
> >> python3 find_doi.py "Trans-conceptual sampling Bayesian inference with competing assumptions" "Journal of Geophysical Research Solid Earth"  
> HTTP response 200  
> Did not find "Trans-conceptual sampling Bayesian inference with competing assumptions" in Crossref database   

## Search for DOIs
Usage:  python3 doi_search.py CSV_FILE  

Format of CSV_FILE:
