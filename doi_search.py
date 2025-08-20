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
import csv, sys
# My modules
import find_doi

def read_research_outputs(filename):
    with open(filename, newline='') as f:
        reader = csv.reader(f, dialect='excel', delimiter=',')
        try:
            for row in reader:
                if row[1] == 'Title' and row[2] == 'Journal':
                    print('Skipping field names...')
                else:
                    print(row)
        except csv.Error as e:
            sys.exit(f'file {filename}, line {reader.line_num}: {e}')



def main():
    read_research_outputs(sys.argv[1])

if __name__ == '__main__':
    sys.exit(main())
