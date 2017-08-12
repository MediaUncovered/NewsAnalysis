# -*- coding: utf-8 -*-
from __future__ import generators
import psycopg2
import pdb
from nltk import tokenize


class Sentences:


    def __init__(self):
        pass


    def connectDatabase(self, info):
        self.connection = psycopg2.connect(database=info.database, host=info.host, port=info.port, password=info.password, user=info.user)


    def queryDatabase(self, selection='*', collection='articles', notEmpty='body'):
        QUERY = "SELECT %s FROM %s WHERE %s.%s IS NOT NULL LIMIT 10" % (selection, collection, collection, notEmpty)
        self.cursor = self.connection.cursor('test')
        self.cursor.itersize = 2000
        self.cursor.execute(QUERY)


    def __iter__(self, dataLimit=50):
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
        sentences = tokenize.sent_tokenize(text)
        return [sentence.split() for sentence in sentences]





