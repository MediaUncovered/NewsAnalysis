from sys import argv
from datastore import model
from datastore import collect
import pdb


def createDatabase(DATABASE, HOST, PORT, USER, PASSWORD, data_path, doc_limit=1000):

    engine = model.engine(database_user=DATABASE, database_password=PASSWORD, database_host=HOST, database_port=PORT, database_name=DATABASE)

    session = model.session(engine)
    collect.download_articles_to_file(session, data_path, source_id=1, limit=int(doc_limit))


if __name__=='__main__':
    createDatabase()
