# -*- coding: utf-8 -*-
from nltk.tokenize import sent_tokenize, word_tokenize
from newsAnalysis.datastore import collect


def open(path):
    articles = collect.articles_in_file(path)
    for article in articles:
        sentences = process(article.body)
        for sentence in sentences:
            yield sentence


def process(text):
    text = text.lower()
    sentences = sent_tokenize(text)
    return [word_tokenize(sentence) for sentence in sentences]


def save(path):
    output = open(path, 'wb')
    for sentence in self:
        output.writelines(' '.join(sentence))
    output.close()
