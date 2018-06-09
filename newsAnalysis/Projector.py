import os
import json
import webbrowser

class Projector:

    def __init__(self, path='../embedding-projector-standalone'):
        self.projector_path = path
        self.data_path = os.path.join(self.projector_path, 'oss_data')
        self.setConfig()

    def run(self):
        index_file = self.projector_path  + '/index.html'
        webbrowser.open_new_tab(index_file)

    def setConfig(self):
        self.config = {}
        self.config["embeddings"] = []
        self.config["modelCheckpointPath"] = "Demo Datasets"

    def addModelToConfig(self, name, path, metadata_path, vocabLength, vectorSize):
        self.config['embeddings'].append({'tensorName': name, 'tensorShape': [vocabLength,vectorSize], 'tensorPath': path, 'metadataPath': metadata_path})


    def writeConfigFile(self):
        config_file = os.path.join(self.data_path, 'oss_demo_projector_config.json')
        with open(config_file, 'w') as config:
            json.dump(self.config, config)
