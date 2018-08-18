# -*- coding: utf-8 -*-
from nltk.tokenize import sent_tokenize, word_tokenize
from datetime import datetime
import csv

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
MIN_DATE = datetime.strptime('0001-01-01 00:00:00', DATE_FORMAT)
MAX_DATE = datetime.now()

class Collection(object):

    def __init__(self, path):
        self.path = path

    def load_articles(self):
        with open(self.path, 'r') as f:
            articles = csv.DictReader(f)
            for article in articles:
                yield article

    def __iter__(self):
        for article in self.load_articles():
            processed_article = article['body'].lower()
            for sentence in sent_tokenize(processed_article):
                yield word_tokenize(sentence)

    def count(self):
        count=0
        for article in self.load_articles():
            if article['body']:
                count += 1
        return count

    def get_earliest_publication_date(self):
        earliest_publication_date = MAX_DATE
        for article in self.load_articles():
            if article['published']:
                date = datetime.strptime(article['published'], DATE_FORMAT)
                if date < earliest_publication_date:
                    earliest_publication_date = date
        return earliest_publication_date.strftime(DATE_FORMAT)

    def get_latest_publication_date(self):
        latest_publication_date =  MIN_DATE
        for article in self.load_articles():
            if article['published']:
                date = datetime.strptime(article['published'], DATE_FORMAT)
                if date > latest_publication_date:
                    latest_publication_date = date
        return latest_publication_date.strftime(DATE_FORMAT)
