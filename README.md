# Check Crossref for one or more journal articles

A couple of scripts that take one or more journal articles and look for DOIs in Crossref.

## Requirements
pip3 install requests

## Find one DOI
Usage:  python3 find_doi.py "title of journal article" "title of journal"   <-- Quotation marks or single quotes are mandatory

### Example 1:
    $ python3 find_doi.py 'Non-cuttable material inspired by seashells' 'TheScienceBreaker'  
      HTTP response 200  
      Found DOI  
      Did not find pages  
      {'author': [
          {'given': 'Stefan', 'family': 'Szyniszewski', 'sequence': 'first', 'affiliation': []},
          {'given': 'Miranda', 'family': 'Anderson', 'sequence': 'additional', 'affiliation': []}],
       'title': ['Non-cuttable material inspired by seashells'],
       'journal': ['TheScienceBreaker'],
       'issue': '03',
       'volume': '07',
       'pages': '',
       'pub_year': 2021,
       'doi': 'http://doi.org/10.25250/thescbr.brk569'
      }

### Example 2:
    $ python3 find_doi.py "Trans-conceptual sampling Bayesian inference with competing assumptions" "Journal of Geophysical Research Solid Earth"  
      HTTP response 200  
      Did not find DOI in Crossref database for "Trans-conceptual sampling Bayesian inference with competing assumptions"  

## Search for DOIs in file
Usage:  python3 doi_search.py CSV_FILE  

Format of CSV_FILE:
Output ID,Title of paper,Journal  

### Example 1:  
Contents of CSV_FILE:  
Output ID,Title,Journal                                                                                              
4423337,Human dexterity and brains evolved hand in hand,Communications Biology  
3966057,Words Without Intentions,Croatian Journal of Philosophy  

$ python3 doi_search.py CSV_FILE










