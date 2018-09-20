import json

class ModelInfo(object):

    def __init__(self, modelType, model):
        self.type = modelType
        self.context_window = model.window
        self.min_freq = model.min_count
        self.epochs = model.epochs
        self.method = self.setMethod(model.sg)

    def setMethod(self, skipgram):
        if skipgram:
            return 'skip-gram'
        else:
            return 'CBOW'

    def toJson(self):
        return json.dumps(self.__dict__, sort_keys=True)






