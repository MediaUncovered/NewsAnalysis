import os
import json
import shutil
import webbrowser

DATA_FOLDER = 'oss_data'

class Projector:

    def __init__(self, model_name, file_path, path='./projector'):
        self.model_name = model_name
        self.file_path = file_path
        self.projector_path = path
        self.setConfig()

    def set_model_paths(self):
        self.model_path = os.path.join(DATA_FOLDER, self.model_name + '.bytes')
        self.metadata_path = os.path.join(DATA_FOLDER, self.model_name + '_metadata.tsv')

    def copyModelFiles(self):
        shutil.copy(self.file_path+'.bytes', os.path.join(self.projector_path, self.model_path))
        shutil.copy(self.file_path+'_metadata.tsv', os.path.join(self.projector_path, self.metadata_path))

    def run(self, vocab_size, embedding_size):
        self.set_model_paths()
        self.copyModelFiles()
        self.addModelToConfig(self.model_name, self.model_path, self.metadata_path, vocab_size, embedding_size)
        self.writeConfigFile()
        webbrowser.open_new_tab(self.projector_path + '/index.html')

    def setConfig(self):
        self.config = {}
        self.config["embeddings"] = []
        self.config["modelCheckpointPath"] = "Demo Datasets"

    def addModelToConfig(self, name, path, metadata_path, vocabLength, vectorSize):
        self.config['embeddings'].append({'tensorName': name, 'tensorShape': [vocabLength,vectorSize], 'tensorPath': path, 'metadataPath': metadata_path})

    def writeConfigFile(self):
        config_file = os.path.join(self.projector_path, DATA_FOLDER, 'oss_demo_projector_config.json')
        with open(config_file, 'w') as config:
            json.dump(self.config, config)
