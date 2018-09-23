# -*- coding: utf-8 -*-
'''
Handles transport of big data for analysis
'''
from newsAnalysis.datastore.model import Article
from newsAnalysis.datastore.model import Source
import unicodecsv as csv
import os


def get_sources(session):
    sources = session.query(Source).all()
    return dict([(source.name, source.id) for source in sources])

def download_articles_to_file(session, file_path, source_id=1, limit=None):
    '''
    session
        An SqlAlchemy Session
    file_path : String
        The path of the file to write to. Will be appended to if it exists and
        already contains data.
    source_id : integer
        The id of the source. For example: The source_id of Moscow Times is 1.
    limit : Integer
        The maximum amount of articles to be downloaded
    '''
    # Find the last id to resume with
    print ("detecting latest id")
    downloaded_articles_count = 0
    last_id = 0
    file_exists = os.path.isfile(file_path)
    if file_exists:
        with open(file_path, "rb") as f:
            reader = csv.reader(f)
            for row in reader:
                last_id = int(row[0])
                downloaded_articles_count += 1
    print ("%d aricles have already been downloaded" % downloaded_articles_count)
    print ("found latest id %d" % last_id)

    corrected_limit = None
    if limit is not None:
        corrected_limit = max(0, limit - downloaded_articles_count)
    print("corrected_limit = %r" % corrected_limit)

    if corrected_limit is None or corrected_limit > 0:
        query = session.query(Article)\
                    .filter(Article.body.isnot(None))\
                    .filter(Article.id >= last_id)\
                    .filter(Article.source_id == source_id)\
                    .order_by(Article.id)\
                    .limit(corrected_limit)\
                    .yield_per(10)

        with open(file_path, "ab") as f:
            writer = csv.writer(f, encoding='utf-8')
            if not file_exists:
                writer.writerow(['id', 'source_id', 'published', 'title', 'body'])
            for article in query:
                print("%d" % (article.id))
                writer.writerow(
                    [article.id, article.source_id, article.published, article.title, article.body]
                )

