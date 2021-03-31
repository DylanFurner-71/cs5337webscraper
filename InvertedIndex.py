from Appearance import Appearance
import re
import pandas as pd
import xlsxwriter


class InvertedIndex:
    """
    Inverted Index class.
    """

    def __init__(self, db):
        self.index = dict()
        self.db = db


    def index_document(self, document):
        """
        Process a given document, save it to the DB and update the index.
        """

        terms = document['text'].split()
        appearances_dict = dict()
        # Dictionary with each term and the frequency it appears in the text.
        #these next 13 lines are heavily based on this website; i have never used python before and this model allowed me to conceptualize how to interact with our index
        #appearance objects contain {docId, frequency} for each instance of a documentId key pair
        for term in terms:
            term_frequency = appearances_dict[term].frequency if term in appearances_dict else 0
            appearances_dict[term] = Appearance(document['id'], term_frequency + 1)

        # Update the inverted index
        update_dict = {key: [appearance]
        if key not in self.index
        else self.index[key] + [appearance]
                       for (key, appearance) in appearances_dict.items()}
        self.index.update(update_dict)
        # Add the document into the database
        self.db.add(document)
        return document

    def print_index(self, numDocs, name):
        workbook = xlsxwriter.Workbook(name)
        worksheet = workbook.add_worksheet()

        # Start from the first cell.
        # Rows and columns are zero indexed.
        row = 1
        keys = list(self.index.keys())
        content = keys
        worksheet.write(0, 0, 'docId')
        for i in range(1, numDocs+1):
            worksheet.write(0, i, i-1)
        for item in content:
            column = 0
            worksheet.write(row, column, item)
            for appearance in self.index[item]:
                column = appearance.docId + 1
                worksheet.write(row, column, appearance.frequency)
            row +=1
        # incrementing the value of row by one
            # with each iteratons.
        workbook.close()
