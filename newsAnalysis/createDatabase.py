from sys import argv
from datastore import model
from datastore import collect

DATABASE = argv[1]
HOST = argv[2]
PORT = argv[3]
USER = argv[4]
PASSWORD = argv[5]

def createDatabase():

    path = 'articles3.csv'
    doc_limit = 120

    engine = model.engine(database_user=DATABASE, database_password=PASSWORD, database_host=HOST, database_port=PORT, database_name=DATABASE)

    session = model.session(engine)
    collect.download_articles_to_file(session, source_id=1, limit=doc_limit)


if __name__=='__main__':
    createDatabase()
