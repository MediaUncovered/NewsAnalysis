from sys import argv
from data import model
from data import collect

DATABASE = argv[1]
HOST = argv[2]
PORT = argv[3]
USER = argv[4]
PASSWORD = argv[5]

def createDatabase():

    engine = model.engine(database_user=DATABASE, database_password=PASSWORD, database_host=HOST, database_port=PORT, database_name=DATABASE)

    session = model.session(engine)
    collect.download_articles_to_file(session, "articles.csv")


if __name__=='__main__':
    createDatabase()
