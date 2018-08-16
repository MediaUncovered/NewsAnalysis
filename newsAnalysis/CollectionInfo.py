from newsAnalysis.Collection import Collection
import json

class CollectionInfo(object):

    def __init__(self, path=None):
        if path:
            collection = Collection(path)
            self.newspaper = self.newspaperName(path)
            self.nr_articles = collection.count()
        else:
            pass

    def newspaperName(self, path):
        filename = path.split('/')[-1]
        newspaper = filename.split('_')[:-1]
        return ' '.join(newspaper)

    def toJson(self):
        return json.dumps(self.__dict__)





