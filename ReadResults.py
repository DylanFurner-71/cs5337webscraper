import json
class ReadResults:
    """
    In memory database representing the already indexed documents.
    """

    def __init__(self, arguments):
        self.nonText = []
        self.external = []
        self.duplicates = []
        self.realD = []
        self.readFile = arguments

    def get_non_text(self):
        return self.nonText

    def get_external(self):
        return self.external
    def get_duplicates(self):
        return self.duplicates
    def get_realD(self):
        return self.realD
    def read_file(self):
        f = open(self.readFile)

        # returns JSON object as
        # a dictionary
        data = json.load(f)

        # Iterating through the json
        # list
        for i in data:
            if 'nonText' in i:
                self.nonText.append(i)
            if 'isDuplicate' in i:
                self.duplicates.append(i)
            if 'external' in i:
                self.external.append(i)
            if 'body' in i and not 'isDuplicate' in i:
                self.realD.append(i)

        # Closing file
        f.close()