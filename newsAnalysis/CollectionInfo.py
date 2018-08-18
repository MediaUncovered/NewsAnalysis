from newsAnalysis.Collection import Collection
import json

class CollectionInfo(object):

    def __init__(self, path=None):
        if path:
            collection = Collection(path)
            self.newspaper = self.getNewspaperName(path)
            self.nr_articles = collection.count()
            self.getPublicationDateRange(collection)

    def getNewspaperName(self, path):
        filename = path.split('/')[-1]
        newspaper = filename.split('_')[:-1]
        return ' '.join(newspaper)

    def getPublicationDateRange(self, collection):
        self.earliest_publication_date = collection.get_earliest_publication_date()
        self.latest_publication_date = collection.get_latest_publication_date()

    def toJson(self):
        return json.dumps(self.__dict__, sort_keys=True)





