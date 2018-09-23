from newsAnalysis.datastore import collect
from newsAnalysis.datastore import model


def createDatabase(DATABASE, HOST, PORT, USER, PASSWORD, data_path, doc_limit=1000, newspaper=None):
    ''' Acesses a SQL database to write the first n articles with their id, id of newspaper, date of publication, title and body to a .csv file '''

    engine = model.engine(database_user=DATABASE, database_password=PASSWORD, database_host=HOST, database_port=PORT, database_name=DATABASE)
    session = model.session(engine)
    if newspaper:
        sources = collect.get_sources(session)
        source_id = sources[newspaper]
    else:
        source_id = 1
    collect.download_articles_to_file(session, data_path, source_id=source_id, limit=int(doc_limit))

