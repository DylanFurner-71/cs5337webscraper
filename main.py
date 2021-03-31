# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from pip._vendor.distlib.compat import raw_input


from docopt import docopt


doc = """Usage:
  main.py main new <pycharm> <spiderOutReaderIn> <outputfile>
  """

from Database import Database
from InvertedIndex import InvertedIndex
from ReadResults import ReadResults
import sys

def main(argv):

    print("arguments:", argv)
    readresults = ReadResults(argv[0])
    readresults.read_file()
    nonText = readresults.get_non_text()
    external = readresults.get_external()
    duplicates = readresults.get_duplicates()
    realD = readresults.get_realD()
    print("There are ", len(nonText), "non text pages")
    print("There are ", len(duplicates), "duplicate pages ")
    print("There are ", len(external), "external urls")
    print("The application will now index", len(realD), "urls found on www.freemanmoore.net")
    db = Database()
    index = InvertedIndex(db)
    numIterations = 0
    for x in realD:
        fullString = x['body']
        if not x['title'] == []:
            fullString += x['title'][0]
        document1 = {
        'id': numIterations,
        'text': fullString
        }
        index.index_document(document1)
        numIterations +=1

    print('Here is our index')
    index.print_index(len(realD), argv[1])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))
    main(sys.argv[1:])
