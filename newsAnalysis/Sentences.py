# -*- coding: utf-8 -*-
import psycopg2
import pdb
from nltk.tokenize import sent_tokenize, word_tokenize 


class Sentences:


    def __init__(self):
        pass


    def connectDatabase(self, info):
        self.connection = psycopg2.connect(database=info.database, host=info.host, port=info.port, password=info.password, user=info.user)


    def queryDatabase(self, selection='*', collection='articles', notEmpty='body', limit=5000, cursorname='test'):
        QUERY = "SELECT %s FROM %s WHERE %s.%s IS NOT NULL LIMIT %i" % (selection, collection, collection, notEmpty, limit)
        self.cursor = self.connection.cursor(cursorname)
        self.cursor.itersize = 1000
        self.cursor.execute(QUERY)


    def __iter__(self, dataLimit=1000):
        while True:
            data = self.cursor.fetchmany(dataLimit)
            if not data:
                break
            for row in data:
                sentences = self.process(row[5])
                for sentence in sentences:
                    yield sentence
        


    def process(self, text):
        text = text.lower()
        sentences = sent_tokenize(text.decode('utf8'))
        return [word_tokenize(sentence) for sentence in sentences]

    
    def save(self, path):
        output = open(path, 'wb')
        for sentence in self:
            output.writelines(' '.join(sentence))
        output.close()






