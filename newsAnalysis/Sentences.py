# -*- coding: utf-8 -*-
from nltk.tokenize import sent_tokenize, word_tokenize
import csv

class Sentences(object):

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

