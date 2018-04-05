from sys import argv
from datastore import model
from datastore import collect


def createDatabase(DATABASE, HOST, PORT, USER, PASSWORD, data_path, doc_limit=1000):
    ''' Acesses a SQL database to write the first n articles with their id, id of newspaper, date of publication, title and body to a .csv file '''

    engine = model.engine(database_user=DATABASE, database_password=PASSWORD, database_host=HOST, database_port=PORT, database_name=DATABASE)

    session = model.session(engine)
    collect.download_articles_to_file(session, data_path, source_id=1, limit=int(doc_limit))

