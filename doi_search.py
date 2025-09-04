"""

DOI_SEARCH

This little script reads a CSV file and calls the Python module FIND_DOI for each research output described in the file


Example usage:
find_doi.find('Non-cuttable material inspired by seashells', 'TheScienceBreaker')


Input CSV file:
Output ID,Title,Journal                                                                            
4403954,University-Industry Collaboration for Academic Success and Employability: A Connectivist Perspective,Studies in Higher Education
4401294,Commonality of 25 Component Themes of integrated care for children: rapid review of 170 models,BMC Health Service Research
4402062,A monetary policy accordion: Why do central banks from different countries expand and contract together?,Journal of Macroeconomics


Output CSV file(s):
TBC

"""
import os, csv, sys
# My modules
import find_doi

count = 0
misses = 0
hits = 0
csv_misses = 'misses.csv'
csv_hits   = 'hits.csv'

def read_research_outputs(filename):
    fname = os.path.splitext(filename)[0]
    ext   = os.path.splitext(filename)[1]
    new   = fname + "_processed" + ext
    fh1 = open(csv_misses, 'w')
    writer1 = csv.writer(fh1)
    fh2 = open(csv_hits, 'w')
    writer2   = csv.writer(fh2)
    fh3 = open(new, 'w')
    writer3   = csv.writer(fh3)
    global count, misses, hits
    with open(filename, newline='') as f:
        reader = csv.reader(f, dialect='excel', delimiter=',')
        try:
            for row in reader:
                oid     = row[0]
                title   = row[1]
                journal = row[2]
                if title == 'Title' and journal == 'Journal':
                    print('Skipping field names...')
                else:
                    print()
                    print('Searching Crossref for ' + str(row))
                    count += 1
                    result = find_doi.find(title, journal)
                    if result == None:
                        misses += 1
                        writer1.writerow(row)
                        writer3.writerow(row)

                    else:
                        hits += 1
                        doi = result['doi']
                        writer2.writerow([oid, title, journal, doi])
                        writer3.writerow([oid, title, journal, doi])
            print('Processed ' + str(count) + ' journal articles')
            print('Found ' + str(hits) + ' DOIs')
            print(str(misses) + ' journal articles without a DOI')
            print()
            print('Created three files:')
            print(csv_misses + ' contains journal articles without DOIs')
            print(csv_hits + ' contains journal articles with DOIs')
            print(new + ' contains DOIs in 4th column')
        except csv.Error as e:
            sys.exit(f'file {filename}, line {reader.line_num}: {e}')

def main():
    try:
        read_research_outputs(sys.argv[1])
    except IndexError:
        filepath = __file__.split('/')
        print('Usage:  python3 ' + filepath.pop()  + ' CSV_FILE where CSV_FILE is in format OutputID,Title,Journal')

if __name__ == '__main__':
    sys.exit(main())
