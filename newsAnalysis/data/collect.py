# -*- coding: utf-8 -*-
'''
Handles transport of big data for analysis
'''
from data.model import Article
import unicodecsv as csv
import os


def download_articles_to_file(session, file_path, source_id=1):
    '''
    connection
        A psycopg2 connection
    file_path : String
        The path of the file to write to. Will be appended to if it exists and
        already contains data.
    source_id : integer
        The id of the source. For example: The source_id of Moscow Times is 1.
    '''

    # Find the last id to resume with
    print ("detecting latest id")
    last_id = 0
    if os.path.isfile(file_path):
        with open(file_path, "rb") as f:
            reader = csv.reader(f)
            for row in reader:
                last_id = int(row[0])
    print ("found latest id %d" % last_id)

    query = session.query(Article)\
                .filter(Article.body.isnot(None))\
                .filter(Article.id >= last_id)\
                .filter(Article.source_id == source_id)\
                .order_by(Article.id)\
                .yield_per(10)

    with open(file_path, "ab") as f:
        writer = csv.writer(f, encoding='utf-8')
        for article in query:
            print("%d %s" % (article.id, article.title))
            writer.writerow(
                [article.id, article.source_id, article.published, article.title, article.body]
            )


def articles_in_file(file_path):
    '''
    file_path : String
        The path of the file to read from.
    '''
    with open(file_path, "rb") as f:
        reader = csv.reader(f, encoding='utf-8')
        for row in reader:
            article = Article(id=row[0], source_id=row[1],
                                    published=row[2], title=row[3], body=row[4])
            yield article
